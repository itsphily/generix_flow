# Flow AI Generix

A Python package that uses AI to analyze database structures, execute queries, and generate comprehensive insights. The system uses CrewAI to orchestrate a team of specialized AI agents that work together to analyze database trends and generate detailed reports.

## Features

- Automated database structure analysis
- AI-powered query generation and optimization
- Trend analysis and reporting
- Hierarchical AI agent collaboration
- Markdown report generation

## Prerequisites

- Python 3.8+
- MySQL database access
- OpenAI API key
- Required Python packages (installed automatically via setup.py)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flow_ai_generix.git
cd flow_ai_generix
```

2. Install the package in development mode:
```bash
pip install -e .
```

## Configuration

1. Create a `.env` file in the root directory with:
```env
OPENAI_API_KEY=your_openai_api_key
MYSQL_CONNECTION_STRING=mysql+mysqlconnector://user:password@host/database
MYSQL_DATABASE_NAME=your_database_name
```

2. Set up your documentation files in the docs/ directory:
   - queries.md: Contains database query results
   - trends.md: Contains trends to analyze

## Project Structure

```
flow_ai_generix/
├── docs/
│   ├── queries.md
│   └── trends.md
├── src/
│   └── flow_ai_generix/
│       ├── crews/
│       │   └── research_crew/
│       │       ├── config/
│       │       │   ├── agents.yaml
│       │       │   └── tasks.yaml
│       │       └── research_crew.py
│       ├── pipelines/
│       │   └── pipeline.py
│       └── main.py
├── setup.py
├── .env
└── README.md
```

## Usage

1. Run the database explorer to generate queries.md:
```python
python database_explorer.py
```

2. Create your trends.md file in the docs directory.

3. Run the main analysis:
```python
python -m flow_ai_generix.main
```

## AI Agents

The system uses three specialized AI agents:

1. **Query Writer**: Generates SQL queries based on trends and database structure
2. **Query Reviewer**: Reviews and optimizes queries for efficiency
3. **Data Analyst**: Analyzes results and generates comprehensive reports

## Output

The system generates a "Database Analysis.md" file containing:
- Trend analysis
- Data interpretations
- Visualizations
- Recommendations
- Limitations and considerations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
