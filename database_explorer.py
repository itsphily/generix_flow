import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
from tabulate import tabulate
import os
from pathlib import Path

def create_engine_string():
    """Create SQLAlchemy engine string"""
    return f"mysql+mysqlconnector://root:demoGenerix!@35.225.14.56/agropur_prod"

def format_results_for_llm(df, query_info):
    """Format query results in a narrative style suitable for LLM consumption"""
    try:
        # Convert all column names to lowercase for consistent access
        df.columns = df.columns.str.lower()
        
        output = f"\n## {query_info['title']}\n\n"
        output += f"{query_info['description']}\n\n"
        
        # Print available columns for debugging
        print(f"Query: {query_info['title']}")
        print(f"Available columns: {df.columns.tolist()}")
        
        # Format results based on query type
        if query_info['title'].startswith("1. Database Size"):
            row = df.iloc[0]
            output += f"The database '{row['database_name']}' has a total size of {row['total_size_gb']} GB "
            output += f"and contains {row['total_tables']} tables, of which {row['tables_with_data']} contain data.\n"
        
        elif query_info['title'].startswith("2. Top 10 Largest Tables"):
            output += "The largest tables in the database are:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['table_name']}: {row['data_size_gb']} GB data, {row['index_size_gb']} GB indexes, "
                output += f"containing {row['table_rows']} rows\n"
        
        elif query_info['title'].startswith("3. Tables with Most Records"):
            output += "Tables with the highest number of records:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['table_name']}: {row['table_rows']} rows ({row['data_size_gb']} GB)\n"
        
        elif query_info['title'].startswith("4. Recent Database Activity"):
            output += "Recent table updates:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['table_name']} was updated at {row['update_time']}, "
                output += f"contains {row['table_rows']} rows ({row['data_size_gb']} GB)\n"
        
        elif query_info['title'].startswith("5. Table Engine Distribution"):
            output += "Storage engine distribution:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['engine']}: {row['table_count']} tables, total size {row['total_size_gb']} GB\n"
        
        elif query_info['title'].startswith("6. Column Details"):
            current_table = None
            output += "Table structure details:\n\n"
            for _, row in df.iterrows():
                if current_table != row['table_name']:
                    current_table = row['table_name']
                    output += f"\n### {current_table}\n"
                
                key_info = f" ({row['key_type']})" if row['key_type'] else ""
                nullable = "nullable" if row['is_nullable'] == 'YES' else "not nullable"
                output += f"- {row['column_name']}: {row['column_type']} - {nullable}{key_info}\n"
        
        elif query_info['title'].startswith("7. Summary of Top Tables"):
            output += "Structure summary for major tables:\n\n"
            for _, row in df.iterrows():
                output += f"### {row['table_name']}\n"
                output += f"- Total columns: {row['total_columns']}\n"
                output += f"- Primary keys: {row['primary_keys']}\n"
                output += f"- Foreign keys: {row['foreign_keys']}\n"
                output += f"- Nullable columns: {row['nullable_columns']}\n"
                output += f"- Data types used: {row['data_types']}\n\n"
        
        elif query_info['title'].startswith("8. Daily Operation"):
            output += "Daily operation patterns:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['operation_date']}: {row['operation_type']} - "
                output += f"{row['operation_count']} operations by {row['unique_users']} users\n"
        
        elif query_info['title'].startswith("9. Order Processing"):
            output += "Order processing performance:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['order_date']}: {row['total_orders']} orders, "
                output += f"avg processing time {row['avg_processing_minutes']:.1f} minutes, "
                output += f"{row['completed_orders']} completed, {row['cancelled_orders']} cancelled\n"
        
        elif query_info['title'].startswith("10. Inventory Movement"):
            output += "Inventory movement patterns:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['movement_type']}: {row['movement_count']} movements, "
                output += f"{row['unique_items']} unique items, avg quantity {row['avg_quantity']:.1f}\n"
        
        elif query_info['title'].startswith("11. Material Adjustments"):
            output += "Material adjustments analysis:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['adjustment_date']}: {row['adjustment_type']} - "
                output += f"{row['adjustment_count']} adjustments, "
                output += f"{row['positive_adjustments']} positive, {row['negative_adjustments']} negative, "
                output += f"avg adjustment size {row['avg_adjustment_size']:.1f}\n"
        
        elif query_info['title'].startswith("12. Picking Performance"):
            output += "Picking performance analysis:\n\n"
            for _, row in df.iterrows():
                output += f"- {row['pick_date']}: {row['total_picks']} picks, "
                output += f"{row['unique_pickers']} unique pickers, avg pick time {row['avg_pick_time_minutes']:.1f} minutes, "
                output += f"{row['accuracy_percentage']:.1f}% accuracy\n"
        
        return output
    except KeyError as e:
        print(f"Error: Column {e} not found in results")
        print(f"Available columns: {df.columns.tolist()}")
        return f"\n## {query_info['title']}\nError processing results: missing column {e}\n\n"
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return f"\n## {query_info['title']}\nError processing results: {str(e)}\n\n"

def run_database_analysis():
    """Run key database analysis queries and write results to queries.md"""
    engine = create_engine(create_engine_string())
    
    # List of queries with descriptions
    queries = [
        {
            'title': "0. Available Tables",
            'description': "Lists all tables in the database with their actual names",
            'query': """
                SELECT 
                    table_name,
                    table_rows,
                    ROUND(data_length/1024/1024/1024, 2) as data_size_gb
                FROM information_schema.tables 
                WHERE table_schema = 'agropur_prod'
                    AND table_rows > 0
                ORDER BY table_name;
            """
        },
        {
            'title': "1. Database Size and Table Count",
            'description': "Overview of database size, total tables, and tables with data",
            'query': """
                SELECT 
                    table_schema as database_name,
                    ROUND(SUM(data_length + index_length)/1024/1024/1024, 2) as total_size_gb,
                    COUNT(*) as total_tables,
                    SUM(CASE WHEN table_rows > 0 THEN 1 ELSE 0 END) as tables_with_data
                FROM information_schema.tables
                WHERE table_schema = 'agropur_prod'
                GROUP BY table_schema;
            """
        },
        {
            'title': "2. Top 10 Largest Tables",
            'description': "Identifies the largest tables by data size",
            'query': """
                SELECT 
                    table_name,
                    ROUND(data_length/1024/1024/1024, 2) as data_size_gb,
                    ROUND(index_length/1024/1024/1024, 2) as index_size_gb,
                    table_rows
                FROM information_schema.tables
                WHERE table_schema = 'agropur_prod'
                    AND table_rows > 0
                ORDER BY (data_length + index_length) DESC
                LIMIT 10;
            """
        },
        {
            'title': "3. Tables with Most Records",
            'description': "Shows tables with the highest number of rows",
            'query': """
                SELECT 
                    table_name,
                    table_rows,
                    ROUND(data_length/1024/1024/1024, 2) as data_size_gb
                FROM information_schema.tables
                WHERE table_schema = 'agropur_prod'
                    AND table_rows > 0
                ORDER BY table_rows DESC
                LIMIT 10;
            """
        },
        {
            'title': "4. Recent Database Activity",
            'description': "Shows tables with recent updates",
            'query': """
                SELECT 
                    table_name,
                    update_time,
                    table_rows,
                    ROUND(data_length/1024/1024/1024, 2) as data_size_gb
                FROM information_schema.tables
                WHERE table_schema = 'agropur_prod'
                    AND update_time IS NOT NULL
                ORDER BY update_time DESC
                LIMIT 10;
            """
        },
        {
            'title': "5. Table Engine Distribution",
            'description': "Shows distribution of storage engines used in the database",
            'query': """
                SELECT 
                    engine,
                    COUNT(*) as table_count,
                    ROUND(SUM(data_length + index_length)/1024/1024/1024, 2) as total_size_gb
                FROM information_schema.tables
                WHERE table_schema = 'agropur_prod'
                    AND engine IS NOT NULL
                GROUP BY engine
                ORDER BY total_size_gb DESC;
            """
        },
        {
            'title': "6. Column Details for All Active Tables",
            'description': "Lists all columns and their data types for all tables containing data",
            'query': """
                SELECT 
                    c.table_name,
                    c.column_name,
                    c.data_type,
                    c.column_type,
                    c.is_nullable,
                    CASE 
                        WHEN c.column_key = 'PRI' THEN 'Primary Key'
                        WHEN c.column_key = 'MUL' THEN 'Foreign Key'
                        WHEN c.column_key = 'UNI' THEN 'Unique Key'
                        ELSE ''
                    END as key_type
                FROM information_schema.columns c
                JOIN information_schema.tables t 
                    ON c.table_name = t.table_name 
                    AND c.table_schema = t.table_schema
                WHERE c.table_schema = 'agropur_prod'
                    AND t.table_rows > 0
                ORDER BY 
                    c.table_name,
                    CASE WHEN c.column_key = 'PRI' THEN 0
                         WHEN c.column_key = 'MUL' THEN 1
                         WHEN c.column_key = 'UNI' THEN 2
                         ELSE 3
                    END,
                    c.column_name;
            """
        },
        {
            'title': "7. Summary of Top Tables Structure",
            'description': "Shows a summary of column types and keys for each large table",
            'query': """
                WITH TopTables AS (
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = 'agropur_prod'
                        AND table_rows > 0
                    ORDER BY table_rows DESC
                    LIMIT 10
                )
                SELECT 
                    c.table_name,
                    COUNT(*) as total_columns,
                    SUM(CASE WHEN c.column_key = 'PRI' THEN 1 ELSE 0 END) as primary_keys,
                    SUM(CASE WHEN c.column_key = 'MUL' THEN 1 ELSE 0 END) as foreign_keys,
                    SUM(CASE WHEN c.is_nullable = 'YES' THEN 1 ELSE 0 END) as nullable_columns,
                    GROUP_CONCAT(DISTINCT c.data_type) as data_types
                FROM information_schema.columns c
                JOIN TopTables t ON c.table_name = t.table_name
                WHERE c.table_schema = 'agropur_prod'
                GROUP BY c.table_name
                ORDER BY total_columns DESC;
            """
        },
        {
            'title': "8. Daily Operation Volumes",
            'description': "Analyzes daily operation patterns in the warehouse",
            'query': """
                SELECT 
                    DATE(eventDate) as operation_date,
                    type as operation_type,
                    COUNT(*) as operation_count,
                    COUNT(DISTINCT user_id) as unique_users
                FROM scMovement
                WHERE eventDate >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                GROUP BY DATE(eventDate), type
                ORDER BY operation_date DESC, operation_count DESC;
            """
        },
        {
            'title': "9. Order Processing Performance",
            'description': "Analyzes order processing times and completion rates",
            'query': """
                SELECT 
                    DATE(createStamp) as order_date,
                    COUNT(*) as total_orders,
                    AVG(TIMESTAMPDIFF(MINUTE, createStamp, updateStamp)) as avg_processing_minutes,
                    COUNT(CASE WHEN status = 'COMPLETED' THEN 1 END) as completed_orders,
                    COUNT(CASE WHEN status = 'CANCELLED' THEN 1 END) as cancelled_orders
                FROM scOrderLine
                WHERE createStamp >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                GROUP BY DATE(createStamp)
                ORDER BY order_date DESC;
            """
        },
        {
            'title': "10. Inventory Movement Patterns",
            'description': "Analyzes patterns in inventory movements",
            'query': """
                SELECT 
                    type as movement_type,
                    COUNT(*) as movement_count,
                    COUNT(DISTINCT item_id) as unique_items,
                    AVG(quantity) as avg_quantity,
                    COUNT(DISTINCT fromLocation_id) as unique_locations
                FROM scMovement
                WHERE eventDate >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                GROUP BY type
                HAVING movement_count > 100
                ORDER BY movement_count DESC;
            """
        },
        {
            'title': "11. Material Adjustments Analysis",
            'description': "Analyzes patterns in inventory adjustments",
            'query': """
                SELECT 
                    DATE(eventDate) as adjustment_date,
                    type as adjustment_type,
                    COUNT(*) as adjustment_count,
                    SUM(CASE WHEN adjustedQty > 0 THEN 1 ELSE 0 END) as positive_adjustments,
                    SUM(CASE WHEN adjustedQty < 0 THEN 1 ELSE 0 END) as negative_adjustments,
                    AVG(ABS(adjustedQty)) as avg_adjustment_size
                FROM scMIAdjustment
                WHERE eventDate >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                GROUP BY DATE(eventDate), type
                ORDER BY adjustment_date DESC, adjustment_count DESC;
            """
        },
        {
            'title': "12. Picking Performance Analysis",
            'description': "Analyzes picking operation efficiency",
            'query': """
                SELECT 
                    DATE(pickedDate) as pick_date,
                    COUNT(*) as total_picks,
                    COUNT(DISTINCT pickedByUser_id) as unique_pickers,
                    AVG(TIMESTAMPDIFF(MINUTE, createStamp, pickedDate)) as avg_pick_time_minutes,
                    SUM(CASE WHEN pickedQty = quantity THEN 1 ELSE 0 END) / COUNT(*) * 100 as accuracy_percentage
                FROM scPKLI
                WHERE pickedDate >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                GROUP BY DATE(pickedDate)
                ORDER BY pick_date DESC;
            """
        }
    ]
    
    # Create the markdown content
    markdown_content = "# Database Analysis and Structure\n\n"
    markdown_content += "Analysis performed on: " + pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"
    
    # Run each query and append results to markdown
    for query_info in queries:
        # Execute query and get results
        df = pd.read_sql(query_info['query'], engine)
        
        # Format results in a narrative style
        markdown_content += format_results_for_llm(df, query_info)
        markdown_content += "\n---\n\n"
    
    # Write to file
    output_path = Path("/Users/phili/Library/CloudStorage/Dropbox/Phil/LeoMarketing/Marketing/Generix/flow_ai_generix/docs/queries.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write(markdown_content)
    
    print(f"Results have been written to: {output_path}")

if __name__ == "__main__":
    run_database_analysis() 