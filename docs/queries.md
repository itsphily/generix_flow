# Database Analysis Queries and Results

Analysis performed on: 2024-11-05 08:25:24

## 1. Database Size and Table Count

Overview of database size, total tables, and tables with data

### Query:
```sql
SELECT 
                    table_schema as database_name,
                    ROUND(SUM(data_length + index_length)/1024/1024/1024, 2) as total_size_gb,
                    COUNT(*) as total_tables,
                    SUM(CASE WHEN table_rows > 0 THEN 1 ELSE 0 END) as tables_with_data
                FROM information_schema.tables
                WHERE table_schema = 'agropur_prod'
                GROUP BY table_schema;
```

### Results:
| database_name   |   total_size_gb |   total_tables |   tables_with_data |
|:----------------|----------------:|---------------:|-------------------:|
| agropur_prod    |          247.37 |            777 |                516 |

---

## 2. Top 10 Largest Tables

Identifies the largest tables by data size

### Query:
```sql
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
```

### Results:
| TABLE_NAME              |   data_size_gb |   index_size_gb |   TABLE_ROWS |
|:------------------------|---------------:|----------------:|-------------:|
| scGeneratedMREQ         |          72.73 |            2.78 |     16668583 |
| scMovement              |          13.51 |           31.43 |     55454691 |
| scMIAdjustment          |          11.74 |           10.39 |     76114843 |
| sysImportedItem         |          16.73 |            0.28 |      2720933 |
| sysProcessProfiling     |           8.56 |            6.19 |     44153523 |
| sysInterfaceArchive     |          12.62 |            0.01 |       660867 |
| scLineAdjustment        |           6.27 |            2.78 |     36046571 |
| scMaterial              |           3.57 |            4.09 |      9633411 |
| scMIAdjustmentDimension |           4.37 |            3.21 |     64015150 |
| scPKLI                  |           2.05 |            3.4  |      7004251 |

---

## 3. Tables with Most Records

Shows tables with the highest number of rows

### Query:
```sql
SELECT 
                    table_name,
                    table_rows,
                    ROUND(data_length/1024/1024/1024, 2) as data_size_gb
                FROM information_schema.tables
                WHERE table_schema = 'agropur_prod'
                    AND table_rows > 0
                ORDER BY table_rows DESC
                LIMIT 10;
```

### Results:
| TABLE_NAME              |   TABLE_ROWS |   data_size_gb |
|:------------------------|-------------:|---------------:|
| scMIAdjustment          |     76114843 |          11.74 |
| scMIAdjustmentDimension |     64015150 |           4.37 |
| scMovement              |     55454691 |          13.51 |
| oidToTable              |     48054858 |           1.47 |
| sysProcessProfiling     |     44153523 |           8.56 |
| scLineAdjustment        |     36046571 |           6.27 |
| sysEvent                |     20021938 |           1.67 |
| scGeneratedMREQ         |     16668583 |          72.73 |
| scOrderAdjustment       |     13272123 |           1.59 |
| scMaterial              |      9633411 |           3.57 |

---

## 4. Recent Database Activity

Shows tables with recent updates

### Query:
```sql
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
```

### Results:
| TABLE_NAME         | UPDATE_TIME         |   TABLE_ROWS |   data_size_gb |
|:-------------------|:--------------------|-------------:|---------------:|
| users              | 2024-11-02 12:38:07 |          654 |           0    |
| sysWorkflowSession | 2024-11-02 12:38:06 |           36 |           0    |
| testObject         | 2024-11-02 12:38:06 |           12 |           0    |
| sysWIFIAccessPoint | 2024-11-02 12:38:06 |            0 |           0    |
| sysUserSession     | 2024-11-02 12:38:06 |       226223 |           0.04 |
| sysUserTransaction | 2024-11-02 12:38:06 |         1101 |           0    |
| sysUserRole        | 2024-11-02 12:37:44 |          856 |           0    |
| sysUserPermission  | 2024-11-02 12:37:44 |         2895 |           0    |
| sysUserAgent       | 2024-11-02 12:37:43 |          649 |           0    |
| sysUIProfiling     | 2024-11-02 12:37:43 |      5455454 |           1.17 |

---

## 5. Table Engine Distribution

Shows distribution of storage engines used in the database

### Query:
```sql
SELECT 
                    engine,
                    COUNT(*) as table_count,
                    ROUND(SUM(data_length + index_length)/1024/1024/1024, 2) as total_size_gb
                FROM information_schema.tables
                WHERE table_schema = 'agropur_prod'
                    AND engine IS NOT NULL
                GROUP BY engine
                ORDER BY total_size_gb DESC;
```

### Results:
| ENGINE   |   table_count |   total_size_gb |
|:---------|--------------:|----------------:|
| InnoDB   |           777 |          247.37 |

---

## 6. Column Details for All Active Tables

Lists all columns and their data types for all tables containing data

### Query:
```sql
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
```

### Results:
| TABLE_NAME                       | COLUMN_NAME                                       | DATA_TYPE   | COLUMN_TYPE    | IS_NULLABLE   | key_type    |
|:---------------------------------|:--------------------------------------------------|:------------|:---------------|:--------------|:------------|
| billGLAccount                    | oid                                               | int         | int            | NO            | Primary Key |
| billGLAccount                    | classoid                                          | int         | int            | NO            |             |
| billGLAccount                    | code                                              | varchar     | varchar(255)   | NO            |             |
| billGLAccount                    | description                                       | text        | text           | NO            |             |
| event                            | oid                                               | bigint      | bigint         | NO            | Primary Key |
| event                            | classoid                                          | int         | int            | NO            | Foreign Key |
| event                            | eventCode                                         | varchar     | varchar(255)   | NO            | Foreign Key |
| event                            | mioid                                             | int         | int            | NO            | Foreign Key |
| event                            | refoid                                            | int         | int            | NO            | Foreign Key |
| event                            | siteoid                                           | int         | int            | NO            | Foreign Key |
| event                            | tooid                                             | int         | int            | NO            | Foreign Key |
| event                            | adjustedQty                                       | bigint      | bigint         | NO            |             |
| event                            | comments                                          | text        | text           | NO            |             |
| event                            | definition_id                                     | int         | int            | NO            |             |
| event                            | eventDate                                         | datetime    | datetime       | NO            |             |
| event                            | eventType                                         | varchar     | varchar(255)   | NO            |             |
| event                            | fromoid                                           | int         | int            | NO            |             |
| event                            | location                                          | varchar     | varchar(255)   | NO            |             |
| event                            | qty                                               | bigint      | bigint         | NO            |             |
| event                            | stamp                                             | datetime    | datetime       | NO            |             |
| event                            | useroid                                           | int         | int            | NO            |             |
| ints                             | i                                                 | int         | int            | NO            | Primary Key |
| objectid                         | entityName                                        | varchar     | varchar(255)   | NO            | Foreign Key |
| objectid                         | next                                              | int         | int            | NO            |             |
| objectid                         | range_start                                       | int         | int            | NO            |             |
| objectid                         | range_stop                                        | int         | int            | NO            |             |
| oidToTable                       | oid                                               | int         | int            | NO            | Primary Key |
| oidToTable                       | classoid                                          | int         | int            | NO            | Foreign Key |
| oidToTable                       | table_id                                          | int         | int            | NO            | Foreign Key |
| scABCClass                       | oid                                               | int         | int            | NO            | Primary Key |
| scABCClass                       | classoid                                          | int         | int            | NO            |             |
| scABCClass                       | description                                       | text        | text           | NO            |             |
| scABCClass                       | name                                              | varchar     | varchar(255)   | NO            |             |
| scABCClass                       | sequence                                          | int         | int            | NO            |             |
| scABCClass                       | site_id                                           | int         | int            | NO            |             |
| scABCConfiguration               | oid                                               | int         | int            | NO            | Primary Key |
| scABCConfiguration               | abcClass_id                                       | int         | int            | NO            |             |
| scABCConfiguration               | classoid                                          | int         | int            | NO            |             |
| scABCConfiguration               | countingJob_id                                    | int         | int            | NO            |             |
| scABCConfiguration               | frequency                                         | int         | int            | NO            |             |
| scABCConfiguration               | generationMode                                    | varchar     | varchar(255)   | NO            |             |
| scABCConfiguration               | owner_id                                          | int         | int            | NO            |             |
| scABCConfiguration               | priority                                          | varchar     | varchar(255)   | NO            |             |
| scABCConfiguration               | route_id                                          | int         | int            | NO            |             |
| scABCConfiguration               | schedule_id                                       | int         | int            | NO            |             |
| scABCConfiguration               | site_id                                           | int         | int            | NO            |             |
| scAddress                        | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scAddress                        | address1                                          | varchar     | varchar(255)   | NO            |             |
| scAddress                        | address2                                          | varchar     | varchar(255)   | NO            |             |
| scAddress                        | address3                                          | varchar     | varchar(255)   | NO            |             |
| scAddress                        | address4                                          | varchar     | varchar(255)   | NO            |             |
| scAddress                        | addresstype                                       | varchar     | varchar(255)   | NO            |             |
| scAddress                        | city                                              | varchar     | varchar(255)   | NO            |             |
| scAddress                        | classoid                                          | int         | int            | NO            |             |
| scAddress                        | country                                           | varchar     | varchar(255)   | NO            |             |
| scAddress                        | country_id                                        | int         | int            | NO            |             |
| scAddress                        | latitude                                          | varchar     | varchar(255)   | NO            |             |
| scAddress                        | longitude                                         | varchar     | varchar(255)   | NO            |             |
| scAddress                        | postalCode                                        | varchar     | varchar(255)   | NO            |             |
| scAddress                        | province                                          | varchar     | varchar(255)   | NO            |             |
| scAddress                        | site_id                                           | int         | int            | NO            |             |
| scAddress                        | stateProvince_id                                  | int         | int            | NO            |             |
| scAgropurContainerSSCC           | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scAgropurContainerSSCC           | container_id                                      | int         | int            | NO            | Foreign Key |
| scAgropurContainerSSCC           | deliveryNo                                        | varchar     | varchar(255)   | NO            | Foreign Key |
| scAgropurContainerSSCC           | pklh_id                                           | int         | int            | NO            | Foreign Key |
| scAgropurContainerSSCC           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scAgropurContainerSSCC           | classoid                                          | int         | int            | NO            |             |
| scAgropurContainerSSCC           | creationDate                                      | datetime    | datetime       | NO            |             |
| scAgropurContainerSSCC           | generatedSSCC_id                                  | int         | int            | NO            |             |
| scAgropurContainerSSCC           | gs1LabelFormat                                    | varchar     | varchar(255)   | NO            |             |
| scAgropurContainerSSCC           | inactiveDate                                      | datetime    | datetime       | NO            |             |
| scAgropurContainerSSCC           | materialmaster_id                                 | int         | int            | NO            |             |
| scAgropurContainerSSCC           | mmdimension_id                                    | int         | int            | NO            |             |
| scAgropurContainerSSCC           | sequence                                          | int         | int            | NO            |             |
| scAgropurContainerSSCC           | sscc                                              | varchar     | varchar(255)   | NO            |             |
| scAgropurHandlingMaterialLoad    | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scAgropurHandlingMaterialLoad    | load_id                                           | int         | int            | NO            | Foreign Key |
| scAgropurHandlingMaterialLoad    | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scAgropurHandlingMaterialLoad    | classoid                                          | int         | int            | NO            |             |
| scAgropurHandlingMaterialLoad    | quantity                                          | bigint      | bigint         | NO            |             |
| scAgropurHandlingMaterialLoad    | uoi_id                                            | int         | int            | NO            |             |
| scAgropurSSCC                    | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scAgropurSSCC                    | companyPrefix                                     | varchar     | varchar(255)   | NO            | Foreign Key |
| scAgropurSSCC                    | organization                                      | varchar     | varchar(255)   | NO            | Foreign Key |
| scAgropurSSCC                    | classoid                                          | int         | int            | NO            |             |
| scAgropurSSCC                    | inactiveDate                                      | datetime    | datetime       | NO            |             |
| scAgropurSSCC                    | serial                                            | int         | int            | NO            |             |
| scAgropurSSCC                    | status                                            | varchar     | varchar(255)   | NO            |             |
| scAisle                          | oid                                               | int         | int            | NO            | Primary Key |
| scAisle                          | allocateInventory                                 | varchar     | varchar(10)    | NO            |             |
| scAisle                          | classoid                                          | int         | int            | NO            |             |
| scAisle                          | name                                              | varchar     | varchar(255)   | NO            |             |
| scAisle                          | site_id                                           | int         | int            | NO            |             |
| scAisle                          | status                                            | varchar     | varchar(255)   | NO            |             |
| scAisle                          | velocity                                          | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | oid                                               | int         | int            | NO            | Primary Key |
| scAllocateInvPolicy              | allocationUOIMode                                 | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | backorderMode                                     | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | bopolicy_id                                       | int         | int            | NO            |             |
| scAllocateInvPolicy              | boReservMode                                      | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | bozone_id                                         | int         | int            | NO            |             |
| scAllocateInvPolicy              | classoid                                          | int         | int            | NO            |             |
| scAllocateInvPolicy              | description                                       | text        | text           | NO            |             |
| scAllocateInvPolicy              | expiryValidationDate                              | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | forwardpick_id                                    | int         | int            | NO            |             |
| scAllocateInvPolicy              | inventoryPriority                                 | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | mergePKLI                                         | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | name                                              | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | pklilocsetting                                    | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | priority                                          | int         | int            | NO            |             |
| scAllocateInvPolicy              | priorizationMode                                  | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | replenishableZone_id                              | int         | int            | NO            |             |
| scAllocateInvPolicy              | reservationMode                                   | varchar     | varchar(255)   | NO            |             |
| scAllocateInvPolicy              | site_id                                           | int         | int            | NO            |             |
| scAllocateInvPolicy              | siteConfiguration_id                              | int         | int            | NO            |             |
| scAllocateInvPolicy              | unallocationMode                                  | varchar     | varchar(255)   | NO            |             |
| scAllocationJob                  | oid                                               | int         | int            | NO            | Primary Key |
| scAllocationJob                  | site_id                                           | int         | int            | NO            | Foreign Key |
| scAllocationJob                  | classoid                                          | int         | int            | NO            |             |
| scAllocationJob                  | description                                       | text        | text           | NO            |             |
| scAllocationJob                  | name                                              | varchar     | varchar(255)   | NO            |             |
| scAllocationJob                  | showAllocationPlan                                | varchar     | varchar(10)    | NO            |             |
| scAllocationJob                  | siteConfiguration_id                              | int         | int            | NO            |             |
| scAllocationJob                  | status                                            | varchar     | varchar(255)   | NO            |             |
| scAllocationJob                  | type                                              | varchar     | varchar(255)   | NO            |             |
| scAllocationJobFillrate          | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scAllocationJobFillrate          | allocationJob_id                                  | int         | int            | NO            |             |
| scAllocationJobFillrate          | classoid                                          | int         | int            | NO            |             |
| scAllocationJobFillrate          | fillrateType_id                                   | int         | int            | NO            |             |
| scAllocationJobFillrate          | sequence                                          | int         | int            | NO            |             |
| scAssembly                       | oid                                               | int         | int            | NO            | Primary Key |
| scAssembly                       | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scAssembly                       | classoid                                          | int         | int            | NO            |             |
| scAssembly                       | name                                              | varchar     | varchar(255)   | NO            |             |
| scAssembly                       | status                                            | varchar     | varchar(255)   | NO            |             |
| scAssembly                       | uoi_id                                            | int         | int            | NO            |             |
| scBayConfiguration               | oid                                               | int         | int            | NO            | Primary Key |
| scBayConfiguration               | bay_id                                            | int         | int            | NO            |             |
| scBayConfiguration               | classoid                                          | int         | int            | NO            |             |
| scBayConfiguration               | printingWorkCenter_id                             | int         | int            | NO            |             |
| scBayConfiguration               | receivingJob_id                                   | int         | int            | NO            |             |
| scCalendarPeriod_Agropur         | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scCalendarPeriod_Agropur         | calendar_id                                       | int         | int            | NO            | Foreign Key |
| scCalendarPeriod_Agropur         | classoid                                          | int         | int            | NO            |             |
| scCalendarPeriod_Agropur         | endDate                                           | datetime    | datetime       | NO            |             |
| scCalendarPeriod_Agropur         | name                                              | varchar     | varchar(255)   | NO            |             |
| scCalendarPeriod_Agropur         | startDate                                         | datetime    | datetime       | NO            |             |
| scCalendarPeriod_Agropur         | type                                              | varchar     | varchar(255)   | NO            |             |
| scCarrierRelation                | oid                                               | int         | int            | NO            | Primary Key |
| scCarrierRelation                | customer_id                                       | int         | int            | NO            | Foreign Key |
| scCarrierRelation                | bolreport_id                                      | int         | int            | NO            |             |
| scCarrierRelation                | carrier_id                                        | int         | int            | NO            |             |
| scCarrierRelation                | carrierAccountNo                                  | varchar     | varchar(255)   | NO            |             |
| scCarrierRelation                | classoid                                          | int         | int            | NO            |             |
| scCarrierRelation                | masterBOLreport_id                                | int         | int            | NO            |             |
| scCarrierRelation                | serviceLevel_id                                   | int         | int            | NO            |             |
| scCarrierRelation                | shipmentType_id                                   | int         | int            | NO            |             |
| scCheckListInstanceComment       | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scCheckListInstanceComment       | classoid                                          | int         | int            | NO            |             |
| scCheckListInstanceComment       | comment                                           | text        | text           | NO            |             |
| scCheckListInstanceComment       | createStamp                                       | datetime    | datetime       | NO            |             |
| scCheckListInstanceComment       | createUser_id                                     | int         | int            | NO            |             |
| scCheckListInstanceComment       | owner_id                                          | int         | int            | NO            |             |
| scCheckListInstanceComment       | ownerType                                         | varchar     | varchar(255)   | NO            |             |
| scCheckListInstanceComment       | publicComment                                     | varchar     | varchar(10)    | NO            |             |
| scCheckListInstanceComment       | updateStamp                                       | datetime    | datetime       | NO            |             |
| scCheckListInstanceComment       | updateUser_id                                     | int         | int            | NO            |             |
| scChecklistDataType              | oid                                               | int         | int            | NO            | Primary Key |
| scChecklistDataType              | checklistType_id                                  | int         | int            | NO            |             |
| scChecklistDataType              | classoid                                          | int         | int            | NO            |             |
| scChecklistDataType              | column_id                                         | int         | int            | NO            |             |
| scChecklistDataType              | name                                              | varchar     | varchar(255)   | NO            |             |
| scChecklistDataType              | query_id                                          | int         | int            | NO            |             |
| scChecklistDataType              | scriptText                                        | text        | text           | NO            |             |
| scChecklistDataType              | type_id                                           | int         | int            | NO            |             |
| scChecklistDataType              | valueList_id                                      | int         | int            | NO            |             |
| scChecklistInstance              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scChecklistInstance              | checklistMaster_id                                | int         | int            | NO            | Foreign Key |
| scChecklistInstance              | reference_id                                      | int         | int            | NO            | Foreign Key |
| scChecklistInstance              | classoid                                          | int         | int            | NO            |             |
| scChecklistInstance              | createStamp                                       | datetime    | datetime       | NO            |             |
| scChecklistInstance              | createUser_id                                     | int         | int            | NO            |             |
| scChecklistInstance              | locked                                            | varchar     | varchar(10)    | NO            |             |
| scChecklistInstance              | materialMaster_id                                 | int         | int            | NO            |             |
| scChecklistInstance              | owner_id                                          | int         | int            | NO            |             |
| scChecklistInstance              | referenceName                                     | varchar     | varchar(255)   | NO            |             |
| scChecklistInstance              | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scChecklistInstance              | revision_id                                       | int         | int            | NO            |             |
| scChecklistInstance              | site_id                                           | int         | int            | NO            |             |
| scChecklistInstance              | source                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistInstance              | status                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistInstance              | unlockStamp                                       | datetime    | datetime       | NO            |             |
| scChecklistInstance              | unlockUser_id                                     | int         | int            | NO            |             |
| scChecklistInstance              | updateStamp                                       | datetime    | datetime       | NO            |             |
| scChecklistInstance              | updateUser_id                                     | int         | int            | NO            |             |
| scChecklistInstanceSourceDetail  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scChecklistInstanceSourceDetail  | checklistInstance_id                              | int         | int            | NO            | Foreign Key |
| scChecklistInstanceSourceDetail  | classoid                                          | int         | int            | NO            |             |
| scChecklistInstanceSourceDetail  | customer_id                                       | int         | int            | NO            |             |
| scChecklistInstanceSourceDetail  | dimension_id                                      | int         | int            | NO            |             |
| scChecklistInstanceSourceDetail  | materialMaster_id                                 | int         | int            | NO            |             |
| scChecklistInstanceSourceDetail  | source                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistInstanceSourceDetail  | vendor_id                                         | int         | int            | NO            |             |
| scChecklistInstanceStep          | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scChecklistInstanceStep          | checklistInstance_id                              | int         | int            | NO            | Foreign Key |
| scChecklistInstanceStep          | stepMaster_id                                     | int         | int            | NO            | Foreign Key |
| scChecklistInstanceStep          | classoid                                          | int         | int            | NO            |             |
| scChecklistInstanceStep          | lastResult_id                                     | int         | int            | NO            |             |
| scChecklistInstanceStep          | sequence                                          | int         | int            | NO            |             |
| scChecklistInstanceStep          | status                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistMaster                | oid                                               | int         | int            | NO            | Primary Key |
| scChecklistMaster                | activeRevision_id                                 | int         | int            | NO            |             |
| scChecklistMaster                | classoid                                          | int         | int            | NO            |             |
| scChecklistMaster                | description_id                                    | int         | int            | NO            |             |
| scChecklistMaster                | label_id                                          | int         | int            | NO            |             |
| scChecklistMaster                | origin_id                                         | int         | int            | NO            |             |
| scChecklistMaster                | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scChecklistMaster                | revision                                          | varchar     | varchar(255)   | NO            |             |
| scChecklistMaster                | status                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistMaster                | type_id                                           | int         | int            | NO            |             |
| scChecklistMasterAction          | oid                                               | int         | int            | NO            | Primary Key |
| scChecklistMasterAction          | step_id                                           | int         | int            | NO            | Foreign Key |
| scChecklistMasterAction          | classoid                                          | int         | int            | NO            |             |
| scChecklistMasterAction          | description_id                                    | int         | int            | NO            |             |
| scChecklistMasterAction          | instanceStatus                                    | varchar     | varchar(255)   | NO            |             |
| scChecklistMasterAction          | label_id                                          | int         | int            | NO            |             |
| scChecklistMasterAction          | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scChecklistMasterRevision        | oid                                               | int         | int            | NO            | Primary Key |
| scChecklistMasterRevision        | checklistMaster_id                                | int         | int            | NO            | Foreign Key |
| scChecklistMasterRevision        | classoid                                          | int         | int            | NO            |             |
| scChecklistMasterRevision        | origin_id                                         | int         | int            | NO            |             |
| scChecklistMasterRevision        | revision                                          | varchar     | varchar(255)   | NO            |             |
| scChecklistMasterRevision        | status                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistMasterStep            | oid                                               | int         | int            | NO            | Primary Key |
| scChecklistMasterStep            | billingEventType_id                               | int         | int            | NO            |             |
| scChecklistMasterStep            | checklistMaster_id                                | int         | int            | NO            |             |
| scChecklistMasterStep            | classoid                                          | int         | int            | NO            |             |
| scChecklistMasterStep            | description_id                                    | int         | int            | NO            |             |
| scChecklistMasterStep            | expectedResult                                    | varchar     | varchar(255)   | NO            |             |
| scChecklistMasterStep            | label_id                                          | int         | int            | NO            |             |
| scChecklistMasterStep            | origin_id                                         | int         | int            | NO            |             |
| scChecklistMasterStep            | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scChecklistMasterStep            | required                                          | varchar     | varchar(10)    | NO            |             |
| scChecklistMasterStep            | resultType_id                                     | int         | int            | NO            |             |
| scChecklistMasterStep            | sequence                                          | int         | int            | NO            |             |
| scChecklistMasterStep            | status                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistStepResult            | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scChecklistStepResult            | reference_id                                      | int         | int            | NO            | Foreign Key |
| scChecklistStepResult            | step_id                                           | int         | int            | NO            | Foreign Key |
| scChecklistStepResult            | action_id                                         | int         | int            | NO            |             |
| scChecklistStepResult            | classoid                                          | int         | int            | NO            |             |
| scChecklistStepResult            | comment                                           | text        | text           | NO            |             |
| scChecklistStepResult            | completedDate                                     | datetime    | datetime       | NO            |             |
| scChecklistStepResult            | result                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistStepResult            | status                                            | varchar     | varchar(255)   | NO            |             |
| scChecklistStepResult            | user_id                                           | int         | int            | NO            |             |
| scChecklistType                  | oid                                               | int         | int            | NO            | Primary Key |
| scChecklistType                  | classoid                                          | int         | int            | NO            |             |
| scChecklistType                  | mode                                              | varchar     | varchar(255)   | NO            |             |
| scChecklistType                  | name                                              | varchar     | varchar(255)   | NO            |             |
| scChecklistType                  | referenceType_id                                  | int         | int            | NO            |             |
| scChecklistType                  | type                                              | varchar     | varchar(255)   | NO            |             |
| scComment                        | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scComment                        | reference_id                                      | int         | int            | NO            | Foreign Key |
| scComment                        | classoid                                          | int         | int            | NO            |             |
| scComment                        | comment                                           | text        | text           | NO            |             |
| scComment                        | timestamp                                         | datetime    | datetime       | NO            |             |
| scComment                        | type                                              | varchar     | varchar(255)   | NO            |             |
| scComment                        | user_id                                           | int         | int            | NO            |             |
| scConfigurationItem              | oid                                               | int         | int            | NO            | Primary Key |
| scConfigurationItem              | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scConfigurationItem              | classoid                                          | int         | int            | NO            |             |
| scConfigurationItem              | enforcePosition                                   | varchar     | varchar(10)    | NO            |             |
| scConfigurationItem              | name                                              | varchar     | varchar(255)   | NO            |             |
| scConfigurationItem              | parent_id                                         | int         | int            | NO            |             |
| scConfigurationItem              | quantity                                          | int         | int            | NO            |             |
| scConfigurationItem              | sequence                                          | int         | int            | NO            |             |
| scConfigurationItem              | status                                            | varchar     | varchar(255)   | NO            |             |
| scConfigurationItem              | subAssembly_id                                    | int         | int            | NO            |             |
| scConfigurationItem              | uoi_id                                            | int         | int            | NO            |             |
| scConsolidationJob               | oid                                               | int         | int            | NO            | Primary Key |
| scConsolidationJob               | classoid                                          | int         | int            | NO            |             |
| scConsolidationJob               | containerConsolidationMode                        | varchar     | varchar(255)   | NO            |             |
| scConsolidationJob               | description                                       | text        | text           | NO            |             |
| scConsolidationJob               | name                                              | varchar     | varchar(255)   | NO            |             |
| scConsolidationJob               | site_id                                           | int         | int            | NO            |             |
| scConsolidationJob               | siteConfiguration_id                              | int         | int            | NO            |             |
| scConsolidationJob               | status                                            | varchar     | varchar(255)   | NO            |             |
| scContainer                      | oid                                               | int         | int            | NO            | Primary Key |
| scContainer                      | container_id                                      | int         | int            | NO            | Foreign Key |
| scContainer                      | currentLOAD_id                                    | int         | int            | NO            | Foreign Key |
| scContainer                      | currentPKLH_id                                    | int         | int            | NO            | Foreign Key |
| scContainer                      | location_id                                       | int         | int            | NO            | Foreign Key |
| scContainer                      | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scContainer                      | parent_id                                         | int         | int            | NO            | Foreign Key |
| scContainer                      | serialNo                                          | varchar     | varchar(255)   | NO            | Foreign Key |
| scContainer                      | sSCC                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scContainer                      | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scContainer                      | topContainer_id                                   | int         | int            | NO            | Foreign Key |
| scContainer                      | trackingNo                                        | varchar     | varchar(255)   | NO            | Foreign Key |
| scContainer                      | type_id                                           | int         | int            | NO            | Foreign Key |
| scContainer                      | capacity                                          | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | capacityUsed                                      | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | classoid                                          | int         | int            | NO            |             |
| scContainer                      | containerSequence                                 | varchar     | varchar(255)   | NO            |             |
| scContainer                      | currentMOVE_id                                    | int         | int            | NO            |             |
| scContainer                      | currentSHLP_id                                    | int         | int            | NO            |             |
| scContainer                      | currentSOLH_id                                    | int         | int            | NO            |             |
| scContainer                      | depth                                             | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | dimensionUOM_id                                   | int         | int            | NO            |             |
| scContainer                      | height                                            | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | items                                             | int         | int            | NO            |             |
| scContainer                      | loadSequence                                      | int         | int            | NO            |             |
| scContainer                      | manualWeight                                      | varchar     | varchar(10)    | NO            |             |
| scContainer                      | maxWeight                                         | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | mobileEquipment_id                                | int         | int            | NO            |             |
| scContainer                      | partitionNo                                       | int         | int            | NO            |             |
| scContainer                      | physicalSequence                                  | int         | int            | NO            |             |
| scContainer                      | pickCOPosition                                    | varchar     | varchar(255)   | NO            |             |
| scContainer                      | pickedSequence                                    | int         | int            | NO            |             |
| scContainer                      | pickingContainer_id                               | int         | int            | NO            |             |
| scContainer                      | shipmentRequest_id                                | int         | int            | NO            |             |
| scContainer                      | shippingLabelPrinted                              | varchar     | varchar(10)    | NO            |             |
| scContainer                      | shipTo_id                                         | int         | int            | NO            |             |
| scContainer                      | shipToZone_id                                     | int         | int            | NO            |             |
| scContainer                      | site_id                                           | int         | int            | NO            |             |
| scContainer                      | supplier_id                                       | int         | int            | NO            |             |
| scContainer                      | tmsInfo_id                                        | int         | int            | NO            |             |
| scContainer                      | totalValue                                        | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | transportEquipment_id                             | int         | int            | NO            |             |
| scContainer                      | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | weightUOM_id                                      | int         | int            | NO            |             |
| scContainer                      | width                                             | decimal     | decimal(19,2)  | NO            |             |
| scContainer                      | zone_id                                           | int         | int            | NO            |             |
| scCountingJob                    | oid                                               | int         | int            | NO            | Primary Key |
| scCountingJob                    | allowRecountUniqueItemInSameSession               | varchar     | varchar(10)    | NO            |             |
| scCountingJob                    | allowSameCounter                                  | varchar     | varchar(255)   | NO            |             |
| scCountingJob                    | classoid                                          | int         | int            | NO            |             |
| scCountingJob                    | countAllLPOneCount                                | varchar     | varchar(10)    | NO            |             |
| scCountingJob                    | countAllLPOneCountMode                            | varchar     | varchar(255)   | NO            |             |
| scCountingJob                    | countMethod                                       | varchar     | varchar(255)   | NO            |             |
| scCountingJob                    | countMode                                         | varchar     | varchar(255)   | NO            |             |
| scCountingJob                    | countTolerance                                    | varchar     | varchar(255)   | NO            |             |
| scCountingJob                    | description                                       | text        | text           | NO            |             |
| scCountingJob                    | displayItemInfoOnBatchLPNCount                    | varchar     | varchar(10)    | NO            |             |
| scCountingJob                    | inconsistentJob_id                                | int         | int            | NO            |             |
| scCountingJob                    | inconsistentStrategy                              | varchar     | varchar(255)   | NO            |             |
| scCountingJob                    | maxConsecutiveCount                               | varchar     | varchar(255)   | NO            |             |
| scCountingJob                    | maxConsecutiveCountBatch                          | int         | int            | NO            |             |
| scCountingJob                    | name                                              | varchar     | varchar(255)   | NO            |             |
| scCountingJob                    | newItemCondition_id                               | int         | int            | NO            |             |
| scCountingJob                    | newItemOwner_id                                   | int         | int            | NO            |             |
| scCountingJob                    | reason_id                                         | int         | int            | NO            |             |
| scCountingJob                    | recoundNewItem                                    | varchar     | varchar(10)    | NO            |             |
| scCountingJob                    | recountNotCounted                                 | varchar     | varchar(10)    | NO            |             |
| scCountingJob                    | sendToReconcile                                   | varchar     | varchar(10)    | NO            |             |
| scCountingJob                    | serialNumberDiscrepancyAllowed                    | varchar     | varchar(10)    | NO            |             |
| scCountingJob                    | site_id                                           | int         | int            | NO            |             |
| scCountingJob                    | siteConfiguration_id                              | int         | int            | NO            |             |
| scCustomerRelation               | oid                                               | int         | int            | NO            | Primary Key |
| scCustomerRelation               | customer_id                                       | int         | int            | NO            | Foreign Key |
| scCustomerRelation               | supplier_id                                       | int         | int            | NO            | Foreign Key |
| scCustomerRelation               | allocationInvPolicy_id                            | int         | int            | NO            |             |
| scCustomerRelation               | billingCustomer_id                                | int         | int            | NO            |             |
| scCustomerRelation               | billingLocation_id                                | int         | int            | NO            |             |
| scCustomerRelation               | billTo_id                                         | int         | int            | NO            |             |
| scCustomerRelation               | billToAddress_id                                  | int         | int            | NO            |             |
| scCustomerRelation               | billToContact_id                                  | int         | int            | NO            |             |
| scCustomerRelation               | blocked                                           | varchar     | varchar(255)   | NO            |             |
| scCustomerRelation               | checklistInbound                                  | int         | int            | NO            |             |
| scCustomerRelation               | checklistInboundByItem                            | int         | int            | NO            |             |
| scCustomerRelation               | checklistInboundByLOTNO                           | int         | int            | NO            |             |
| scCustomerRelation               | checklistInboundByReceivingDocument               | int         | int            | NO            |             |
| scCustomerRelation               | classoid                                          | int         | int            | NO            |             |
| scCustomerRelation               | customerNo                                        | varchar     | varchar(255)   | NO            |             |
| scCustomerRelation               | defaultSOLIPriority                               | varchar     | varchar(255)   | NO            |             |
| scCustomerRelation               | packingSlip_id                                    | int         | int            | NO            |             |
| scCustomerRelation               | productionReceivingLabel_id                       | int         | int            | NO            |             |
| scCustomerRelation               | productionReceivingLabelQty                       | int         | int            | NO            |             |
| scCustomerRelation               | shipTo_id                                         | int         | int            | NO            |             |
| scCustomerRelation               | shipToAddress_id                                  | int         | int            | NO            |             |
| scCustomerRelation               | shipToContact_id                                  | int         | int            | NO            |             |
| scCustomerRelation               | shipVia_id                                        | int         | int            | NO            |             |
| scCustomerRelation               | shipViaAddress_id                                 | int         | int            | NO            |             |
| scCustomerRelation               | shipViaContact_id                                 | int         | int            | NO            |             |
| scCycleCount                     | oid                                               | int         | int            | NO            | Primary Key |
| scCycleCount                     | calendar_id                                       | int         | int            | NO            |             |
| scCycleCount                     | classoid                                          | int         | int            | NO            |             |
| scCycleCount                     | countedItems                                      | int         | int            | NO            |             |
| scCycleCount                     | countingJob_id                                    | int         | int            | NO            |             |
| scCycleCount                     | countingMode                                      | varchar     | varchar(255)   | NO            |             |
| scCycleCount                     | currentCycle                                      | int         | int            | NO            |             |
| scCycleCount                     | currentLocation_id                                | int         | int            | NO            |             |
| scCycleCount                     | endLocation_id                                    | int         | int            | NO            |             |
| scCycleCount                     | frequency                                         | int         | int            | NO            |             |
| scCycleCount                     | locationType                                      | varchar     | varchar(255)   | NO            |             |
| scCycleCount                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scCycleCount                     | parent_id                                         | int         | int            | NO            |             |
| scCycleCount                     | priority                                          | varchar     | varchar(255)   | NO            |             |
| scCycleCount                     | remainingDays                                     | int         | int            | NO            |             |
| scCycleCount                     | route_id                                          | int         | int            | NO            |             |
| scCycleCount                     | schedule_id                                       | int         | int            | NO            |             |
| scCycleCount                     | scheduledItems                                    | int         | int            | NO            |             |
| scCycleCount                     | site_id                                           | int         | int            | NO            |             |
| scCycleCount                     | startLocation_id                                  | int         | int            | NO            |             |
| scCycleCount                     | status                                            | varchar     | varchar(255)   | NO            |             |
| scCycleCount                     | totalDays                                         | int         | int            | NO            |             |
| scCycleCount                     | totalItems                                        | int         | int            | NO            |             |
| scDeliveryJob                    | oid                                               | int         | int            | NO            | Primary Key |
| scDeliveryJob                    | site_id                                           | int         | int            | NO            | Foreign Key |
| scDeliveryJob                    | classoid                                          | int         | int            | NO            |             |
| scDeliveryJob                    | description                                       | text        | text           | NO            |             |
| scDeliveryJob                    | name                                              | varchar     | varchar(255)   | NO            |             |
| scDeliveryJob                    | siteConfiguration_id                              | int         | int            | NO            |             |
| scDeliveryJob                    | status                                            | varchar     | varchar(255)   | NO            |             |
| scExpiryDateJobLog               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scExpiryDateJobLog               | expiryDateJob_id                                  | int         | int            | NO            | Foreign Key |
| scExpiryDateJobLog               | classoid                                          | int         | int            | NO            |             |
| scExpiryDateJobLog               | description                                       | varchar     | varchar(255)   | NO            |             |
| scExpiryDateJobLog               | endDate                                           | datetime    | datetime       | NO            |             |
| scExpiryDateJobLog               | startDate                                         | datetime    | datetime       | NO            |             |
| scExpiryDateJobLog               | user_id                                           | int         | int            | NO            |             |
| scFillrateType                   | oid                                               | int         | int            | NO            | Primary Key |
| scFillrateType                   | baseType                                          | varchar     | varchar(255)   | NO            |             |
| scFillrateType                   | classoid                                          | int         | int            | NO            |             |
| scFillrateType                   | description                                       | varchar     | varchar(255)   | NO            |             |
| scFillrateType                   | name                                              | varchar     | varchar(255)   | NO            |             |
| scGTIN                           | oid                                               | int         | int            | NO            | Primary Key |
| scGTIN                           | gtin                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scGTIN                           | uoiconfig_id                                      | int         | int            | NO            | Foreign Key |
| scGTIN                           | classoid                                          | int         | int            | NO            |             |
| scGeneratedItem                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scGeneratedItem                  | generation_id                                     | int         | int            | NO            | Foreign Key |
| scGeneratedItem                  | allocatedQty                                      | bigint      | bigint         | NO            |             |
| scGeneratedItem                  | availableQty                                      | bigint      | bigint         | NO            |             |
| scGeneratedItem                  | classoid                                          | int         | int            | NO            |             |
| scGeneratedItem                  | materialMaster_id                                 | int         | int            | NO            |             |
| scGeneratedItem                  | partitionNo                                       | int         | int            | NO            |             |
| scGeneratedItem                  | requestedQty                                      | bigint      | bigint         | NO            |             |
| scGeneratedItem                  | totalQty                                          | bigint      | bigint         | NO            |             |
| scGeneratedItem                  | uoi_id                                            | int         | int            | NO            |             |
| scGeneratedMREQ                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scGeneratedMREQ                  | generatedOrder_id                                 | int         | int            | NO            | Foreign Key |
| scGeneratedMREQ                  | item_id                                           | int         | int            | NO            | Foreign Key |
| scGeneratedMREQ                  | mreq_id                                           | int         | int            | NO            | Foreign Key |
| scGeneratedMREQ                  | allocatedQty                                      | bigint      | bigint         | NO            |             |
| scGeneratedMREQ                  | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scGeneratedMREQ                  | classoid                                          | int         | int            | NO            |             |
| scGeneratedMREQ                  | fillrateType_id                                   | int         | int            | NO            |             |
| scGeneratedMREQ                  | fulfilledValue                                    | decimal     | decimal(19,2)  | NO            |             |
| scGeneratedMREQ                  | locations                                         | mediumtext  | mediumtext     | NO            |             |
| scGeneratedMREQ                  | partitionNo                                       | int         | int            | NO            |             |
| scGeneratedMREQ                  | policy_id                                         | int         | int            | NO            |             |
| scGeneratedMREQ                  | reason                                            | varchar     | varchar(255)   | NO            |             |
| scGeneratedMREQ                  | requiredQty                                       | bigint      | bigint         | NO            |             |
| scGeneratedMREQ                  | sequence                                          | int         | int            | NO            |             |
| scGeneratedMREQ                  | status                                            | varchar     | varchar(255)   | NO            |             |
| scGeneratedMREQ                  | totalValue                                        | decimal     | decimal(19,2)  | NO            |             |
| scGeneratedMREQ                  | uoi_id                                            | int         | int            | NO            |             |
| scGeneratedOrder                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scGeneratedOrder                 | generation_id                                     | int         | int            | NO            | Foreign Key |
| scGeneratedOrder                 | shipmentRequest_id                                | int         | int            | NO            | Foreign Key |
| scGeneratedOrder                 | solh_id                                           | int         | int            | NO            | Foreign Key |
| scGeneratedOrder                 | classoid                                          | int         | int            | NO            |             |
| scGeneratedOrder                 | fillrateType_id                                   | int         | int            | NO            |             |
| scGeneratedOrder                 | fulfilledValue                                    | decimal     | decimal(19,2)  | NO            |             |
| scGeneratedOrder                 | partitionNo                                       | int         | int            | NO            |             |
| scGeneratedOrder                 | reason                                            | varchar     | varchar(255)   | NO            |             |
| scGeneratedOrder                 | status                                            | varchar     | varchar(255)   | NO            |             |
| scGeneratedOrder                 | totalValue                                        | decimal     | decimal(19,2)  | NO            |             |
| scGeneration                     | oid                                               | int         | int            | NO            | Primary Key |
| scGeneration                     | generationTime                                    | datetime    | datetime       | NO            | Foreign Key |
| scGeneration                     | allocatedLines                                    | int         | int            | NO            |             |
| scGeneration                     | allocationJob_id                                  | int         | int            | NO            |             |
| scGeneration                     | assemblyMode                                      | varchar     | varchar(255)   | NO            |             |
| scGeneration                     | cancelledLines                                    | int         | int            | NO            |             |
| scGeneration                     | classoid                                          | int         | int            | NO            |             |
| scGeneration                     | completedTime                                     | datetime    | datetime       | NO            |             |
| scGeneration                     | executionTime                                     | int         | int            | NO            |             |
| scGeneration                     | ignoredLines                                      | int         | int            | NO            |             |
| scGeneration                     | message                                           | text        | text           | NO            |             |
| scGeneration                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scGeneration                     | partiallyAllocatedLines                           | int         | int            | NO            |             |
| scGeneration                     | partitionNo                                       | int         | int            | NO            |             |
| scGeneration                     | policy_id                                         | int         | int            | NO            |             |
| scGeneration                     | preposition_id                                    | int         | int            | NO            |             |
| scGeneration                     | prepositionZone_id                                | int         | int            | NO            |             |
| scGeneration                     | requestedTime                                     | datetime    | datetime       | NO            |             |
| scGeneration                     | simulation                                        | varchar     | varchar(10)    | NO            |             |
| scGeneration                     | site_id                                           | int         | int            | NO            |             |
| scGeneration                     | status                                            | varchar     | varchar(255)   | NO            |             |
| scGeneration                     | totalItems                                        | int         | int            | NO            |             |
| scGeneration                     | totalLines                                        | int         | int            | NO            |             |
| scGeneration                     | type                                              | varchar     | varchar(255)   | NO            |             |
| scGeneration                     | user_id                                           | int         | int            | NO            |             |
| scGeneration                     | wave_id                                           | int         | int            | NO            |             |
| scHandlingMaterialOrderContainer | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scHandlingMaterialOrderContainer | container_id                                      | int         | int            | NO            | Foreign Key |
| scHandlingMaterialOrderContainer | solh_id                                           | int         | int            | NO            | Foreign Key |
| scHandlingMaterialOrderContainer | classoid                                          | int         | int            | NO            |             |
| scHandlingMaterialOrderContainer | handlingMaterial_id                               | int         | int            | NO            |             |
| scHandlingMaterialOrderContainer | quantity                                          | bigint      | bigint         | NO            |             |
| scHandlingMaterialOrderContainer | uoi_id                                            | int         | int            | NO            |             |
| scInternalRoute                  | oid                                               | int         | int            | NO            | Primary Key |
| scInternalRoute                  | aislepattern                                      | varchar     | varchar(255)   | NO            |             |
| scInternalRoute                  | classoid                                          | int         | int            | NO            |             |
| scInternalRoute                  | description                                       | varchar     | varchar(255)   | NO            |             |
| scInternalRoute                  | levelpattern                                      | varchar     | varchar(255)   | NO            |             |
| scInternalRoute                  | name                                              | varchar     | varchar(255)   | NO            |             |
| scInternalRoute                  | rackpattern                                       | varchar     | varchar(255)   | NO            |             |
| scInternalRoute                  | siteoid                                           | int         | int            | NO            |             |
| scInternalRoute                  | zoneoid                                           | int         | int            | NO            |             |
| scInvAdjustmentReason            | oid                                               | int         | int            | NO            | Primary Key |
| scInvAdjustmentReason            | classoid                                          | int         | int            | NO            |             |
| scInvAdjustmentReason            | condition_id                                      | int         | int            | NO            |             |
| scInvAdjustmentReason            | costcenter_id                                     | int         | int            | NO            |             |
| scInvAdjustmentReason            | description_id                                    | int         | int            | NO            |             |
| scInvAdjustmentReason            | glAccount_id                                      | int         | int            | NO            |             |
| scInvAdjustmentReason            | hostValue                                         | varchar     | varchar(255)   | NO            |             |
| scInvAdjustmentReason            | label_id                                          | int         | int            | NO            |             |
| scInvAdjustmentReason            | name                                              | varchar     | varchar(255)   | NO            |             |
| scInventoryCountSession          | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scInventoryCountSession          | abcClass_id                                       | int         | int            | NO            |             |
| scInventoryCountSession          | activeCount                                       | int         | int            | NO            |             |
| scInventoryCountSession          | aisle_id                                          | int         | int            | NO            |             |
| scInventoryCountSession          | cancelledCount                                    | int         | int            | NO            |             |
| scInventoryCountSession          | classoid                                          | int         | int            | NO            |             |
| scInventoryCountSession          | comment                                           | text        | text           | NO            |             |
| scInventoryCountSession          | completedCount                                    | int         | int            | NO            |             |
| scInventoryCountSession          | completedDate                                     | datetime    | datetime       | NO            |             |
| scInventoryCountSession          | countingJob_id                                    | int         | int            | NO            |             |
| scInventoryCountSession          | countingMode                                      | varchar     | varchar(255)   | NO            |             |
| scInventoryCountSession          | creationDate                                      | datetime    | datetime       | NO            |             |
| scInventoryCountSession          | cycleCount_id                                     | int         | int            | NO            |             |
| scInventoryCountSession          | location_id                                       | int         | int            | NO            |             |
| scInventoryCountSession          | locationItemCount_id                              | int         | int            | NO            |             |
| scInventoryCountSession          | locationType                                      | varchar     | varchar(255)   | NO            |             |
| scInventoryCountSession          | materialMaster_id                                 | int         | int            | NO            |             |
| scInventoryCountSession          | name                                              | varchar     | varchar(255)   | NO            |             |
| scInventoryCountSession          | owner_id                                          | int         | int            | NO            |             |
| scInventoryCountSession          | pkli_id                                           | int         | int            | NO            |             |
| scInventoryCountSession          | priority                                          | int         | int            | NO            |             |
| scInventoryCountSession          | productClass_id                                   | int         | int            | NO            |             |
| scInventoryCountSession          | requiredDate                                      | datetime    | datetime       | NO            |             |
| scInventoryCountSession          | site_id                                           | int         | int            | NO            |             |
| scInventoryCountSession          | status                                            | varchar     | varchar(255)   | NO            |             |
| scInventoryCountSession          | totalCount                                        | int         | int            | NO            |             |
| scInventoryCountSession          | type                                              | varchar     | varchar(255)   | NO            |             |
| scInventoryCountSession          | user_id                                           | int         | int            | NO            |             |
| scInventoryCountSession          | zone_id                                           | int         | int            | NO            |             |
| scInventoryLocation              | oid                                               | int         | int            | NO            | Primary Key |
| scInventoryLocation              | aisle_id                                          | int         | int            | NO            | Foreign Key |
| scInventoryLocation              | level_id                                          | int         | int            | NO            | Foreign Key |
| scInventoryLocation              | materialAssignment                                | varchar     | varchar(255)   | NO            | Foreign Key |
| scInventoryLocation              | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scInventoryLocation              | rack_id                                           | int         | int            | NO            | Foreign Key |
| scInventoryLocation              | site_id                                           | int         | int            | NO            | Foreign Key |
| scInventoryLocation              | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scInventoryLocation              | type_id                                           | int         | int            | NO            | Foreign Key |
| scInventoryLocation              | zone_id                                           | int         | int            | NO            | Foreign Key |
| scInventoryLocation              | allocateInventory                                 | varchar     | varchar(10)    | NO            |             |
| scInventoryLocation              | checkDigit                                        | varchar     | varchar(255)   | NO            |             |
| scInventoryLocation              | classoid                                          | int         | int            | NO            |             |
| scInventoryLocation              | createStamp                                       | datetime    | datetime       | NO            |             |
| scInventoryLocation              | createUser_id                                     | int         | int            | NO            |             |
| scInventoryLocation              | enableAgingReport                                 | varchar     | varchar(10)    | NO            |             |
| scInventoryLocation              | lastLocation_id                                   | int         | int            | NO            |             |
| scInventoryLocation              | lastMovement_id                                   | int         | int            | NO            |             |
| scInventoryLocation              | lightId                                           | varchar     | varchar(255)   | NO            |             |
| scInventoryLocation              | nbLPInTheLocation                                 | int         | int            | NO            |             |
| scInventoryLocation              | nextLocation_id                                   | int         | int            | NO            |             |
| scInventoryLocation              | position                                          | varchar     | varchar(255)   | NO            |             |
| scInventoryLocation              | sequence                                          | int         | int            | NO            |             |
| scInventoryLocation              | TrackingMode                                      | varchar     | varchar(255)   | NO            |             |
| scInventoryLocation              | updateStamp                                       | datetime    | datetime       | NO            |             |
| scInventoryLocation              | updateUser_id                                     | int         | int            | NO            |             |
| scInventoryLocation              | user_id                                           | int         | int            | NO            |             |
| scInventoryLocation              | velocity                                          | varchar     | varchar(255)   | NO            |             |
| scInventoryLocationType          | oid                                               | int         | int            | NO            | Primary Key |
| scInventoryLocationType          | type                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scInventoryLocationType          | agropurRestrictStagingBay                         | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | agropurStagingBay                                 | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | askReasonCode                                     | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | assignmentType                                    | varchar     | varchar(255)   | NO            |             |
| scInventoryLocationType          | baseMaxVolume                                     | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | baseMaxWeight                                     | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | capacity                                          | varchar     | varchar(255)   | NO            |             |
| scInventoryLocationType          | classoid                                          | int         | int            | NO            |             |
| scInventoryLocationType          | description                                       | text        | text           | NO            |             |
| scInventoryLocationType          | dimensionUOM_id                                   | int         | int            | NO            |             |
| scInventoryLocationType          | dropAction                                        | varchar     | varchar(255)   | NO            |             |
| scInventoryLocationType          | dropBay                                           | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | exteriorDepth                                     | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | exteriorHeight                                    | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | exteriorWidth                                     | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | forwardPickBay                                    | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | interiorDepth                                     | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | interiorHeight                                    | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | interiorWidth                                     | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | maxNumberOfLP                                     | int         | int            | NO            |             |
| scInventoryLocationType          | maxVolume                                         | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | maxWeight                                         | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | name                                              | varchar     | varchar(255)   | NO            |             |
| scInventoryLocationType          | period                                            | decimal     | decimal(19,2)  | NO            |             |
| scInventoryLocationType          | productionBay                                     | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | qaBay                                             | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | receivingBay                                      | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | shippingBay                                       | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | stagingBay                                        | varchar     | varchar(10)    | NO            |             |
| scInventoryLocationType          | status                                            | varchar     | varchar(255)   | NO            |             |
| scInventoryLocationType          | weightUOM_id                                      | int         | int            | NO            |             |
| scInventorySnapshot              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scInventorySnapshot              | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scInventorySnapshot              | parent_id                                         | int         | int            | NO            | Foreign Key |
| scInventorySnapshot              | session_id                                        | int         | int            | NO            | Foreign Key |
| scInventorySnapshot              | classoid                                          | int         | int            | NO            |             |
| scInventorySnapshot              | condition_id                                      | int         | int            | NO            |             |
| scInventorySnapshot              | consumedQty                                       | bigint      | bigint         | NO            |             |
| scInventorySnapshot              | costCenter_id                                     | int         | int            | NO            |             |
| scInventorySnapshot              | location_id                                       | int         | int            | NO            |             |
| scInventorySnapshot              | lotNo_id                                          | int         | int            | NO            |             |
| scInventorySnapshot              | outputtedQty                                      | bigint      | bigint         | NO            |             |
| scInventorySnapshot              | owner_id                                          | int         | int            | NO            |             |
| scInventorySnapshot              | pickedQty                                         | bigint      | bigint         | NO            |             |
| scInventorySnapshot              | processedQty                                      | bigint      | bigint         | NO            |             |
| scInventorySnapshot              | quantity                                          | bigint      | bigint         | NO            |             |
| scInventorySnapshot              | receivedQty                                       | bigint      | bigint         | NO            |             |
| scInventorySnapshot              | sequenceLevel                                     | varchar     | varchar(255)   | NO            |             |
| scInventorySnapshot              | serialNo_id                                       | int         | int            | NO            |             |
| scInventorySnapshot              | snapshotLevel                                     | varchar     | varchar(255)   | NO            |             |
| scInventorySnapshot              | uoi_id                                            | int         | int            | NO            |             |
| scInventorySnapshot              | zone_id                                           | int         | int            | NO            |             |
| scJobConstraint                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scJobConstraint                  | job_id                                            | int         | int            | NO            | Foreign Key |
| scJobConstraint                  | classoid                                          | int         | int            | NO            |             |
| scJobConstraint                  | maxValue                                          | decimal     | decimal(19,2)  | NO            |             |
| scJobConstraint                  | sequence                                          | int         | int            | NO            |             |
| scJobConstraint                  | type                                              | varchar     | varchar(255)   | NO            |             |
| scJobDestination                 | oid                                               | int         | int            | NO            | Primary Key |
| scJobDestination                 | job_id                                            | int         | int            | NO            | Foreign Key |
| scJobDestination                 | classoid                                          | int         | int            | NO            |             |
| scJobDestination                 | location_id                                       | int         | int            | NO            |             |
| scJobDestination                 | site_id                                           | int         | int            | NO            |             |
| scJobDestination                 | type                                              | varchar     | varchar(255)   | NO            |             |
| scJobDestination                 | zone_id                                           | int         | int            | NO            |             |
| scJobSplitter                    | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scJobSplitter                    | job_id                                            | int         | int            | NO            | Foreign Key |
| scJobSplitter                    | classoid                                          | int         | int            | NO            |             |
| scJobSplitter                    | sequence                                          | int         | int            | NO            |             |
| scJobSplitter                    | type                                              | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | oid                                               | int         | int            | NO            | Primary Key |
| scJobZone                        | job_id                                            | int         | int            | NO            | Foreign Key |
| scJobZone                        | allocationMode                                    | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | breakUOI                                          | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | classoid                                          | int         | int            | NO            |             |
| scJobZone                        | disableFutureReplenishments                       | varchar     | varchar(10)    | NO            |             |
| scJobZone                        | forceAllocateConfiguredUOI                        | varchar     | varchar(10)    | NO            |             |
| scJobZone                        | forwardPick_id                                    | int         | int            | NO            |             |
| scJobZone                        | locationPriorizationMode                          | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | maxPickPercentage                                 | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | minReplenishmentPercentage                        | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | name                                              | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | overCapacityMode                                  | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | pickPredecessor_id                                | int         | int            | NO            |             |
| scJobZone                        | priority                                          | int         | int            | NO            |             |
| scJobZone                        | replenishmentJob_id                               | int         | int            | NO            |             |
| scJobZone                        | replenishmentMode                                 | varchar     | varchar(255)   | NO            |             |
| scJobZone                        | route_id                                          | int         | int            | NO            |             |
| scJobZone                        | validateCapacity                                  | varchar     | varchar(10)    | NO            |             |
| scJobZone                        | zone_id                                           | int         | int            | NO            |             |
| scLOAD                           | oid                                               | int         | int            | NO            | Primary Key |
| scLOAD                           | location_id                                       | int         | int            | NO            | Foreign Key |
| scLOAD                           | plannedDoor_id                                    | int         | int            | NO            | Foreign Key |
| scLOAD                           | site_id                                           | int         | int            | NO            | Foreign Key |
| scLOAD                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scLOAD                           | capacity                                          | decimal     | decimal(19,2)  | NO            |             |
| scLOAD                           | capacityUsed                                      | decimal     | decimal(19,2)  | NO            |             |
| scLOAD                           | classoid                                          | int         | int            | NO            |             |
| scLOAD                           | createStamp                                       | datetime    | datetime       | NO            |             |
| scLOAD                           | createUser_id                                     | int         | int            | NO            |             |
| scLOAD                           | deliveryDate                                      | datetime    | datetime       | NO            |             |
| scLOAD                           | description                                       | varchar     | varchar(255)   | NO            |             |
| scLOAD                           | dimensionUOM_id                                   | int         | int            | NO            |             |
| scLOAD                           | displayOnTV                                       | varchar     | varchar(10)    | NO            |             |
| scLOAD                           | equipment_id                                      | int         | int            | NO            |             |
| scLOAD                           | isAgropur_Staged                                  | varchar     | varchar(10)    | NO            |             |
| scLOAD                           | lifeCycle                                         | varchar     | varchar(255)   | NO            |             |
| scLOAD                           | loadingJob_id                                     | int         | int            | NO            |             |
| scLOAD                           | maxWeight                                         | decimal     | decimal(19,2)  | NO            |             |
| scLOAD                           | plannedArrival                                    | datetime    | datetime       | NO            |             |
| scLOAD                           | plannedDeparture                                  | datetime    | datetime       | NO            |             |
| scLOAD                           | priority                                          | varchar     | varchar(255)   | NO            |             |
| scLOAD                           | proBill                                           | varchar     | varchar(255)   | NO            |             |
| scLOAD                           | queue_id                                          | int         | int            | NO            |             |
| scLOAD                           | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scLOAD                           | requiredDate                                      | datetime    | datetime       | NO            |             |
| scLOAD                           | route_id                                          | int         | int            | NO            |             |
| scLOAD                           | routeName                                         | varchar     | varchar(255)   | NO            |             |
| scLOAD                           | seal                                              | varchar     | varchar(255)   | NO            |             |
| scLOAD                           | sendShipmentDetailToOracle                        | varchar     | varchar(10)    | NO            |             |
| scLOAD                           | shippedDate                                       | datetime    | datetime       | NO            |             |
| scLOAD                           | type_id                                           | int         | int            | NO            |             |
| scLOAD                           | updateStamp                                       | datetime    | datetime       | NO            |             |
| scLOAD                           | updateUser_id                                     | int         | int            | NO            |             |
| scLOAD                           | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scLOAD                           | weightUOM_id                                      | int         | int            | NO            |             |
| scLevel                          | oid                                               | int         | int            | NO            | Primary Key |
| scLevel                          | aisle_id                                          | int         | int            | NO            | Foreign Key |
| scLevel                          | rack_id                                           | int         | int            | NO            | Foreign Key |
| scLevel                          | allocateInventory                                 | varchar     | varchar(10)    | NO            |             |
| scLevel                          | classoid                                          | int         | int            | NO            |             |
| scLevel                          | lightId                                           | varchar     | varchar(255)   | NO            |             |
| scLevel                          | name                                              | varchar     | varchar(255)   | NO            |             |
| scLevel                          | site_id                                           | int         | int            | NO            |             |
| scLevel                          | status                                            | varchar     | varchar(255)   | NO            |             |
| scLevel                          | velocity                                          | varchar     | varchar(255)   | NO            |             |
| scLineAdjustment                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scLineAdjustment                 | line_id                                           | int         | int            | NO            | Foreign Key |
| scLineAdjustment                 | parent_id                                         | int         | int            | NO            | Foreign Key |
| scLineAdjustment                 | reference_id                                      | int         | int            | NO            | Foreign Key |
| scLineAdjustment                 | allocatedQty                                      | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | classoid                                          | int         | int            | NO            |             |
| scLineAdjustment                 | consumedQty                                       | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | loadedQty                                         | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | outstandingQty                                    | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | packedQty                                         | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | partitionNo                                       | int         | int            | NO            |             |
| scLineAdjustment                 | pickedQty                                         | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | prepositionQty                                    | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | quantity                                          | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | receivedQty                                       | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | releasedQty                                       | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | shippedQty                                        | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | stagedQty                                         | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | status                                            | varchar     | varchar(255)   | NO            |             |
| scLineAdjustment                 | toReceiveQty                                      | bigint      | bigint         | NO            |             |
| scLineAdjustment                 | uoi_id                                            | int         | int            | NO            |             |
| scLoadType                       | oid                                               | int         | int            | NO            | Primary Key |
| scLoadType                       | canBeLockedByChecklist                            | varchar     | varchar(255)   | NO            |             |
| scLoadType                       | capacity                                          | decimal     | decimal(19,2)  | NO            |             |
| scLoadType                       | classoid                                          | int         | int            | NO            |             |
| scLoadType                       | creationMode                                      | varchar     | varchar(255)   | NO            |             |
| scLoadType                       | depth                                             | decimal     | decimal(19,2)  | NO            |             |
| scLoadType                       | description                                       | text        | text           | NO            |             |
| scLoadType                       | dimensionUOM_id                                   | int         | int            | NO            |             |
| scLoadType                       | forceSealNoInput                                  | varchar     | varchar(255)   | NO            |             |
| scLoadType                       | height                                            | decimal     | decimal(19,2)  | NO            |             |
| scLoadType                       | inboundChecklist_id                               | int         | int            | NO            |             |
| scLoadType                       | initialStatus                                     | varchar     | varchar(255)   | NO            |             |
| scLoadType                       | loadingSequenceOrderAlgorithm                     | varchar     | varchar(255)   | NO            |             |
| scLoadType                       | loadingSequenceOrderMode                          | varchar     | varchar(255)   | NO            |             |
| scLoadType                       | maxWeight                                         | decimal     | decimal(19,2)  | NO            |             |
| scLoadType                       | name                                              | varchar     | varchar(255)   | NO            |             |
| scLoadType                       | preLoadingChecklist_id                            | int         | int            | NO            |             |
| scLoadType                       | shipmentType_id                                   | int         | int            | NO            |             |
| scLoadType                       | weightUOM_id                                      | int         | int            | NO            |             |
| scLoadType                       | width                                             | decimal     | decimal(19,2)  | NO            |             |
| scLoadingJob                     | oid                                               | int         | int            | NO            | Primary Key |
| scLoadingJob                     | site_id                                           | int         | int            | NO            | Foreign Key |
| scLoadingJob                     | allowContainerLoadingOnToLoadList                 | varchar     | varchar(10)    | NO            |             |
| scLoadingJob                     | allowMultipleItemLoading                          | varchar     | varchar(10)    | NO            |             |
| scLoadingJob                     | askEquipmentOperating                             | varchar     | varchar(10)    | NO            |             |
| scLoadingJob                     | canBeLockedByChecklist                            | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | classoid                                          | int         | int            | NO            |             |
| scLoadingJob                     | description                                       | text        | text           | NO            |             |
| scLoadingJob                     | forceSealNoInput                                  | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | itemCapacityDefault                               | int         | int            | NO            |             |
| scLoadingJob                     | itemCapacityReachMode                             | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | itemCapacityStartMoveNotReachMode                 | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | itemVerificationThreshold                         | int         | int            | NO            |             |
| scLoadingJob                     | loadingSequenceOrderAlgorithm                     | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | loadingSequenceOrderMode                          | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | preLoadingChecklist_id                            | int         | int            | NO            |             |
| scLoadingJob                     | restrictionMode                                   | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | shipmentRestriction                               | varchar     | varchar(255)   | NO            |             |
| scLoadingJob                     | showOnlyAssigned                                  | varchar     | varchar(10)    | NO            |             |
| scLoadingJob                     | siteConfiguration_id                              | int         | int            | NO            |             |
| scLoadingJob                     | status                                            | varchar     | varchar(255)   | NO            |             |
| scLocationRoute                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scLocationRoute                  | location_id                                       | int         | int            | NO            | Foreign Key |
| scLocationRoute                  | route_id                                          | int         | int            | NO            | Foreign Key |
| scLocationRoute                  | classoid                                          | int         | int            | NO            |             |
| scLocationRoute                  | sequence                                          | int         | int            | NO            |             |
| scMIAdjustment                   | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMIAdjustment                   | eventDate                                         | datetime    | datetime       | NO            | Foreign Key |
| scMIAdjustment                   | location_id                                       | int         | int            | NO            | Foreign Key |
| scMIAdjustment                   | material_id                                       | int         | int            | NO            | Foreign Key |
| scMIAdjustment                   | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scMIAdjustment                   | movement_id                                       | int         | int            | NO            | Foreign Key |
| scMIAdjustment                   | type                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scMIAdjustment                   | adjustedQty                                       | bigint      | bigint         | NO            |             |
| scMIAdjustment                   | adjustedWeight                                    | decimal     | decimal(19,2)  | NO            |             |
| scMIAdjustment                   | classoid                                          | int         | int            | NO            |             |
| scMIAdjustment                   | condition_id                                      | int         | int            | NO            |             |
| scMIAdjustment                   | costCenter_id                                     | int         | int            | NO            |             |
| scMIAdjustment                   | externalOID                                       | varchar     | varchar(255)   | NO            |             |
| scMIAdjustment                   | owner_id                                          | int         | int            | NO            |             |
| scMIAdjustment                   | partitionNo                                       | int         | int            | NO            |             |
| scMIAdjustment                   | reason_id                                         | int         | int            | NO            |             |
| scMIAdjustment                   | reference_id                                      | int         | int            | NO            |             |
| scMIAdjustment                   | site_id                                           | int         | int            | NO            |             |
| scMIAdjustment                   | stampDate                                         | datetime    | datetime       | NO            |             |
| scMIAdjustment                   | status                                            | varchar     | varchar(255)   | NO            |             |
| scMIAdjustment                   | totalQty                                          | bigint      | bigint         | NO            |             |
| scMIAdjustment                   | totalWeight                                       | decimal     | decimal(19,2)  | NO            |             |
| scMIAdjustment                   | uoi_id                                            | int         | int            | NO            |             |
| scMIAdjustment                   | user_id                                           | int         | int            | NO            |             |
| scMIAdjustment                   | weightUOM_id                                      | int         | int            | NO            |             |
| scMIAdjustment                   | zone_id                                           | int         | int            | NO            |             |
| scMIAdjustmentDimension          | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMIAdjustmentDimension          | adjustment_id                                     | int         | int            | NO            | Foreign Key |
| scMIAdjustmentDimension          | dimension_id                                      | int         | int            | NO            | Foreign Key |
| scMIAdjustmentDimension          | classoid                                          | int         | int            | NO            |             |
| scMIAdjustmentDimension          | partitionNo                                       | int         | int            | NO            |             |
| scMIAdjustmentDimension          | quantity                                          | bigint      | bigint         | NO            |             |
| scMIAdjustmentDimension          | uoi_id                                            | int         | int            | NO            |             |
| scMIAdjustmentDimension          | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMIAdjustmentDimension          | weightUOM_id                                      | int         | int            | NO            |             |
| scMICondition                    | oid                                               | int         | int            | NO            | Primary Key |
| scMICondition                    | baseCondition                                     | varchar     | varchar(255)   | NO            |             |
| scMICondition                    | classoid                                          | int         | int            | NO            |             |
| scMICondition                    | description_id                                    | int         | int            | NO            |             |
| scMICondition                    | label_id                                          | int         | int            | NO            |             |
| scMICondition                    | name                                              | varchar     | varchar(255)   | NO            |             |
| scMIDimension                    | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMIDimension                    | dimension_id                                      | int         | int            | NO            | Foreign Key |
| scMIDimension                    | material_id                                       | int         | int            | NO            | Foreign Key |
| scMIDimension                    | classoid                                          | int         | int            | NO            |             |
| scMIDimension                    | dimensionUOM_id                                   | int         | int            | NO            |             |
| scMIDimension                    | partitionNo                                       | int         | int            | NO            |             |
| scMIDimension                    | quantity                                          | bigint      | bigint         | NO            |             |
| scMIDimension                    | soliDimension_id                                  | int         | int            | NO            |             |
| scMIDimension                    | status                                            | varchar     | varchar(255)   | NO            |             |
| scMIDimension                    | uoi_id                                            | int         | int            | NO            |             |
| scMIDimension                    | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scMIDimension                    | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMIDimension                    | weightUOM_id                                      | int         | int            | NO            |             |
| scMIDimension                    | wosDimension_id                                   | int         | int            | NO            |             |
| scMIHistory                      | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMIHistory                      | material_id                                       | int         | int            | NO            | Foreign Key |
| scMIHistory                      | pkli_id                                           | int         | int            | NO            | Foreign Key |
| scMIHistory                      | shli_id                                           | int         | int            | NO            | Foreign Key |
| scMIHistory                      | wos_id                                            | int         | int            | NO            | Foreign Key |
| scMIHistory                      | activeDate                                        | datetime    | datetime       | NO            |             |
| scMIHistory                      | classoid                                          | int         | int            | NO            |             |
| scMIHistory                      | inactiveDate                                      | datetime    | datetime       | NO            |             |
| scMIHistory                      | load_id                                           | int         | int            | NO            |             |
| scMIHistory                      | partitionNo                                       | int         | int            | NO            |             |
| scMIHistory                      | previous_id                                       | int         | int            | NO            |             |
| scMIHistory                      | rcli_id                                           | int         | int            | NO            |             |
| scMIHistory                      | site_id                                           | int         | int            | NO            |             |
| scMIHistory                      | status                                            | varchar     | varchar(255)   | NO            |             |
| scMMABCCycleCount                | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMMABCCycleCount                | cycleCount_id                                     | int         | int            | NO            | Foreign Key |
| scMMABCCycleCount                | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scMMABCCycleCount                | cancelledLocations                                | int         | int            | NO            |             |
| scMMABCCycleCount                | classoid                                          | int         | int            | NO            |             |
| scMMABCCycleCount                | countedLocations                                  | int         | int            | NO            |             |
| scMMABCCycleCount                | createdCycle                                      | int         | int            | NO            |             |
| scMMABCCycleCount                | createdDate                                       | datetime    | datetime       | NO            |             |
| scMMABCCycleCount                | itemCount                                         | int         | int            | NO            |             |
| scMMABCCycleCount                | lastCountedDate                                   | datetime    | datetime       | NO            |             |
| scMMABCCycleCount                | lastCycle                                         | int         | int            | NO            |             |
| scMMABCCycleCount                | lastSession_id                                    | int         | int            | NO            |             |
| scMMABCCycleCount                | remainingCount                                    | int         | int            | NO            |             |
| scMMABCCycleCount                | scheduledLocations                                | int         | int            | NO            |             |
| scMMCustAttribute                | oid                                               | int         | int            | NO            | Primary Key |
| scMMCustAttribute                | relation_id                                       | int         | int            | NO            | Foreign Key |
| scMMCustAttribute                | checklistInboundByItem                            | int         | int            | NO            |             |
| scMMCustAttribute                | checklistInboundByLOTNO                           | int         | int            | NO            |             |
| scMMCustAttribute                | classoid                                          | int         | int            | NO            |             |
| scMMCustAttribute                | customerName                                      | varchar     | varchar(255)   | NO            |             |
| scMMCustAttribute                | customerPartNo                                    | varchar     | varchar(255)   | NO            |             |
| scMMCustAttribute                | expiryDateTolerance                               | varchar     | varchar(255)   | NO            |             |
| scMMCustAttribute                | expiryDateToleranceMode                           | varchar     | varchar(255)   | NO            |             |
| scMMCustAttribute                | matmaster_id                                      | int         | int            | NO            |             |
| scMMCustAttribute                | maxqty                                            | int         | int            | NO            |             |
| scMMCustAttribute                | minqty                                            | int         | int            | NO            |             |
| scMMDimension                    | oid                                               | int         | int            | NO            | Primary Key |
| scMMDimension                    | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scMMDimension                    | value                                             | varchar     | varchar(255)   | NO            | Foreign Key |
| scMMDimension                    | classoid                                          | int         | int            | NO            |             |
| scMMDimension                    | country_id                                        | int         | int            | NO            |             |
| scMMDimension                    | expiryDate                                        | datetime    | datetime       | NO            |             |
| scMMDimension                    | lotNumber_id                                      | int         | int            | NO            |             |
| scMMDimension                    | manufacturer_id                                   | int         | int            | NO            |             |
| scMMDimension                    | productionDate                                    | datetime    | datetime       | NO            |             |
| scMMDimension                    | reference_id                                      | int         | int            | NO            |             |
| scMMDimension                    | status                                            | varchar     | varchar(255)   | NO            |             |
| scMMDimension                    | type                                              | varchar     | varchar(255)   | NO            |             |
| scMMDimension                    | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMMDimension                    | weightUOM_id                                      | int         | int            | NO            |             |
| scMMDimensionLocation            | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMMDimensionLocation            | mmDimension_id                                    | int         | int            | NO            | Foreign Key |
| scMMDimensionLocation            | mmLocation_id                                     | int         | int            | NO            | Foreign Key |
| scMMDimensionLocation            | classoid                                          | int         | int            | NO            |             |
| scMMDimensionLocation            | dimensionUOM_id                                   | int         | int            | NO            |             |
| scMMDimensionLocation            | quantity                                          | bigint      | bigint         | NO            |             |
| scMMDimensionLocation            | uoi_id                                            | int         | int            | NO            |             |
| scMMDimensionLocation            | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scMMDimensionLocation            | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMMDimensionLocation            | weightUOM_id                                      | int         | int            | NO            |             |
| scMMLocation                     | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMMLocation                     | location_id                                       | int         | int            | NO            | Foreign Key |
| scMMLocation                     | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scMMLocation                     | abcClass_id                                       | int         | int            | NO            |             |
| scMMLocation                     | baseVolume                                        | decimal     | decimal(19,2)  | NO            |             |
| scMMLocation                     | baseWeight                                        | decimal     | decimal(19,2)  | NO            |             |
| scMMLocation                     | classoid                                          | int         | int            | NO            |             |
| scMMLocation                     | condition_id                                      | int         | int            | NO            |             |
| scMMLocation                     | dimensionUOM_id                                   | int         | int            | NO            |             |
| scMMLocation                     | displayPartNo                                     | varchar     | varchar(255)   | NO            |             |
| scMMLocation                     | maximumQty                                        | bigint      | bigint         | NO            |             |
| scMMLocation                     | owner_id                                          | int         | int            | NO            |             |
| scMMLocation                     | pickedQty                                         | bigint      | bigint         | NO            |             |
| scMMLocation                     | quantity                                          | bigint      | bigint         | NO            |             |
| scMMLocation                     | replenishmentQty                                  | bigint      | bigint         | NO            |             |
| scMMLocation                     | replenishThresholdQty                             | bigint      | bigint         | NO            |             |
| scMMLocation                     | reservedMoveQty                                   | bigint      | bigint         | NO            |             |
| scMMLocation                     | reservedPickQty                                   | bigint      | bigint         | NO            |             |
| scMMLocation                     | site_id                                           | int         | int            | NO            |             |
| scMMLocation                     | uoi_id                                            | int         | int            | NO            |             |
| scMMLocation                     | uoiConfigLocation_id                              | int         | int            | NO            |             |
| scMMLocation                     | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scMMLocation                     | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMMLocation                     | weightUOM_id                                      | int         | int            | NO            |             |
| scMMLocationLog                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMMLocationLog                  | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scMMLocationLog                  | classoid                                          | int         | int            | NO            |             |
| scMMLocationLog                  | condition_id                                      | int         | int            | NO            |             |
| scMMLocationLog                  | location_id                                       | int         | int            | NO            |             |
| scMMLocationLog                  | owner_id                                          | int         | int            | NO            |             |
| scMMLocationLog                  | pickedQty                                         | varchar     | varchar(10)    | NO            |             |
| scMMLocationLog                  | quantity                                          | varchar     | varchar(10)    | NO            |             |
| scMMLocationLog                  | replenishmentQty                                  | varchar     | varchar(10)    | NO            |             |
| scMMLocationLog                  | reservedMoveQty                                   | varchar     | varchar(10)    | NO            |             |
| scMMLocationLog                  | reservedPickQty                                   | varchar     | varchar(10)    | NO            |             |
| scMMLocationLog                  | timestamp                                         | datetime    | datetime       | NO            |             |
| scMMLocationLog                  | uoiConfigLocation                                 | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | oid                                               | int         | int            | NO            | Primary Key |
| scMMSiteAttributes               | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scMMSiteAttributes               | abcClass_id                                       | int         | int            | NO            |             |
| scMMSiteAttributes               | allowMixAttributes                                | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | allowMixExpiryDate                                | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | allowMixItems                                     | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | allowMixLotNo                                     | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | allowMixMode                                      | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | allowMixOwners                                    | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | allowReserve                                      | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | catchWeightMode                                   | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | checklistInboundByItem                            | int         | int            | NO            |             |
| scMMSiteAttributes               | checklistInboundByLOTNO                           | int         | int            | NO            |             |
| scMMSiteAttributes               | classoid                                          | int         | int            | NO            |             |
| scMMSiteAttributes               | conditionChangeReasonList_id                      | int         | int            | NO            |             |
| scMMSiteAttributes               | conditionReasonRequired                           | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | confLocMovingRangeOverlapValidationMode           | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | consumptionTolerance                              | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | consumptionToleranceMode                          | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | cooReceiving                                      | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | cooTracking                                       | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | customerExpiryDateTolerance                       | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | customerExpiryDateToleranceMode                   | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | deliverySequence                                  | int         | int            | NO            |             |
| scMMSiteAttributes               | description                                       | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | expiryDateDelay                                   | int         | int            | NO            |             |
| scMMSiteAttributes               | expiryDateProduction                              | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | expiryDateReceiving                               | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | expiryDateTracking                                | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | externalBarcodeTracking                           | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | gs1LabelFormat                                    | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | handlingMaterialQtyAutomaticAdjustReason_id       | int         | int            | NO            |             |
| scMMSiteAttributes               | ingredientUOI_id                                  | int         | int            | NO            |             |
| scMMSiteAttributes               | inventoryUOI_id                                   | int         | int            | NO            |             |
| scMMSiteAttributes               | lotNoFormat_id                                    | int         | int            | NO            |             |
| scMMSiteAttributes               | lotNoProduction                                   | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | lotNoReceiving                                    | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | lotNoTracking                                     | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | manufacturerReceiving                             | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | manufacturerTracking                              | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | manufacturingUOI_id                               | int         | int            | NO            |             |
| scMMSiteAttributes               | maxqty                                            | int         | int            | NO            |             |
| scMMSiteAttributes               | minqty                                            | int         | int            | NO            |             |
| scMMSiteAttributes               | mmInfoLabelSite                                   | int         | int            | NO            |             |
| scMMSiteAttributes               | name                                              | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | overPickTolerance                                 | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | overReceivingTolerance                            | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | overrideShippableMode                             | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | owner_id                                          | int         | int            | NO            |             |
| scMMSiteAttributes               | packlabel_id                                      | int         | int            | NO            |             |
| scMMSiteAttributes               | pickingPriority                                   | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | pickingPriorityEnforcement                        | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | pickingPriorityValidation                         | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | pickingSequence                                   | int         | int            | NO            |             |
| scMMSiteAttributes               | picklabel_id                                      | int         | int            | NO            |             |
| scMMSiteAttributes               | printSingleShippingInfoLabelPerLine               | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | productionDateReceiving                           | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | putawayAllowedCondition                           | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | putawayFromReceiving                              | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | putawayRestrainConfiguredZones                    | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | quantityReasonRequired                            | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | receivingUOI_id                                   | int         | int            | NO            |             |
| scMMSiteAttributes               | receivingWeightDimensionUpdateDelay               | int         | int            | NO            |             |
| scMMSiteAttributes               | receivingWeightDimensionUpdateMode                | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | reclabel_id                                       | int         | int            | NO            |             |
| scMMSiteAttributes               | sampleQAFrequency                                 | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | sampleQAMode                                      | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | sampleQAQty                                       | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | scrapReasonList_id                                | int         | int            | NO            |             |
| scMMSiteAttributes               | serialNoFormat_id                                 | int         | int            | NO            |             |
| scMMSiteAttributes               | serialNoTracking                                  | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | shiplabel_id                                      | int         | int            | NO            |             |
| scMMSiteAttributes               | shippableLimit                                    | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | shippingInfoLabel_id                              | int         | int            | NO            |             |
| scMMSiteAttributes               | shippingInfoLabelQty                              | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | shippingLabelQty                                  | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | shippingUOI_id                                    | int         | int            | NO            |             |
| scMMSiteAttributes               | shortPickTolerance                                | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | site_id                                           | int         | int            | NO            |             |
| scMMSiteAttributes               | siteConfiguration_id                              | int         | int            | NO            |             |
| scMMSiteAttributes               | sitePartNo                                        | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | stackingMode                                      | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | temperatureCategory_id                            | int         | int            | NO            |             |
| scMMSiteAttributes               | uniqueAttributeByExternalBarcode                  | varchar     | varchar(10)    | NO            |             |
| scMMSiteAttributes               | vendorExpiryDateTolerance                         | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | vendorExpiryDateToleranceMode                     | varchar     | varchar(255)   | NO            |             |
| scMMSiteAttributes               | womh_id                                           | int         | int            | NO            |             |
| scMMStatistic                    | oid                                               | int         | int            | NO            | Primary Key |
| scMMStatistic                    | mm_id                                             | int         | int            | NO            | Foreign Key |
| scMMStatistic                    | classoid                                          | int         | int            | NO            |             |
| scMMStatistic                    | name                                              | varchar     | varchar(255)   | NO            |             |
| scMMStatistic                    | site_id                                           | int         | int            | NO            |             |
| scMMStatistic                    | value                                             | varchar     | varchar(255)   | NO            |             |
| scMOVE                           | oid                                               | int         | int            | NO            | Primary Key |
| scMOVE                           | fromLocation_id                                   | int         | int            | NO            | Foreign Key |
| scMOVE                           | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scMOVE                           | parent_id                                         | int         | int            | NO            | Foreign Key |
| scMOVE                           | site_id                                           | int         | int            | NO            | Foreign Key |
| scMOVE                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scMOVE                           | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scMOVE                           | classoid                                          | int         | int            | NO            |             |
| scMOVE                           | condition_id                                      | int         | int            | NO            |             |
| scMOVE                           | currentLocation_id                                | int         | int            | NO            |             |
| scMOVE                           | displayPartNo                                     | varchar     | varchar(255)   | NO            |             |
| scMOVE                           | from_id                                           | int         | int            | NO            |             |
| scMOVE                           | fromContainer_id                                  | int         | int            | NO            |             |
| scMOVE                           | fromZone_id                                       | int         | int            | NO            |             |
| scMOVE                           | generatedItem_id                                  | int         | int            | NO            |             |
| scMOVE                           | inProgressQty                                     | bigint      | bigint         | NO            |             |
| scMOVE                           | item_id                                           | int         | int            | NO            |             |
| scMOVE                           | lastLockedTime                                    | datetime    | datetime       | NO            |             |
| scMOVE                           | lastUser_id                                       | int         | int            | NO            |             |
| scMOVE                           | lockedUntil                                       | datetime    | datetime       | NO            |             |
| scMOVE                           | moveAction                                        | varchar     | varchar(255)   | NO            |             |
| scMOVE                           | movedQty                                          | bigint      | bigint         | NO            |             |
| scMOVE                           | movingJob_id                                      | int         | int            | NO            |             |
| scMOVE                           | owner_id                                          | int         | int            | NO            |             |
| scMOVE                           | priority                                          | varchar     | varchar(255)   | NO            |             |
| scMOVE                           | quantity                                          | bigint      | bigint         | NO            |             |
| scMOVE                           | queue_id                                          | int         | int            | NO            |             |
| scMOVE                           | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scMOVE                           | replenReservedBarcode_id                          | int         | int            | NO            |             |
| scMOVE                           | requiredDate                                      | datetime    | datetime       | NO            |             |
| scMOVE                           | to_id                                             | int         | int            | NO            |             |
| scMOVE                           | toContainer_id                                    | int         | int            | NO            |             |
| scMOVE                           | toLocation_id                                     | int         | int            | NO            |             |
| scMOVE                           | toZone_id                                         | int         | int            | NO            |             |
| scMOVE                           | type                                              | varchar     | varchar(255)   | NO            |             |
| scMOVE                           | uoi_id                                            | int         | int            | NO            |             |
| scMOVEDimension                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMOVEDimension                  | move_id                                           | int         | int            | NO            | Foreign Key |
| scMOVEDimension                  | classoid                                          | int         | int            | NO            |             |
| scMOVEDimension                  | dimension_id                                      | int         | int            | NO            |             |
| scMOVEDimension                  | mode                                              | varchar     | varchar(255)   | NO            |             |
| scMOVEDimension                  | quantity                                          | bigint      | bigint         | NO            |             |
| scMOVEDimension                  | uoi_id                                            | int         | int            | NO            |             |
| scMREQToSHLI                     | oid                                               | int         | int            | NO            | Primary Key |
| scMREQToSHLI                     | mreq_id                                           | int         | int            | NO            | Foreign Key |
| scMREQToSHLI                     | shli_id                                           | int         | int            | NO            | Foreign Key |
| scMREQToSHLI                     | classoid                                          | int         | int            | NO            |             |
| scMREQToSHLI                     | quantity                                          | bigint      | bigint         | NO            |             |
| scMREQToSHLI                     | receivedQty                                       | bigint      | bigint         | NO            |             |
| scMREQToSHLI                     | toReceiveQty                                      | bigint      | bigint         | NO            |             |
| scMREQToSHLI                     | uoi_id                                            | int         | int            | NO            |             |
| scMSHLH                          | oid                                               | int         | int            | NO            | Primary Key |
| scMSHLH                          | shipfrom_id                                       | int         | int            | NO            | Foreign Key |
| scMSHLH                          | shipto_id                                         | int         | int            | NO            | Foreign Key |
| scMSHLH                          | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scMSHLH                          | type_id                                           | int         | int            | NO            | Foreign Key |
| scMSHLH                          | bolNumber                                         | varchar     | varchar(255)   | NO            |             |
| scMSHLH                          | carrier_id                                        | int         | int            | NO            |             |
| scMSHLH                          | classoid                                          | int         | int            | NO            |             |
| scMSHLH                          | createStamp                                       | datetime    | datetime       | NO            |             |
| scMSHLH                          | createUser_id                                     | int         | int            | NO            |             |
| scMSHLH                          | deliveryArrival                                   | datetime    | datetime       | NO            |             |
| scMSHLH                          | deliveryDate                                      | datetime    | datetime       | NO            |             |
| scMSHLH                          | deliveryDeparture                                 | datetime    | datetime       | NO            |             |
| scMSHLH                          | deliverySequence                                  | int         | int            | NO            |             |
| scMSHLH                          | equipment_id                                      | int         | int            | NO            |             |
| scMSHLH                          | equipmentNo                                       | varchar     | varchar(255)   | NO            |             |
| scMSHLH                          | equipmentType_id                                  | int         | int            | NO            |             |
| scMSHLH                          | load_id                                           | int         | int            | NO            |             |
| scMSHLH                          | location_id                                       | int         | int            | NO            |             |
| scMSHLH                          | owner_id                                          | int         | int            | NO            |             |
| scMSHLH                          | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scMSHLH                          | sealNo                                            | varchar     | varchar(255)   | NO            |             |
| scMSHLH                          | shippedDate                                       | datetime    | datetime       | NO            |             |
| scMSHLH                          | shippingTerms_id                                  | int         | int            | NO            |             |
| scMSHLH                          | updateStamp                                       | datetime    | datetime       | NO            |             |
| scMSHLH                          | updateUser_id                                     | int         | int            | NO            |             |
| scManufacturingJob               | oid                                               | int         | int            | NO            | Primary Key |
| scManufacturingJob               | site_id                                           | int         | int            | NO            | Foreign Key |
| scManufacturingJob               | allowModifyDependencies                           | varchar     | varchar(10)    | NO            |             |
| scManufacturingJob               | allowOverProduction                               | varchar     | varchar(10)    | NO            |             |
| scManufacturingJob               | classoid                                          | int         | int            | NO            |             |
| scManufacturingJob               | consumptionMethod                                 | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | consumptionTolerance                              | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | consumptionToleranceMode                          | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | defaultBatchSize                                  | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | description                                       | text        | text           | NO            |             |
| scManufacturingJob               | expiryDateMode                                    | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | name                                              | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | outputCompletionCondition_id                      | int         | int            | NO            |             |
| scManufacturingJob               | outputCreationCondition_id                        | int         | int            | NO            |             |
| scManufacturingJob               | qtyConfirmationMethod                             | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | qtyOutputMode                                     | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | receivingLabel_id                                 | int         | int            | NO            |             |
| scManufacturingJob               | sequencingMethod                                  | varchar     | varchar(255)   | NO            |             |
| scManufacturingJob               | siteConfiguration_id                              | int         | int            | NO            |             |
| scManufacturingJob               | status                                            | varchar     | varchar(255)   | NO            |             |
| scMaterial                       | oid                                               | int         | int            | NO            | Primary Key |
| scMaterial                       | agropurMaterialSupplier_id                        | int         | int            | NO            | Foreign Key |
| scMaterial                       | asset_id                                          | int         | int            | NO            | Foreign Key |
| scMaterial                       | container_id                                      | int         | int            | NO            | Foreign Key |
| scMaterial                       | currentLOAD_id                                    | int         | int            | NO            | Foreign Key |
| scMaterial                       | currentPKLI_id                                    | int         | int            | NO            | Foreign Key |
| scMaterial                       | currentSHLI_id                                    | int         | int            | NO            | Foreign Key |
| scMaterial                       | expiryDate                                        | datetime    | datetime       | NO            | Foreign Key |
| scMaterial                       | externalOID                                       | varchar     | varchar(255)   | NO            | Foreign Key |
| scMaterial                       | label_id                                          | int         | int            | NO            | Foreign Key |
| scMaterial                       | location_id                                       | int         | int            | NO            | Foreign Key |
| scMaterial                       | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scMaterial                       | origin_id                                         | int         | int            | NO            | Foreign Key |
| scMaterial                       | parent_id                                         | int         | int            | NO            | Foreign Key |
| scMaterial                       | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scMaterial                       | topAsset_id                                       | int         | int            | NO            | Foreign Key |
| scMaterial                       | topContainer_id                                   | int         | int            | NO            | Foreign Key |
| scMaterial                       | transportEquipment_id                             | int         | int            | NO            | Foreign Key |
| scMaterial                       | type                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scMaterial                       | abcClass_id                                       | int         | int            | NO            |             |
| scMaterial                       | agropurLotNo                                      | varchar     | varchar(255)   | NO            |             |
| scMaterial                       | agropurLotNoCalculated                            | varchar     | varchar(10)    | NO            |             |
| scMaterial                       | classoid                                          | int         | int            | NO            |             |
| scMaterial                       | condition                                         | varchar     | varchar(255)   | NO            |             |
| scMaterial                       | conditionReason_id                                | int         | int            | NO            |             |
| scMaterial                       | costCenter_id                                     | int         | int            | NO            |             |
| scMaterial                       | creationDate                                      | datetime    | datetime       | NO            |             |
| scMaterial                       | currentMOVE_id                                    | int         | int            | NO            |             |
| scMaterial                       | currentPKLH_id                                    | int         | int            | NO            |             |
| scMaterial                       | currentRCLI_id                                    | int         | int            | NO            |             |
| scMaterial                       | currentSKLI_id                                    | int         | int            | NO            |             |
| scMaterial                       | currentUKLI_id                                    | int         | int            | NO            |             |
| scMaterial                       | currentWOS_id                                     | int         | int            | NO            |             |
| scMaterial                       | depth                                             | decimal     | decimal(19,2)  | NO            |             |
| scMaterial                       | dimensionType                                     | varchar     | varchar(255)   | NO            |             |
| scMaterial                       | dimensionUOM_id                                   | int         | int            | NO            |             |
| scMaterial                       | displayPartNo                                     | varchar     | varchar(255)   | NO            |             |
| scMaterial                       | height                                            | decimal     | decimal(19,2)  | NO            |             |
| scMaterial                       | history_id                                        | int         | int            | NO            |             |
| scMaterial                       | inventoryUOI_id                                   | int         | int            | NO            |             |
| scMaterial                       | lastMovedDate                                     | datetime    | datetime       | NO            |             |
| scMaterial                       | manualWeight                                      | varchar     | varchar(10)    | NO            |             |
| scMaterial                       | materialCondition_id                              | int         | int            | NO            |             |
| scMaterial                       | mobileEquipment_id                                | int         | int            | NO            |             |
| scMaterial                       | output_id                                         | int         | int            | NO            |             |
| scMaterial                       | owner_id                                          | int         | int            | NO            |             |
| scMaterial                       | packingContainer_id                               | int         | int            | NO            |             |
| scMaterial                       | partitionNo                                       | int         | int            | NO            |             |
| scMaterial                       | position                                          | varchar     | varchar(255)   | NO            |             |
| scMaterial                       | previous_id                                       | int         | int            | NO            |             |
| scMaterial                       | productionDate                                    | datetime    | datetime       | NO            |             |
| scMaterial                       | putawayDate                                       | datetime    | datetime       | NO            |             |
| scMaterial                       | quantity                                          | bigint      | bigint         | NO            |             |
| scMaterial                       | receptionDate                                     | datetime    | datetime       | NO            |             |
| scMaterial                       | reservedQty                                       | bigint      | bigint         | NO            |             |
| scMaterial                       | site_id                                           | int         | int            | NO            |             |
| scMaterial                       | unitCost                                          | decimal     | decimal(19,2)  | NO            |             |
| scMaterial                       | unitPrice                                         | decimal     | decimal(19,2)  | NO            |             |
| scMaterial                       | uoi_id                                            | int         | int            | NO            |             |
| scMaterial                       | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scMaterial                       | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMaterial                       | weightUOM_id                                      | int         | int            | NO            |             |
| scMaterial                       | width                                             | decimal     | decimal(19,2)  | NO            |             |
| scMaterial                       | zone_id                                           | int         | int            | NO            |             |
| scMaterialBarcode                | oid                                               | int         | int            | NO            | Primary Key |
| scMaterialBarcode                | classoid                                          | int         | int            | NO            | Foreign Key |
| scMaterialBarcode                | material_id                                       | int         | int            | NO            | Foreign Key |
| scMaterialBarcode                | country_id                                        | int         | int            | NO            |             |
| scMaterialBarcode                | dimension_id                                      | int         | int            | NO            |             |
| scMaterialBarcode                | dimensionUOM_id                                   | int         | int            | NO            |             |
| scMaterialBarcode                | expiryDate                                        | datetime    | datetime       | NO            |             |
| scMaterialBarcode                | gtin_id                                           | int         | int            | NO            |             |
| scMaterialBarcode                | lotNo                                             | varchar     | varchar(255)   | NO            |             |
| scMaterialBarcode                | partitionNo                                       | int         | int            | NO            |             |
| scMaterialBarcode                | productionDate                                    | datetime    | datetime       | NO            |             |
| scMaterialBarcode                | quantity                                          | bigint      | bigint         | NO            |             |
| scMaterialBarcode                | report_id                                         | int         | int            | NO            |             |
| scMaterialBarcode                | status                                            | varchar     | varchar(255)   | NO            |             |
| scMaterialBarcode                | uoi_id                                            | int         | int            | NO            |             |
| scMaterialBarcode                | value                                             | varchar     | varchar(255)   | NO            |             |
| scMaterialBarcode                | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scMaterialBarcode                | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMaterialBarcode                | weightUOM_id                                      | int         | int            | NO            |             |
| scMaterialMaster                 | oid                                               | int         | int            | NO            | Primary Key |
| scMaterialMaster                 | baseUOI_id                                        | int         | int            | NO            | Foreign Key |
| scMaterialMaster                 | mmProductClass_id                                 | int         | int            | NO            | Foreign Key |
| scMaterialMaster                 | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scMaterialMaster                 | partNo                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scMaterialMaster                 | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scMaterialMaster                 | agrFormat                                         | varchar     | varchar(255)   | NO            |             |
| scMaterialMaster                 | argFormatUOM                                      | varchar     | varchar(255)   | NO            |             |
| scMaterialMaster                 | category2_id                                      | int         | int            | NO            |             |
| scMaterialMaster                 | category3_id                                      | int         | int            | NO            |             |
| scMaterialMaster                 | category_id                                       | int         | int            | NO            |             |
| scMaterialMaster                 | classoid                                          | int         | int            | NO            |             |
| scMaterialMaster                 | createStamp                                       | datetime    | datetime       | NO            |             |
| scMaterialMaster                 | createUser_id                                     | int         | int            | NO            |             |
| scMaterialMaster                 | description                                       | varchar     | varchar(255)   | NO            |             |
| scMaterialMaster                 | description_id                                    | int         | int            | NO            |             |
| scMaterialMaster                 | hazmat                                            | int         | int            | NO            |             |
| scMaterialMaster                 | itemTemplate_id                                   | int         | int            | NO            |             |
| scMaterialMaster                 | maxNumberOfLicencePlatesStacked                   | int         | int            | NO            |             |
| scMaterialMaster                 | name_id                                           | int         | int            | NO            |             |
| scMaterialMaster                 | natureSubClass                                    | varchar     | varchar(255)   | NO            |             |
| scMaterialMaster                 | nmfc                                              | int         | int            | NO            |             |
| scMaterialMaster                 | nmfcClass                                         | int         | int            | NO            |             |
| scMaterialMaster                 | owner_id                                          | int         | int            | NO            |             |
| scMaterialMaster                 | precisionlength                                   | int         | int            | NO            |             |
| scMaterialMaster                 | purchasingPrice                                   | decimal     | decimal(19,2)  | NO            |             |
| scMaterialMaster                 | shipInCase                                        | varchar     | varchar(10)    | NO            |             |
| scMaterialMaster                 | shippingDescription                               | varchar     | varchar(255)   | NO            |             |
| scMaterialMaster                 | supplier                                          | varchar     | varchar(255)   | NO            |             |
| scMaterialMaster                 | type                                              | varchar     | varchar(255)   | NO            |             |
| scMaterialMaster                 | updateStamp                                       | datetime    | datetime       | NO            |             |
| scMaterialMaster                 | updateUser_id                                     | int         | int            | NO            |             |
| scMobileEquipment                | oid                                               | int         | int            | NO            | Primary Key |
| scMobileEquipment                | parent_id                                         | int         | int            | NO            | Foreign Key |
| scMobileEquipment                | site_id                                           | int         | int            | NO            | Foreign Key |
| scMobileEquipment                | capacity                                          | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipment                | capacityUsed                                      | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipment                | classoid                                          | int         | int            | NO            |             |
| scMobileEquipment                | currentPKLH_id                                    | int         | int            | NO            |             |
| scMobileEquipment                | dimensionUOM_id                                   | int         | int            | NO            |             |
| scMobileEquipment                | items                                             | int         | int            | NO            |             |
| scMobileEquipment                | job_id                                            | int         | int            | NO            |             |
| scMobileEquipment                | location_id                                       | int         | int            | NO            |             |
| scMobileEquipment                | maxWeight                                         | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipment                | mobileEquipment_id                                | int         | int            | NO            |             |
| scMobileEquipment                | name                                              | varchar     | varchar(255)   | NO            |             |
| scMobileEquipment                | status                                            | varchar     | varchar(255)   | NO            |             |
| scMobileEquipment                | transportEquipment_id                             | int         | int            | NO            |             |
| scMobileEquipment                | type_id                                           | int         | int            | NO            |             |
| scMobileEquipment                | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipment                | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipment                | weightUOM_id                                      | int         | int            | NO            |             |
| scMobileEquipment                | zone_id                                           | int         | int            | NO            |             |
| scMobileEquipmentType            | oid                                               | int         | int            | NO            | Primary Key |
| scMobileEquipmentType            | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scMobileEquipmentType            | agropurType                                       | varchar     | varchar(255)   | NO            |             |
| scMobileEquipmentType            | capacity                                          | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipmentType            | classoid                                          | int         | int            | NO            |             |
| scMobileEquipmentType            | description                                       | text        | text           | NO            |             |
| scMobileEquipmentType            | dimensionUOM_id                                   | int         | int            | NO            |             |
| scMobileEquipmentType            | interiorDepth                                     | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipmentType            | interiorHeight                                    | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipmentType            | interiorWidth                                     | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipmentType            | lpnCapacity                                       | int         | int            | NO            |             |
| scMobileEquipmentType            | maxWeight                                         | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipmentType            | status                                            | varchar     | varchar(255)   | NO            |             |
| scMobileEquipmentType            | type                                              | varchar     | varchar(255)   | NO            |             |
| scMobileEquipmentType            | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMobileEquipmentType            | weightUOM_id                                      | int         | int            | NO            |             |
| scMovement                       | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scMovement                       | classoid                                          | int         | int            | NO            | Foreign Key |
| scMovement                       | eventDate                                         | datetime    | datetime       | NO            | Foreign Key |
| scMovement                       | fromContainer_id                                  | int         | int            | NO            | Foreign Key |
| scMovement                       | fromLocation_id                                   | int         | int            | NO            | Foreign Key |
| scMovement                       | fromParent_id                                     | int         | int            | NO            | Foreign Key |
| scMovement                       | fromSite_id                                       | int         | int            | NO            | Foreign Key |
| scMovement                       | fromTransportEquipment_id                         | int         | int            | NO            | Foreign Key |
| scMovement                       | fromZone_id                                       | int         | int            | NO            | Foreign Key |
| scMovement                       | item_id                                           | int         | int            | NO            | Foreign Key |
| scMovement                       | itemMaster_id                                     | int         | int            | NO            | Foreign Key |
| scMovement                       | reference_id                                      | int         | int            | NO            | Foreign Key |
| scMovement                       | sourceItem_id                                     | int         | int            | NO            | Foreign Key |
| scMovement                       | toContainer_id                                    | int         | int            | NO            | Foreign Key |
| scMovement                       | toLocation_id                                     | int         | int            | NO            | Foreign Key |
| scMovement                       | toParent_id                                       | int         | int            | NO            | Foreign Key |
| scMovement                       | toSite_id                                         | int         | int            | NO            | Foreign Key |
| scMovement                       | toTransportEquipment_id                           | int         | int            | NO            | Foreign Key |
| scMovement                       | toZone_id                                         | int         | int            | NO            | Foreign Key |
| scMovement                       | type                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scMovement                       | user_id                                           | int         | int            | NO            | Foreign Key |
| scMovement                       | comment_id                                        | int         | int            | NO            |             |
| scMovement                       | dimensionUOM_id                                   | int         | int            | NO            |             |
| scMovement                       | fromCondition_id                                  | int         | int            | NO            |             |
| scMovement                       | fromCostCenter_id                                 | int         | int            | NO            |             |
| scMovement                       | fromMaterial_id                                   | int         | int            | NO            |             |
| scMovement                       | fromMobileEquipment_id                            | int         | int            | NO            |             |
| scMovement                       | fromOwner_id                                      | int         | int            | NO            |             |
| scMovement                       | fromStatus                                        | varchar     | varchar(255)   | NO            |             |
| scMovement                       | fromTopContainer_id                               | int         | int            | NO            |             |
| scMovement                       | parent_id                                         | int         | int            | NO            |             |
| scMovement                       | partitionNo                                       | int         | int            | NO            |             |
| scMovement                       | previous_id                                       | int         | int            | NO            |             |
| scMovement                       | quantity                                          | bigint      | bigint         | NO            |             |
| scMovement                       | reason_id                                         | int         | int            | NO            |             |
| scMovement                       | referenceName                                     | varchar     | varchar(255)   | NO            |             |
| scMovement                       | stampDate                                         | datetime    | datetime       | NO            |             |
| scMovement                       | toCondition_id                                    | int         | int            | NO            |             |
| scMovement                       | toCostCenter_id                                   | int         | int            | NO            |             |
| scMovement                       | toMaterial_id                                     | int         | int            | NO            |             |
| scMovement                       | toMobileEquipment_id                              | int         | int            | NO            |             |
| scMovement                       | toOwner_id                                        | int         | int            | NO            |             |
| scMovement                       | toStatus                                          | varchar     | varchar(255)   | NO            |             |
| scMovement                       | toTopContainer_id                                 | int         | int            | NO            |             |
| scMovement                       | uoiconfig_id                                      | int         | int            | NO            |             |
| scMovement                       | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scMovement                       | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scMovement                       | weightUOM_id                                      | int         | int            | NO            |             |
| scMovingJob                      | oid                                               | int         | int            | NO            | Primary Key |
| scMovingJob                      | site_id                                           | int         | int            | NO            | Foreign Key |
| scMovingJob                      | allowLPNMove                                      | varchar     | varchar(10)    | NO            |             |
| scMovingJob                      | askMobileEquipmentOperating                       | varchar     | varchar(10)    | NO            |             |
| scMovingJob                      | assumeQuantity                                    | varchar     | varchar(10)    | NO            |             |
| scMovingJob                      | classoid                                          | int         | int            | NO            |             |
| scMovingJob                      | description                                       | text        | text           | NO            |             |
| scMovingJob                      | lockingDuration                                   | int         | int            | NO            |             |
| scMovingJob                      | lpnCapacityDefault                                | int         | int            | NO            |             |
| scMovingJob                      | lpnCapacityReachMode                              | varchar     | varchar(255)   | NO            |             |
| scMovingJob                      | lpnCapacityStartMoveNotReachMode                  | varchar     | varchar(255)   | NO            |             |
| scMovingJob                      | name                                              | varchar     | varchar(255)   | NO            |             |
| scMovingJob                      | returnToLocationAfterMove                         | varchar     | varchar(10)    | NO            |             |
| scMovingJob                      | route_id                                          | int         | int            | NO            |             |
| scMovingJob                      | shortMode                                         | varchar     | varchar(255)   | NO            |             |
| scMovingJob                      | siteConfiguration_id                              | int         | int            | NO            |             |
| scOrder                          | oid                                               | int         | int            | NO            | Primary Key |
| scOrder                          | orderNo                                           | varchar     | varchar(255)   | NO            | Foreign Key |
| scOrder                          | orderType_id                                      | int         | int            | NO            | Foreign Key |
| scOrder                          | referenceNo                                       | varchar     | varchar(255)   | NO            | Foreign Key |
| scOrder                          | requester_id                                      | int         | int            | NO            | Foreign Key |
| scOrder                          | requiredDate                                      | datetime    | datetime       | NO            | Foreign Key |
| scOrder                          | shippedDate                                       | datetime    | datetime       | NO            | Foreign Key |
| scOrder                          | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scOrder                          | updateDate                                        | datetime    | datetime       | NO            | Foreign Key |
| scOrder                          | workOrder_id                                      | int         | int            | NO            | Foreign Key |
| scOrder                          | backOrder                                         | varchar     | varchar(255)   | NO            |             |
| scOrder                          | billTo_id                                         | int         | int            | NO            |             |
| scOrder                          | billToAddress_id                                  | int         | int            | NO            |             |
| scOrder                          | billToContact_id                                  | int         | int            | NO            |             |
| scOrder                          | billToCostCenter_id                               | int         | int            | NO            |             |
| scOrder                          | billToName                                        | varchar     | varchar(255)   | NO            |             |
| scOrder                          | broker_id                                         | int         | int            | NO            |             |
| scOrder                          | cancelReason                                      | int         | int            | NO            |             |
| scOrder                          | classoid                                          | int         | int            | NO            |             |
| scOrder                          | consolidationGroup                                | varchar     | varchar(255)   | NO            |             |
| scOrder                          | contractNo                                        | varchar     | varchar(255)   | NO            |             |
| scOrder                          | createUser_id                                     | int         | int            | NO            |             |
| scOrder                          | creationDate                                      | datetime    | datetime       | NO            |             |
| scOrder                          | cusotmerPO                                        | varchar     | varchar(255)   | NO            |             |
| scOrder                          | deliveryNo                                        | varchar     | varchar(255)   | NO            |             |
| scOrder                          | description                                       | text        | text           | NO            |             |
| scOrder                          | fillrateType_id                                   | int         | int            | NO            |             |
| scOrder                          | lastAdjustment_id                                 | int         | int            | NO            |             |
| scOrder                          | leadingStatus                                     | varchar     | varchar(255)   | NO            |             |
| scOrder                          | lifecycle                                         | varchar     | varchar(255)   | NO            |             |
| scOrder                          | loadingSequence                                   | int         | int            | NO            |             |
| scOrder                          | loadNumber                                        | varchar     | varchar(255)   | NO            |             |
| scOrder                          | loadSequence                                      | int         | int            | NO            |             |
| scOrder                          | maxShipmentQuantity                               | int         | int            | NO            |             |
| scOrder                          | minimumFillrate                                   | int         | int            | NO            |             |
| scOrder                          | nbContainer                                       | int         | int            | NO            |             |
| scOrder                          | orderClass                                        | varchar     | varchar(255)   | NO            |             |
| scOrder                          | orderPrice                                        | decimal     | decimal(19,2)  | NO            |             |
| scOrder                          | originalOrderNo                                   | varchar     | varchar(255)   | NO            |             |
| scOrder                          | originalPO                                        | int         | int            | NO            |             |
| scOrder                          | owner_id                                          | int         | int            | NO            |             |
| scOrder                          | partitionNo                                       | int         | int            | NO            |             |
| scOrder                          | pickCOPosition                                    | varchar     | varchar(255)   | NO            |             |
| scOrder                          | pickTicketNo                                      | varchar     | varchar(255)   | NO            |             |
| scOrder                          | priority                                          | varchar     | varchar(255)   | NO            |             |
| scOrder                          | receivedDate                                      | datetime    | datetime       | NO            |             |
| scOrder                          | requesterContact_id                               | int         | int            | NO            |             |
| scOrder                          | requesterDepartment_id                            | int         | int            | NO            |             |
| scOrder                          | route                                             | varchar     | varchar(255)   | NO            |             |
| scOrder                          | sealNumber                                        | varchar     | varchar(255)   | NO            |             |
| scOrder                          | sendCancelQtiesToOracle                           | varchar     | varchar(10)    | NO            |             |
| scOrder                          | sequenceERPConfirmation                           | int         | int            | NO            |             |
| scOrder                          | shipmentCount                                     | int         | int            | NO            |             |
| scOrder                          | shippingDetails_id                                | int         | int            | NO            |             |
| scOrder                          | supplier_id                                       | int         | int            | NO            |             |
| scOrder                          | trailer                                           | varchar     | varchar(255)   | NO            |             |
| scOrder                          | trailingStatus                                    | varchar     | varchar(255)   | NO            |             |
| scOrder                          | updateUser_id                                     | int         | int            | NO            |             |
| scOrder                          | workOrderNo                                       | varchar     | varchar(255)   | NO            |             |
| scOrderAdjustment                | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scOrderAdjustment                | order_id                                          | int         | int            | NO            | Foreign Key |
| scOrderAdjustment                | reference_id                                      | int         | int            | NO            | Foreign Key |
| scOrderAdjustment                | allocatedValue                                    | int         | int            | NO            |             |
| scOrderAdjustment                | cancelledValue                                    | int         | int            | NO            |             |
| scOrderAdjustment                | classoid                                          | int         | int            | NO            |             |
| scOrderAdjustment                | eventDate                                         | datetime    | datetime       | NO            |             |
| scOrderAdjustment                | fillRateType_id                                   | int         | int            | NO            |             |
| scOrderAdjustment                | leadingStatus                                     | varchar     | varchar(255)   | NO            |             |
| scOrderAdjustment                | orderedValue                                      | int         | int            | NO            |             |
| scOrderAdjustment                | outstandingValue                                  | int         | int            | NO            |             |
| scOrderAdjustment                | packedValue                                       | int         | int            | NO            |             |
| scOrderAdjustment                | partitionNo                                       | int         | int            | NO            |             |
| scOrderAdjustment                | pickedValue                                       | int         | int            | NO            |             |
| scOrderAdjustment                | shippedValue                                      | int         | int            | NO            |             |
| scOrderAdjustment                | status                                            | varchar     | varchar(255)   | NO            |             |
| scOrderAdjustment                | trailingStatus                                    | varchar     | varchar(255)   | NO            |             |
| scOrderAdjustment                | type                                              | varchar     | varchar(255)   | NO            |             |
| scOrderAdjustment                | user_id                                           | int         | int            | NO            |             |
| scOrderInstruction               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scOrderInstruction               | classoid                                          | int         | int            | NO            |             |
| scOrderInstruction               | instruction                                       | text        | text           | NO            |             |
| scOrderInstruction               | mreq_id                                           | int         | int            | NO            |             |
| scOrderInstruction               | partitionNo                                       | int         | int            | NO            |             |
| scOrderInstruction               | solh_id                                           | int         | int            | NO            |             |
| scOrderInstruction               | type                                              | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | oid                                               | int         | int            | NO            | Primary Key |
| scOrderLine                      | currentLoad_id                                    | int         | int            | NO            | Foreign Key |
| scOrderLine                      | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scOrderLine                      | parent_id                                         | int         | int            | NO            | Foreign Key |
| scOrderLine                      | pickTicketNo                                      | varchar     | varchar(255)   | NO            | Foreign Key |
| scOrderLine                      | referenceNo                                       | varchar     | varchar(255)   | NO            | Foreign Key |
| scOrderLine                      | requiredDate                                      | datetime    | datetime       | NO            | Foreign Key |
| scOrderLine                      | shipmentRequest_id                                | int         | int            | NO            | Foreign Key |
| scOrderLine                      | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scOrderLine                      | wave_id                                           | int         | int            | NO            | Foreign Key |
| scOrderLine                      | wos_id                                            | int         | int            | NO            | Foreign Key |
| scOrderLine                      | allocatedQty                                      | bigint      | bigint         | NO            |             |
| scOrderLine                      | allocationInvPolicy_id                            | int         | int            | NO            |             |
| scOrderLine                      | backOrder                                         | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | backorderQty                                      | bigint      | bigint         | NO            |             |
| scOrderLine                      | billToCostCenter_id                               | int         | int            | NO            |             |
| scOrderLine                      | blockPartialShipment                              | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scOrderLine                      | classoid                                          | int         | int            | NO            |             |
| scOrderLine                      | condition_id                                      | int         | int            | NO            |             |
| scOrderLine                      | consolidationGroup                                | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | consumedQty                                       | bigint      | bigint         | NO            |             |
| scOrderLine                      | costcenter_id                                     | int         | int            | NO            |             |
| scOrderLine                      | createStamp                                       | datetime    | datetime       | NO            |             |
| scOrderLine                      | createUser_id                                     | int         | int            | NO            |             |
| scOrderLine                      | currency                                          | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | description                                       | text        | text           | NO            |             |
| scOrderLine                      | displayPartNo                                     | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | fillrateType_id                                   | int         | int            | NO            |             |
| scOrderLine                      | generatedMREQ_id                                  | int         | int            | NO            |             |
| scOrderLine                      | ignoreOrderFillrate                               | varchar     | varchar(10)    | NO            |             |
| scOrderLine                      | leadingStatus                                     | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | lineOutstandingToCancelReason                     | int         | int            | NO            |             |
| scOrderLine                      | loadedQty                                         | bigint      | bigint         | NO            |             |
| scOrderLine                      | minimumFillrate                                   | int         | int            | NO            |             |
| scOrderLine                      | outstandingQty                                    | bigint      | bigint         | NO            |             |
| scOrderLine                      | overrideShippable                                 | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | owner_id                                          | int         | int            | NO            |             |
| scOrderLine                      | packedQty                                         | bigint      | bigint         | NO            |             |
| scOrderLine                      | partitionNo                                       | int         | int            | NO            |             |
| scOrderLine                      | pickCOPosition                                    | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | pickedQty                                         | bigint      | bigint         | NO            |             |
| scOrderLine                      | prepositionQty                                    | bigint      | bigint         | NO            |             |
| scOrderLine                      | priority                                          | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | quantity                                          | bigint      | bigint         | NO            |             |
| scOrderLine                      | receivedQty                                       | bigint      | bigint         | NO            |             |
| scOrderLine                      | receivingUOI_id                                   | int         | int            | NO            |             |
| scOrderLine                      | releasedQty                                       | bigint      | bigint         | NO            |             |
| scOrderLine                      | sequence                                          | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | shippedDate                                       | datetime    | datetime       | NO            |             |
| scOrderLine                      | shippedQty                                        | bigint      | bigint         | NO            |             |
| scOrderLine                      | shipTo_id                                         | int         | int            | NO            |             |
| scOrderLine                      | shipToContact_id                                  | int         | int            | NO            |             |
| scOrderLine                      | shipToDepartment_id                               | int         | int            | NO            |             |
| scOrderLine                      | shipToDoor_id                                     | int         | int            | NO            |             |
| scOrderLine                      | shipToLocation_id                                 | int         | int            | NO            |             |
| scOrderLine                      | stagedQty                                         | bigint      | bigint         | NO            |             |
| scOrderLine                      | supplier_id                                       | int         | int            | NO            |             |
| scOrderLine                      | supplierLocation_id                               | int         | int            | NO            |             |
| scOrderLine                      | supplierZone_id                                   | int         | int            | NO            |             |
| scOrderLine                      | toReceiveQty                                      | bigint      | bigint         | NO            |             |
| scOrderLine                      | trailingStatus                                    | varchar     | varchar(255)   | NO            |             |
| scOrderLine                      | unitPrice                                         | decimal     | decimal(19,2)  | NO            |             |
| scOrderLine                      | uoi_id                                            | int         | int            | NO            |             |
| scOrderLine                      | updateStamp                                       | datetime    | datetime       | NO            |             |
| scOrderLine                      | updateUser_id                                     | int         | int            | NO            |             |
| scOrderLineDimension             | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scOrderLineDimension             | soli_id                                           | int         | int            | NO            | Foreign Key |
| scOrderLineDimension             | backOrderQty                                      | bigint      | bigint         | NO            |             |
| scOrderLineDimension             | classoid                                          | int         | int            | NO            |             |
| scOrderLineDimension             | dimension_id                                      | int         | int            | NO            |             |
| scOrderLineDimension             | mode                                              | varchar     | varchar(255)   | NO            |             |
| scOrderLineDimension             | partitionNo                                       | int         | int            | NO            |             |
| scOrderLineDimension             | quantity                                          | bigint      | bigint         | NO            |             |
| scOrderLineDimension             | uoi_id                                            | int         | int            | NO            |             |
| scOrderLineLog                   | oid                                               | int         | int            | NO            | Primary Key |
| scOrderLineLog                   | orderLine_id                                      | int         | int            | NO            | Foreign Key |
| scOrderLineLog                   | eventDate                                         | datetime    | datetime       | NO            |             |
| scOrderLineLog                   | orderLineData                                     | varchar     | varchar(10000) | NO            |             |
| scOrderType                      | oid                                               | int         | int            | NO            | Primary Key |
| scOrderType                      | agropur_AllowDeliverFromContainerDeliveryWhenLoad | varchar     | varchar(10)    | NO            |             |
| scOrderType                      | allowContainerDelivery                            | varchar     | varchar(10)    | NO            |             |
| scOrderType                      | allowUpdateCarrier                                | varchar     | varchar(10)    | NO            |             |
| scOrderType                      | allowUpdateLoad                                   | varchar     | varchar(10)    | NO            |             |
| scOrderType                      | autoReleaseQty                                    | varchar     | varchar(10)    | NO            |             |
| scOrderType                      | canBeLockedByChecklist                            | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | cancelReasonList                                  | int         | int            | NO            |             |
| scOrderType                      | cancelReasonRequired                              | varchar     | varchar(10)    | NO            |             |
| scOrderType                      | classoid                                          | int         | int            | NO            |             |
| scOrderType                      | condition_id                                      | int         | int            | NO            |             |
| scOrderType                      | defaultSOLIPriority                               | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | deliverRestriction                                | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | deliveryNoAssignment                              | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | description                                       | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | enableTEUsageStatusWhenReceiptCompleted           | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | fillrateType_id                                   | int         | int            | NO            |             |
| scOrderType                      | InboundCompletionAction                           | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | initialStatus                                     | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | lifeCycle                                         | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | lineOutstandingToCancelReasonList                 | int         | int            | NO            |             |
| scOrderType                      | lineOutstandingToCancelReasonRequired             | varchar     | varchar(10)    | NO            |             |
| scOrderType                      | maxShipPKLIStatusRequired                         | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | name                                              | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | orderClass                                        | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | orderCompletion                                   | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | orderCreation                                     | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | outboundCancellation                              | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | outboundModification                              | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | owner                                             | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | preReceivingChecklist_id                          | int         | int            | NO            |             |
| scOrderType                      | reason_id                                         | int         | int            | NO            |             |
| scOrderType                      | receiptClosureAction                              | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | shipAction                                        | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | shipmentCreation                                  | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | shipmentType_id                                   | int         | int            | NO            |             |
| scOrderType                      | shortPickAction                                   | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | status                                            | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | teUsageStatusWhenReceiptCompleted                 | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | thresholdToEnableClosing                          | varchar     | varchar(255)   | NO            |             |
| scOrderType                      | zeroPickAction                                    | varchar     | varchar(255)   | NO            |             |
| scPKLH                           | oid                                               | int         | int            | NO            | Primary Key |
| scPKLH                           | parent_id                                         | int         | int            | NO            | Foreign Key |
| scPKLH                           | pickingJob_id                                     | int         | int            | NO            | Foreign Key |
| scPKLH                           | requiredDate                                      | datetime    | datetime       | NO            | Foreign Key |
| scPKLH                           | shipmentRequest_id                                | int         | int            | NO            | Foreign Key |
| scPKLH                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scPKLH                           | assignedDate                                      | datetime    | datetime       | NO            |             |
| scPKLH                           | balancingMethodUsed                               | varchar     | varchar(255)   | NO            |             |
| scPKLH                           | classoid                                          | int         | int            | NO            |             |
| scPKLH                           | consolidation_pklh_id                             | int         | int            | NO            |             |
| scPKLH                           | containerType_id                                  | int         | int            | NO            |             |
| scPKLH                           | dimensionUOM_id                                   | int         | int            | NO            |             |
| scPKLH                           | firstLocation_id                                  | int         | int            | NO            |             |
| scPKLH                           | firstZone_id                                      | int         | int            | NO            |             |
| scPKLH                           | lastPickStamp                                     | datetime    | datetime       | NO            |             |
| scPKLH                           | load_id                                           | int         | int            | NO            |             |
| scPKLH                           | loadSequence                                      | int         | int            | NO            |             |
| scPKLH                           | partitionNo                                       | int         | int            | NO            |             |
| scPKLH                           | plannedEnd                                        | datetime    | datetime       | NO            |             |
| scPKLH                           | plannedStart                                      | datetime    | datetime       | NO            |             |
| scPKLH                           | printedDate                                       | datetime    | datetime       | NO            |             |
| scPKLH                           | priority                                          | varchar     | varchar(255)   | NO            |             |
| scPKLH                           | queue_id                                          | int         | int            | NO            |             |
| scPKLH                           | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scPKLH                           | site_id                                           | int         | int            | NO            |             |
| scPKLH                           | sortedByLayer                                     | varchar     | varchar(10)    | NO            |             |
| scPKLH                           | splitOrderedPickLines                             | varchar     | varchar(10)    | NO            |             |
| scPKLH                           | subType                                           | varchar     | varchar(255)   | NO            |             |
| scPKLH                           | user_id                                           | int         | int            | NO            |             |
| scPKLH                           | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scPKLH                           | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scPKLH                           | weightUOM_id                                      | int         | int            | NO            |             |
| scPKLH                           | zone_id                                           | int         | int            | NO            |             |
| scPKLI                           | oid                                               | int         | int            | NO            | Primary Key |
| scPKLI                           | generatedMREQ_id                                  | int         | int            | NO            | Foreign Key |
| scPKLI                           | load_id                                           | int         | int            | NO            | Foreign Key |
| scPKLI                           | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scPKLI                           | mreq_id                                           | int         | int            | NO            | Foreign Key |
| scPKLI                           | pickedDate                                        | datetime    | datetime       | NO            | Foreign Key |
| scPKLI                           | pklh_id                                           | int         | int            | NO            | Foreign Key |
| scPKLI                           | referenceNo                                       | varchar     | varchar(255)   | NO            | Foreign Key |
| scPKLI                           | requiredDate                                      | datetime    | datetime       | NO            | Foreign Key |
| scPKLI                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scPKLI                           | supplierLocation_id                               | int         | int            | NO            | Foreign Key |
| scPKLI                           | backorder                                         | varchar     | varchar(255)   | NO            |             |
| scPKLI                           | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scPKLI                           | classoid                                          | int         | int            | NO            |             |
| scPKLI                           | condition_id                                      | int         | int            | NO            |             |
| scPKLI                           | createStamp                                       | datetime    | datetime       | NO            |             |
| scPKLI                           | createUser_id                                     | int         | int            | NO            |             |
| scPKLI                           | currentContainer_id                               | int         | int            | NO            |             |
| scPKLI                           | dimensionUOM_id                                   | int         | int            | NO            |             |
| scPKLI                           | expiryDate                                        | datetime    | datetime       | NO            |             |
| scPKLI                           | invalidPickPriority                               | varchar     | varchar(10)    | NO            |             |
| scPKLI                           | loadSequence                                      | int         | int            | NO            |             |
| scPKLI                           | location_id                                       | int         | int            | NO            |             |
| scPKLI                           | mreqToLoad_id                                     | int         | int            | NO            |             |
| scPKLI                           | owner_id                                          | int         | int            | NO            |             |
| scPKLI                           | packedQty                                         | bigint      | bigint         | NO            |             |
| scPKLI                           | palletLayer                                       | varchar     | varchar(255)   | NO            |             |
| scPKLI                           | parent_id                                         | int         | int            | NO            |             |
| scPKLI                           | partitionNo                                       | int         | int            | NO            |             |
| scPKLI                           | pickAction                                        | varchar     | varchar(255)   | NO            |             |
| scPKLI                           | pickCOPosition                                    | varchar     | varchar(255)   | NO            |             |
| scPKLI                           | pickedByUser_id                                   | int         | int            | NO            |             |
| scPKLI                           | pickedQty                                         | bigint      | bigint         | NO            |             |
| scPKLI                           | pickingLayer                                      | int         | int            | NO            |             |
| scPKLI                           | priority                                          | varchar     | varchar(255)   | NO            |             |
| scPKLI                           | quantity                                          | bigint      | bigint         | NO            |             |
| scPKLI                           | rcli_id                                           | int         | int            | NO            |             |
| scPKLI                           | replenishmentCount                                | int         | int            | NO            |             |
| scPKLI                           | requester_id                                      | int         | int            | NO            |             |
| scPKLI                           | sequence                                          | int         | int            | NO            |             |
| scPKLI                           | shipTo_id                                         | int         | int            | NO            |             |
| scPKLI                           | site_id                                           | int         | int            | NO            |             |
| scPKLI                           | splitPickLine                                     | varchar     | varchar(10)    | NO            |             |
| scPKLI                           | subType                                           | varchar     | varchar(255)   | NO            |             |
| scPKLI                           | supplier_id                                       | int         | int            | NO            |             |
| scPKLI                           | supplierZone_id                                   | int         | int            | NO            |             |
| scPKLI                           | toPickQuantity                                    | bigint      | bigint         | NO            |             |
| scPKLI                           | uoi_id                                            | int         | int            | NO            |             |
| scPKLI                           | updateStamp                                       | datetime    | datetime       | NO            |             |
| scPKLI                           | updateUser_id                                     | int         | int            | NO            |             |
| scPKLI                           | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scPKLI                           | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scPKLI                           | weightUOM_id                                      | int         | int            | NO            |             |
| scPKLI                           | zone_id                                           | int         | int            | NO            |             |
| scPKLIDimension                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scPKLIDimension                  | pkli_id                                           | int         | int            | NO            | Foreign Key |
| scPKLIDimension                  | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scPKLIDimension                  | classoid                                          | int         | int            | NO            |             |
| scPKLIDimension                  | dimension_id                                      | int         | int            | NO            |             |
| scPKLIDimension                  | mode                                              | varchar     | varchar(255)   | NO            |             |
| scPKLIDimension                  | partitionNo                                       | int         | int            | NO            |             |
| scPKLIDimension                  | pickedQty                                         | bigint      | bigint         | NO            |             |
| scPKLIDimension                  | quantity                                          | bigint      | bigint         | NO            |             |
| scPKLIDimension                  | uoi_id                                            | int         | int            | NO            |             |
| scPackingJob                     | oid                                               | int         | int            | NO            | Primary Key |
| scPackingJob                     | classoid                                          | int         | int            | NO            |             |
| scPackingJob                     | description                                       | text        | text           | NO            |             |
| scPackingJob                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scPackingJob                     | site_id                                           | int         | int            | NO            |             |
| scPackingJob                     | siteConfiguration_id                              | int         | int            | NO            |             |
| scPickingJob                     | oid                                               | int         | int            | NO            | Primary Key |
| scPickingJob                     | route_id                                          | int         | int            | NO            | Foreign Key |
| scPickingJob                     | site_id                                           | int         | int            | NO            | Foreign Key |
| scPickingJob                     | askMobileEquipmentOperating                       | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | assemblyLevel                                     | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | assemblyStartLocation                             | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | assyOverflowStrategy                              | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | autoDropLocation_id                               | int         | int            | NO            |             |
| scPickingJob                     | blockPicklistScanByUnassignedUsers                | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | bulkClusterCapacity                               | int         | int            | NO            |             |
| scPickingJob                     | classoid                                          | int         | int            | NO            |             |
| scPickingJob                     | clustersize                                       | int         | int            | NO            |             |
| scPickingJob                     | confMethod                                        | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | coPosAssignMode                                   | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | defaultContainer_id                               | int         | int            | NO            |             |
| scPickingJob                     | defaultCountingJob_id                             | int         | int            | NO            |             |
| scPickingJob                     | description                                       | text        | text           | NO            |             |
| scPickingJob                     | dropSuggestionSource                              | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | groupingZone                                      | int         | int            | NO            |             |
| scPickingJob                     | groupMethod                                       | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | includebo                                         | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | includePending                                    | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | labelFormat                                       | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | labelGroupBy                                      | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | maxItems                                          | int         | int            | NO            |             |
| scPickingJob                     | maxlines                                          | int         | int            | NO            |             |
| scPickingJob                     | maxLocations                                      | int         | int            | NO            |             |
| scPickingJob                     | maxorders                                         | int         | int            | NO            |             |
| scPickingJob                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | notifyPKLHComplete                                | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | notifyZoneChange                                  | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | orderlineqty                                      | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | orderType                                         | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | overPickTolerance                                 | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | overweightPercent                                 | int         | int            | NO            |             |
| scPickingJob                     | overweightStrategy                                | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | packreport_id                                     | int         | int            | NO            |             |
| scPickingJob                     | palletLevelingAssemblyMinLayerThreshold           | decimal     | decimal(19,2)  | NO            |             |
| scPickingJob                     | palletLevelingLayerOnPallet                       | int         | int            | NO            |             |
| scPickingJob                     | palletLevelingLinkedPickingJob                    | int         | int            | NO            |             |
| scPickingJob                     | palletLevelingMaxLayerOnPallet                    | int         | int            | NO            |             |
| scPickingJob                     | palletLevelingMinLayerOnPallet                    | int         | int            | NO            |             |
| scPickingJob                     | palletLevelingOverloadThreshold                   | decimal     | decimal(19,2)  | NO            |             |
| scPickingJob                     | palletLevelingRangeFullPallet                     | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | palletLevelingSharedPalletCultureSpace            | int         | int            | NO            |             |
| scPickingJob                     | pickingLabel_id                                   | int         | int            | NO            |             |
| scPickingJob                     | pickingPriorityValidation                         | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | pickListBalancingMethod                           | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | pickmethod                                        | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | pickmode                                          | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | pickRfListMode                                    | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | pklhCapacityReachMode                             | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | printLabelAtPicking                               | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | productConfirmationMethod                         | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | qtyConfMethod                                     | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | reverseConsolidationMode                          | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | sequence                                          | int         | int            | NO            |             |
| scPickingJob                     | shippingInfoLabel_id                              | int         | int            | NO            |             |
| scPickingJob                     | shippingInfoLabelQty                              | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | shippingLabel_id                                  | int         | int            | NO            |             |
| scPickingJob                     | shippingLabelQty                                  | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | shortPickAction                                   | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | shortPickCountMode                                | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | shortPickTolerance                                | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | showInstructions                                  | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | siteConfiguration_id                              | int         | int            | NO            |             |
| scPickingJob                     | skipZoneList                                      | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | sortedByLayer                                     | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | sortorder                                         | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | sortOrderList                                     | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | splitcarriers                                     | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | splitConsGroup                                    | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | splitdestination                                  | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | splitfamily                                       | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | splitShipment                                     | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | splitShipVia                                      | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | splitVolWeight                                    | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | userRequiredToReleaseOnAssembly                   | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | voicePicking                                      | varchar     | varchar(255)   | NO            |             |
| scPickingJob                     | volCapacity                                       | decimal     | decimal(19,2)  | NO            |             |
| scPickingJob                     | warnBaseUOI                                       | varchar     | varchar(10)    | NO            |             |
| scPickingJob                     | weightbase                                        | int         | int            | NO            |             |
| scPickingJob                     | weightCapacity                                    | decimal     | decimal(19,2)  | NO            |             |
| scPickingJob                     | workcenter_id                                     | int         | int            | NO            |             |
| scPrinter                        | oid                                               | int         | int            | NO            | Primary Key |
| scPrinter                        | backup_id                                         | int         | int            | NO            |             |
| scPrinter                        | classoid                                          | int         | int            | NO            |             |
| scPrinter                        | name                                              | varchar     | varchar(255)   | NO            |             |
| scPrinter                        | path                                              | varchar     | varchar(255)   | NO            |             |
| scPrinter                        | printerFormat_id                                  | int         | int            | NO            |             |
| scPrinter                        | printService_id                                   | int         | int            | NO            |             |
| scPrinter                        | site_id                                           | int         | int            | NO            |             |
| scPrinter                        | status                                            | varchar     | varchar(255)   | NO            |             |
| scPrinter                        | type_id                                           | int         | int            | NO            |             |
| scPrinter                        | voiceLabel_id                                     | int         | int            | NO            |             |
| scProductCategory                | oid                                               | int         | int            | NO            | Primary Key |
| scProductCategory                | code                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scProductCategory                | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scProductCategory                | classoid                                          | int         | int            | NO            |             |
| scProductCategory                | description                                       | varchar     | varchar(255)   | NO            |             |
| scProductCategory                | mmPosition                                        | varchar     | varchar(255)   | NO            |             |
| scProductCategoryItem            | oid                                               | int         | int            | NO            | Primary Key |
| scProductCategoryItem            | category_id                                       | int         | int            | NO            |             |
| scProductCategoryItem            | classoid                                          | int         | int            | NO            |             |
| scProductCategoryItem            | code                                              | varchar     | varchar(255)   | NO            |             |
| scProductCategoryItem            | name                                              | varchar     | varchar(255)   | NO            |             |
| scProductClass                   | oid                                               | int         | int            | NO            | Primary Key |
| scProductClass                   | classoid                                          | int         | int            | NO            |             |
| scProductClass                   | code                                              | varchar     | varchar(255)   | NO            |             |
| scProductClass                   | glaccount_id                                      | int         | int            | NO            |             |
| scProductClass                   | glcode                                            | varchar     | varchar(255)   | NO            |             |
| scProductClass                   | name                                              | varchar     | varchar(255)   | NO            |             |
| scProductClass                   | shipdesc                                          | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | oid                                               | int         | int            | NO            | Primary Key |
| scPutawayJob                     | site_id                                           | int         | int            | NO            | Foreign Key |
| scPutawayJob                     | allowAllConditions                                | varchar     | varchar(10)    | NO            |             |
| scPutawayJob                     | allowPutawayOverride                              | varchar     | varchar(10)    | NO            |             |
| scPutawayJob                     | automaticTaskCreation                             | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | binTypeSequenceRequired                           | varchar     | varchar(10)    | NO            |             |
| scPutawayJob                     | classoid                                          | int         | int            | NO            |             |
| scPutawayJob                     | constraintLocationMode                            | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | description                                       | text        | text           | NO            |             |
| scPutawayJob                     | maxAddSuggestions                                 | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | maxInitialSuggestions                             | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | movingJob_id                                      | int         | int            | NO            |             |
| scPutawayJob                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | pickingPriority                                   | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | pickingPriorityEnforcement                        | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | putawayOverrideReasonMode                         | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | siteConfiguration_id                              | int         | int            | NO            |             |
| scPutawayJob                     | suggestionMode                                    | varchar     | varchar(255)   | NO            |             |
| scPutawayJob                     | uoiMode                                           | varchar     | varchar(255)   | NO            |             |
| scPutawayOverrideEvent           | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scPutawayOverrideEvent           | reason_id                                         | int         | int            | NO            | Foreign Key |
| scPutawayOverrideEvent           | timestamp                                         | datetime    | datetime       | NO            | Foreign Key |
| scPutawayOverrideEvent           | user_id                                           | int         | int            | NO            | Foreign Key |
| scPutawayOverrideEvent           | classoid                                          | int         | int            | NO            |             |
| scPutawayOverrideEvent           | location_id                                       | int         | int            | NO            |             |
| scPutawayOverrideEvent           | materialMaster_id                                 | int         | int            | NO            |             |
| scPutawayOverrideEvent           | movement_id                                       | int         | int            | NO            |             |
| scPutawayOverrideEvent           | suggestedLocation_id                              | int         | int            | NO            |             |
| scPutawayOverrideEventReason     | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scPutawayOverrideEventReason     | classoid                                          | int         | int            | NO            |             |
| scPutawayOverrideEventReason     | description                                       | varchar     | varchar(255)   | NO            |             |
| scPutawayOverrideEventReason     | label                                             | varchar     | varchar(255)   | NO            |             |
| scPutawayOverrideEventReason     | name                                              | varchar     | varchar(255)   | NO            |             |
| scPutawaySuggestion              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scPutawaySuggestion              | putawayJob_id                                     | int         | int            | NO            | Foreign Key |
| scPutawaySuggestion              | allocateInventory                                 | varchar     | varchar(10)    | NO            |             |
| scPutawaySuggestion              | classoid                                          | int         | int            | NO            |             |
| scPutawaySuggestion              | enableConfLocMovingQtyRange                       | varchar     | varchar(10)    | NO            |             |
| scPutawaySuggestion              | locationType                                      | varchar     | varchar(255)   | NO            |             |
| scPutawaySuggestion              | maxPriority                                       | varchar     | varchar(255)   | NO            |             |
| scPutawaySuggestion              | maxSuggestions                                    | int         | int            | NO            |             |
| scPutawaySuggestion              | minPercentage                                     | int         | int            | NO            |             |
| scPutawaySuggestion              | minPriority                                       | varchar     | varchar(255)   | NO            |             |
| scPutawaySuggestion              | name                                              | varchar     | varchar(255)   | NO            |             |
| scPutawaySuggestion              | nearSuggestion_id                                 | int         | int            | NO            |             |
| scPutawaySuggestion              | sequence                                          | int         | int            | NO            |             |
| scPutawaySuggestion              | sortBy                                            | varchar     | varchar(255)   | NO            |             |
| scPutawaySuggestion              | sortMode                                          | varchar     | varchar(255)   | NO            |             |
| scRCLH                           | oid                                               | int         | int            | NO            | Primary Key |
| scRCLH                           | document_id                                       | int         | int            | NO            | Foreign Key |
| scRCLH                           | referenceNo                                       | varchar     | varchar(255)   | NO            | Foreign Key |
| scRCLH                           | site_id                                           | int         | int            | NO            | Foreign Key |
| scRCLH                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scRCLH                           | supplier_id                                       | int         | int            | NO            | Foreign Key |
| scRCLH                           | bolNumber                                         | varchar     | varchar(255)   | NO            |             |
| scRCLH                           | classoid                                          | int         | int            | NO            |             |
| scRCLH                           | completedDate                                     | datetime    | datetime       | NO            |             |
| scRCLH                           | documentNo                                        | varchar     | varchar(255)   | NO            |             |
| scRCLH                           | location_id                                       | int         | int            | NO            |             |
| scRCLH                           | owner_id                                          | int         | int            | NO            |             |
| scRCLH                           | pickTicketNo                                      | varchar     | varchar(255)   | NO            |             |
| scRCLH                           | priority                                          | varchar     | varchar(255)   | NO            |             |
| scRCLH                           | receiptDate                                       | datetime    | datetime       | NO            |             |
| scRCLH                           | receivingJob_id                                   | int         | int            | NO            |             |
| scRCLH                           | reopenedDate                                      | datetime    | datetime       | NO            |             |
| scRCLH                           | shippedDate                                       | datetime    | datetime       | NO            |             |
| scRCLH                           | type                                              | varchar     | varchar(255)   | NO            |             |
| scRCLH                           | unforecasted                                      | varchar     | varchar(10)    | NO            |             |
| scRCLH                           | user_id                                           | int         | int            | NO            |             |
| scRCLI                           | oid                                               | int         | int            | NO            | Primary Key |
| scRCLI                           | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scRCLI                           | mreq_id                                           | int         | int            | NO            | Foreign Key |
| scRCLI                           | rclh_id                                           | int         | int            | NO            | Foreign Key |
| scRCLI                           | receivedDate                                      | datetime    | datetime       | NO            | Foreign Key |
| scRCLI                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scRCLI                           | classoid                                          | int         | int            | NO            |             |
| scRCLI                           | costCenter_id                                     | int         | int            | NO            |             |
| scRCLI                           | deliverTo_id                                      | int         | int            | NO            |             |
| scRCLI                           | description                                       | varchar     | varchar(255)   | NO            |             |
| scRCLI                           | isQASample                                        | varchar     | varchar(10)    | NO            |             |
| scRCLI                           | location_id                                       | int         | int            | NO            |             |
| scRCLI                           | material_id                                       | int         | int            | NO            |             |
| scRCLI                           | parentRCLI_id                                     | int         | int            | NO            |             |
| scRCLI                           | priority                                          | varchar     | varchar(255)   | NO            |             |
| scRCLI                           | putawayJob_id                                     | int         | int            | NO            |             |
| scRCLI                           | quantity                                          | bigint      | bigint         | NO            |             |
| scRCLI                           | receivedQuantity                                  | bigint      | bigint         | NO            |             |
| scRCLI                           | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scRCLI                           | supplier_id                                       | int         | int            | NO            |             |
| scRCLI                           | uoi_id                                            | int         | int            | NO            |             |
| scRCLI                           | user_id                                           | int         | int            | NO            |             |
| scRCLIDimension                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scRCLIDimension                  | dimension_id                                      | int         | int            | NO            | Foreign Key |
| scRCLIDimension                  | rcli_id                                           | int         | int            | NO            | Foreign Key |
| scRCLIDimension                  | classoid                                          | int         | int            | NO            |             |
| scRCLIDimension                  | quantity                                          | bigint      | bigint         | NO            |             |
| scRCLIDimension                  | uoi_id                                            | int         | int            | NO            |             |
| scRack                           | oid                                               | int         | int            | NO            | Primary Key |
| scRack                           | aisle_id                                          | int         | int            | NO            | Foreign Key |
| scRack                           | allocateInventory                                 | varchar     | varchar(255)   | NO            |             |
| scRack                           | classoid                                          | int         | int            | NO            |             |
| scRack                           | lightId                                           | varchar     | varchar(255)   | NO            |             |
| scRack                           | name                                              | varchar     | varchar(255)   | NO            |             |
| scRack                           | site_id                                           | int         | int            | NO            |             |
| scRack                           | status                                            | varchar     | varchar(255)   | NO            |             |
| scRack                           | velocity                                          | varchar     | varchar(255)   | NO            |             |
| scReasonList                     | oid                                               | int         | int            | NO            | Primary Key |
| scReasonList                     | classoid                                          | int         | int            | NO            |             |
| scReasonList                     | description_id                                    | int         | int            | NO            |             |
| scReasonList                     | label_id                                          | int         | int            | NO            |             |
| scReasonList                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scReasonListItem                 | oid                                               | int         | int            | NO            | Primary Key |
| scReasonListItem                 | classoid                                          | int         | int            | NO            |             |
| scReasonListItem                 | list_id                                           | int         | int            | NO            |             |
| scReasonListItem                 | reason_id                                         | int         | int            | NO            |             |
| scReasonListItem                 | sequence                                          | int         | int            | NO            |             |
| scReceivingJob                   | oid                                               | int         | int            | NO            | Primary Key |
| scReceivingJob                   | allowMixConditionsInContainer                     | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | allowMultipleQtyReceiving                         | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | allowMultipleScanReceiving                        | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | allowOverReceiving                                | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | allowReceivingWhenMissingHandlingMaterials        | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | allowReopeningRCLH                                | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | askBOLNumberReceiving                             | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | askCommentReceiving                               | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | askCostCenterUnforcastedReceiving                 | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | askDepartmentUnforcastedReceiving                 | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | askDestinationUnforcastedReceiving                | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | askDocumentNoUnforcatedReceiving                  | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | askMultiScanCyclesReceiving                       | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | askOriginUnforcastedReceiving                     | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | askZoneForNewCOReceiving                          | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | canBeLockedByChecklist                            | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | classoid                                          | int         | int            | NO            |             |
| scReceivingJob                   | conditionChangeReasonList_id                      | int         | int            | NO            |             |
| scReceivingJob                   | consolidateReceiving                              | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | defaultItemOwner                                  | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | defaultMaterialConditionReceiving_id              | int         | int            | NO            |             |
| scReceivingJob                   | description                                       | text        | text           | NO            |             |
| scReceivingJob                   | enableTEUsageStatusWhenReceiptCompleted           | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | handlingMaterialPutawayBay_id                     | int         | int            | NO            |             |
| scReceivingJob                   | inboundLineSortOrder                              | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | inboundShowPartNumber                             | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | materialLabelRequiredOnReceiving                  | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | maximumQuantityReceiving                          | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | missingDepthWarning                               | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | missingDimensionCondition_id                      | int         | int            | NO            |             |
| scReceivingJob                   | missingHeightWarning                              | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | missingWeightWarning                              | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | missingWidthWarning                               | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | name                                              | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | noAllocatableInventoryWarning                     | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | preReceivingChecklist_id                          | int         | int            | NO            |             |
| scReceivingJob                   | printExternalBarcodeOnReceiving                   | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | printingWorkCenter_id                             | int         | int            | NO            |             |
| scReceivingJob                   | qaMaterialConditionReceiving_id                   | int         | int            | NO            |             |
| scReceivingJob                   | receiptClosureAction                              | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | receivingLabel_id                                 | int         | int            | NO            |             |
| scReceivingJob                   | receivingLocationEnforcement                      | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | receivingMode                                     | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | receivingMultipleDocument                         | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | receivingMultipleShipment                         | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | receivingPrintMaterialLabel                       | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | recGroupReceivingLines                            | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | sampleQAQuantityMode                              | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | showRelatedOrderOnReceiving                       | varchar     | varchar(10)    | NO            |             |
| scReceivingJob                   | site_id                                           | int         | int            | NO            |             |
| scReceivingJob                   | siteConfiguration_id                              | int         | int            | NO            |             |
| scReceivingJob                   | specificNoScanReceivingConsolidationMode          | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | teUsageStatusWhenReceiptCompleted                 | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | thresholdToEnableClosing                          | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | xdockMode_Opportunities                           | varchar     | varchar(255)   | NO            |             |
| scReceivingJob                   | xdockMode_SOBind                                  | varchar     | varchar(255)   | NO            |             |
| scReplenishmentJob               | oid                                               | int         | int            | NO            | Primary Key |
| scReplenishmentJob               | allowFromFixedPick                                | varchar     | varchar(10)    | NO            |             |
| scReplenishmentJob               | classoid                                          | int         | int            | NO            |             |
| scReplenishmentJob               | description                                       | text        | text           | NO            |             |
| scReplenishmentJob               | dropAction                                        | varchar     | varchar(255)   | NO            |             |
| scReplenishmentJob               | lpnQtyRoundingMode                                | varchar     | varchar(255)   | NO            |             |
| scReplenishmentJob               | mergeQuantity                                     | varchar     | varchar(10)    | NO            |             |
| scReplenishmentJob               | mergeReplenishments                               | varchar     | varchar(10)    | NO            |             |
| scReplenishmentJob               | movingJob_id                                      | int         | int            | NO            |             |
| scReplenishmentJob               | name                                              | varchar     | varchar(255)   | NO            |             |
| scReplenishmentJob               | qtyPriorityMode                                   | varchar     | varchar(255)   | NO            |             |
| scReplenishmentJob               | site_id                                           | int         | int            | NO            |             |
| scReplenishmentJob               | siteConfiguration_id                              | int         | int            | NO            |             |
| scSHLH                           | oid                                               | int         | int            | NO            | Primary Key |
| scSHLH                           | orderNo                                           | varchar     | varchar(255)   | NO            | Foreign Key |
| scSHLH                           | parent_id                                         | int         | int            | NO            | Foreign Key |
| scSHLH                           | shippedDate                                       | datetime    | datetime       | NO            | Foreign Key |
| scSHLH                           | billTo_id                                         | int         | int            | NO            |             |
| scSHLH                           | classoid                                          | int         | int            | NO            |             |
| scSHLH                           | customerOrderNo                                   | varchar     | varchar(255)   | NO            |             |
| scSHLH                           | deliveryDate                                      | datetime    | datetime       | NO            |             |
| scSHLH                           | lastAdjustment_id                                 | int         | int            | NO            |             |
| scSHLH                           | owner_id                                          | int         | int            | NO            |             |
| scSHLH                           | partitionNo                                       | int         | int            | NO            |             |
| scSHLH                           | reference_id                                      | int         | int            | NO            |             |
| scSHLH                           | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scSHLH                           | requester_id                                      | int         | int            | NO            |             |
| scSHLH                           | requiredDate                                      | datetime    | datetime       | NO            |             |
| scSHLH                           | shipFrom_id                                       | int         | int            | NO            |             |
| scSHLH                           | shipmentRequest_id                                | int         | int            | NO            |             |
| scSHLH                           | shippingServiceLevel_id                           | int         | int            | NO            |             |
| scSHLH                           | shipTo_id                                         | int         | int            | NO            |             |
| scSHLH                           | shipToAddress_id                                  | int         | int            | NO            |             |
| scSHLH                           | status                                            | varchar     | varchar(255)   | NO            |             |
| scSHLH                           | type_id                                           | int         | int            | NO            |             |
| scSHLI                           | oid                                               | int         | int            | NO            | Primary Key |
| scSHLI                           | masterShipment_id                                 | int         | int            | NO            | Foreign Key |
| scSHLI                           | pack_id                                           | int         | int            | NO            | Foreign Key |
| scSHLI                           | parent_id                                         | int         | int            | NO            | Foreign Key |
| scSHLI                           | cancelledDate                                     | varchar     | varchar(255)   | NO            |             |
| scSHLI                           | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scSHLI                           | classoid                                          | int         | int            | NO            |             |
| scSHLI                           | deliveryDate                                      | datetime    | datetime       | NO            |             |
| scSHLI                           | dimensionUOM_id                                   | int         | int            | NO            |             |
| scSHLI                           | externalOID                                       | varchar     | varchar(255)   | NO            |             |
| scSHLI                           | materialMaster_id                                 | int         | int            | NO            |             |
| scSHLI                           | orderLine_id                                      | int         | int            | NO            |             |
| scSHLI                           | owner_id                                          | int         | int            | NO            |             |
| scSHLI                           | partitionNo                                       | int         | int            | NO            |             |
| scSHLI                           | quantity                                          | bigint      | bigint         | NO            |             |
| scSHLI                           | receivedQty                                       | bigint      | bigint         | NO            |             |
| scSHLI                           | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scSHLI                           | requiredDate                                      | datetime    | datetime       | NO            |             |
| scSHLI                           | sequence                                          | varchar     | varchar(255)   | NO            |             |
| scSHLI                           | shippedDate                                       | datetime    | datetime       | NO            |             |
| scSHLI                           | shipTo_id                                         | int         | int            | NO            |             |
| scSHLI                           | shipToDepartment_id                               | int         | int            | NO            |             |
| scSHLI                           | status                                            | varchar     | varchar(255)   | NO            |             |
| scSHLI                           | supplier_id                                       | int         | int            | NO            |             |
| scSHLI                           | toReceiveQty                                      | bigint      | bigint         | NO            |             |
| scSHLI                           | uoi_id                                            | int         | int            | NO            |             |
| scSHLI                           | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scSHLI                           | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scSHLI                           | weightUOM_id                                      | int         | int            | NO            |             |
| scSHLIDimension                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scSHLIDimension                  | dimension_id                                      | int         | int            | NO            | Foreign Key |
| scSHLIDimension                  | shli_id                                           | int         | int            | NO            | Foreign Key |
| scSHLIDimension                  | classoid                                          | int         | int            | NO            |             |
| scSHLIDimension                  | partitionNo                                       | int         | int            | NO            |             |
| scSHLIDimension                  | quantity                                          | bigint      | bigint         | NO            |             |
| scSHLIDimension                  | uoi_id                                            | int         | int            | NO            |             |
| scSHLIDimension                  | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scSHLIDimension                  | weightUOM_id                                      | int         | int            | NO            |             |
| scSHLP                           | oid                                               | int         | int            | NO            | Primary Key |
| scSHLP                           | container_id                                      | int         | int            | NO            | Foreign Key |
| scSHLP                           | masterShipment_id                                 | int         | int            | NO            | Foreign Key |
| scSHLP                           | pack_id                                           | int         | int            | NO            | Foreign Key |
| scSHLP                           | parent_id                                         | int         | int            | NO            | Foreign Key |
| scSHLP                           | cancelledDate                                     | varchar     | varchar(255)   | NO            |             |
| scSHLP                           | classoid                                          | int         | int            | NO            |             |
| scSHLP                           | containerType_id                                  | int         | int            | NO            |             |
| scSHLP                           | deliveryDate                                      | datetime    | datetime       | NO            |             |
| scSHLP                           | dimensionUOM_id                                   | int         | int            | NO            |             |
| scSHLP                           | partitionNo                                       | int         | int            | NO            |             |
| scSHLP                           | sequence                                          | int         | int            | NO            |             |
| scSHLP                           | sscc                                              | varchar     | varchar(255)   | NO            |             |
| scSHLP                           | status                                            | varchar     | varchar(255)   | NO            |             |
| scSHLP                           | trackingNo                                        | varchar     | varchar(255)   | NO            |             |
| scSHLP                           | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scSHLP                           | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scSHLP                           | weightUOM_id                                      | int         | int            | NO            |             |
| scSKLH                           | oid                                               | int         | int            | NO            | Primary Key |
| scSKLH                           | cycleCount_id                                     | int         | int            | NO            | Foreign Key |
| scSKLH                           | location_id                                       | int         | int            | NO            | Foreign Key |
| scSKLH                           | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scSKLH                           | session_id                                        | int         | int            | NO            | Foreign Key |
| scSKLH                           | site_id                                           | int         | int            | NO            | Foreign Key |
| scSKLH                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scSKLH                           | aisle_id                                          | int         | int            | NO            |             |
| scSKLH                           | classoid                                          | int         | int            | NO            |             |
| scSKLH                           | completedDate                                     | datetime    | datetime       | NO            |             |
| scSKLH                           | countingMode                                      | varchar     | varchar(255)   | NO            |             |
| scSKLH                           | inconsistentAction                                | varchar     | varchar(255)   | NO            |             |
| scSKLH                           | inconsistentSKLH                                  | int         | int            | NO            |             |
| scSKLH                           | inconsistentSKLI_id                               | int         | int            | NO            |             |
| scSKLH                           | owner_id                                          | int         | int            | NO            |             |
| scSKLH                           | priority                                          | int         | int            | NO            |             |
| scSKLH                           | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scSKLH                           | startDate                                         | datetime    | datetime       | NO            |             |
| scSKLH                           | verificationDate                                  | datetime    | datetime       | NO            |             |
| scSKLH                           | verifiedByUser_id                                 | int         | int            | NO            |             |
| scSKLH                           | zone_id                                           | int         | int            | NO            |             |
| scSKLHCount                      | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scSKLHCount                      | sklh_id                                           | int         | int            | NO            | Foreign Key |
| scSKLHCount                      | batchCountType                                    | varchar     | varchar(255)   | NO            |             |
| scSKLHCount                      | classoid                                          | int         | int            | NO            |             |
| scSKLHCount                      | completedDate                                     | datetime    | datetime       | NO            |             |
| scSKLHCount                      | countedQtyItem                                    | bigint      | bigint         | NO            |             |
| scSKLHCount                      | countedQtyLPN                                     | int         | int            | NO            |             |
| scSKLHCount                      | countNo                                           | int         | int            | NO            |             |
| scSKLHCount                      | expectedQtyItem                                   | bigint      | bigint         | NO            |             |
| scSKLHCount                      | expectedQtyLPN                                    | int         | int            | NO            |             |
| scSKLHCount                      | materialMaster_id                                 | int         | int            | NO            |             |
| scSKLHCount                      | previousCount                                     | int         | int            | NO            |             |
| scSKLHCount                      | status                                            | varchar     | varchar(255)   | NO            |             |
| scSKLHCount                      | uoiConfig_id                                      | int         | int            | NO            |             |
| scSKLHCount                      | user_id                                           | int         | int            | NO            |             |
| scSKLI                           | oid                                               | int         | int            | NO            | Primary Key |
| scSKLI                           | lastCount_id                                      | int         | int            | NO            | Foreign Key |
| scSKLI                           | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scSKLI                           | parent_id                                         | int         | int            | NO            | Foreign Key |
| scSKLI                           | skli_id                                           | int         | int            | NO            | Foreign Key |
| scSKLI                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scSKLI                           | abcClass_id                                       | int         | int            | NO            |             |
| scSKLI                           | adjustedQty                                       | bigint      | bigint         | NO            |             |
| scSKLI                           | adjustedWeight                                    | decimal     | decimal(19,2)  | NO            |             |
| scSKLI                           | classoid                                          | int         | int            | NO            |             |
| scSKLI                           | condition_id                                      | int         | int            | NO            |             |
| scSKLI                           | container_id                                      | int         | int            | NO            |             |
| scSKLI                           | countAllLPOneCount                                | varchar     | varchar(10)    | NO            |             |
| scSKLI                           | countingJob_id                                    | int         | int            | NO            |             |
| scSKLI                           | dimension_id                                      | int         | int            | NO            |             |
| scSKLI                           | displayPartNo                                     | varchar     | varchar(255)   | NO            |             |
| scSKLI                           | inconsistentAction                                | varchar     | varchar(255)   | NO            |             |
| scSKLI                           | inconsistentReason                                | varchar     | varchar(255)   | NO            |             |
| scSKLI                           | inconsistentRelatedSKLI_id                        | int         | int            | NO            |             |
| scSKLI                           | label_id                                          | int         | int            | NO            |             |
| scSKLI                           | owner_id                                          | int         | int            | NO            |             |
| scSKLI                           | serialMoved                                       | varchar     | varchar(10)    | NO            |             |
| scSKLI                           | site_id                                           | int         | int            | NO            |             |
| scSKLI                           | totalCount                                        | int         | int            | NO            |             |
| scSKLI                           | uoi_id                                            | int         | int            | NO            |             |
| scSKLI                           | verificationDate                                  | datetime    | datetime       | NO            |             |
| scSKLI                           | verifiedByUser_id                                 | int         | int            | NO            |             |
| scSKLI                           | weightUOM                                         | int         | int            | NO            |             |
| scSKLICount                      | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scSKLICount                      | skli_id                                           | int         | int            | NO            | Foreign Key |
| scSKLICount                      | adjustedWeight                                    | decimal     | decimal(19,2)  | NO            |             |
| scSKLICount                      | adjustment                                        | bigint      | bigint         | NO            |             |
| scSKLICount                      | classoid                                          | int         | int            | NO            |             |
| scSKLICount                      | completedDate                                     | datetime    | datetime       | NO            |             |
| scSKLICount                      | countedQty                                        | bigint      | bigint         | NO            |             |
| scSKLICount                      | countedWeight                                     | decimal     | decimal(19,2)  | NO            |             |
| scSKLICount                      | countNo                                           | int         | int            | NO            |             |
| scSKLICount                      | expectedQty                                       | bigint      | bigint         | NO            |             |
| scSKLICount                      | expectedWeight                                    | decimal     | decimal(19,2)  | NO            |             |
| scSKLICount                      | previousCount_id                                  | int         | int            | NO            |             |
| scSKLICount                      | status                                            | varchar     | varchar(255)   | NO            |             |
| scSKLICount                      | uoi_id                                            | int         | int            | NO            |             |
| scSKLICount                      | user_id                                           | int         | int            | NO            |             |
| scSKLICount                      | weightUOM                                         | int         | int            | NO            |             |
| scSOLHReason                     | oid                                               | int         | int            | NO            | Primary Key |
| scSOLHReason                     | classoid                                          | int         | int            | NO            |             |
| scSOLHReason                     | description_id                                    | int         | int            | NO            |             |
| scSOLHReason                     | label_id                                          | int         | int            | NO            |             |
| scSOLHReason                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scSOLHReasonList                 | oid                                               | int         | int            | NO            | Primary Key |
| scSOLHReasonList                 | classoid                                          | int         | int            | NO            |             |
| scSOLHReasonList                 | description_id                                    | int         | int            | NO            |             |
| scSOLHReasonList                 | label_id                                          | int         | int            | NO            |             |
| scSOLHReasonList                 | name                                              | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | oid                                               | int         | int            | NO            | Primary Key |
| scShipmentRequest                | carrier_id                                        | int         | int            | NO            | Foreign Key |
| scShipmentRequest                | deliverByDate                                     | datetime    | datetime       | NO            | Foreign Key |
| scShipmentRequest                | deliveryNo                                        | varchar     | varchar(255)   | NO            | Foreign Key |
| scShipmentRequest                | load_id                                           | int         | int            | NO            | Foreign Key |
| scShipmentRequest                | reference_id                                      | int         | int            | NO            | Foreign Key |
| scShipmentRequest                | shipTo_id                                         | int         | int            | NO            | Foreign Key |
| scShipmentRequest                | wave_id                                           | int         | int            | NO            | Foreign Key |
| scShipmentRequest                | allocationInvPolicy_id                            | int         | int            | NO            |             |
| scShipmentRequest                | bolreport_id                                      | int         | int            | NO            |             |
| scShipmentRequest                | broker_id                                         | int         | int            | NO            |             |
| scShipmentRequest                | callDeliveryAppointment                           | varchar     | varchar(10)    | NO            |             |
| scShipmentRequest                | cancelByDate                                      | datetime    | datetime       | NO            |             |
| scShipmentRequest                | carrierBillAccount                                | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | carrierDeliveryOption                             | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | carrierShippingInsurance                          | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | classoid                                          | int         | int            | NO            |             |
| scShipmentRequest                | codAmount                                         | decimal     | decimal(19,2)  | NO            |             |
| scShipmentRequest                | creationDate                                      | datetime    | datetime       | NO            |             |
| scShipmentRequest                | freightTerms_id                                   | int         | int            | NO            |             |
| scShipmentRequest                | ignoreAddressValidation                           | varchar     | varchar(10)    | NO            |             |
| scShipmentRequest                | insideDelivery                                    | varchar     | varchar(10)    | NO            |             |
| scShipmentRequest                | liftGate                                          | varchar     | varchar(10)    | NO            |             |
| scShipmentRequest                | loadingDock                                       | varchar     | varchar(10)    | NO            |             |
| scShipmentRequest                | name                                              | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | packingSlip_id                                    | int         | int            | NO            |             |
| scShipmentRequest                | partitionNo                                       | int         | int            | NO            |             |
| scShipmentRequest                | pickByDate                                        | datetime    | datetime       | NO            |             |
| scShipmentRequest                | plannedShippingCost                               | decimal     | decimal(19,2)  | NO            |             |
| scShipmentRequest                | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | releaseDate                                       | datetime    | datetime       | NO            |             |
| scShipmentRequest                | requestDate                                       | datetime    | datetime       | NO            |             |
| scShipmentRequest                | requester_id                                      | int         | int            | NO            |             |
| scShipmentRequest                | route_id                                          | int         | int            | NO            |             |
| scShipmentRequest                | routingGuide                                      | varchar     | varchar(10)    | NO            |             |
| scShipmentRequest                | serviceLevel_id                                   | int         | int            | NO            |             |
| scShipmentRequest                | shipByDate                                        | datetime    | datetime       | NO            |             |
| scShipmentRequest                | shipFrom_id                                       | int         | int            | NO            |             |
| scShipmentRequest                | shipFromAddress_id                                | int         | int            | NO            |             |
| scShipmentRequest                | shipFromContact_id                                | int         | int            | NO            |             |
| scShipmentRequest                | shipFromName                                      | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | shipFromPhoneNo                                   | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | shippingIssurance                                 | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | shipToAddress_id                                  | int         | int            | NO            |             |
| scShipmentRequest                | shipToContact_id                                  | int         | int            | NO            |             |
| scShipmentRequest                | shipToLocation_id                                 | int         | int            | NO            |             |
| scShipmentRequest                | shipToName                                        | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | shipToPhoneNo                                     | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | shipToZone_id                                     | int         | int            | NO            |             |
| scShipmentRequest                | shipVia_id                                        | int         | int            | NO            |             |
| scShipmentRequest                | shipViaAddress_id                                 | int         | int            | NO            |             |
| scShipmentRequest                | shipViaContact_id                                 | int         | int            | NO            |             |
| scShipmentRequest                | shipViaName                                       | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | status                                            | varchar     | varchar(255)   | NO            |             |
| scShipmentRequest                | thirdPartyFreight_id                              | int         | int            | NO            |             |
| scShipmentRequest                | type_id                                           | int         | int            | NO            |             |
| scShipmentRequest                | workCenter_id                                     | int         | int            | NO            |             |
| scShipmentRequest                | workCenterType_id                                 | int         | int            | NO            |             |
| scShipmentType                   | oid                                               | int         | int            | NO            | Primary Key |
| scShipmentType                   | canBeLockedByChecklist                            | varchar     | varchar(255)   | NO            |             |
| scShipmentType                   | classoid                                          | int         | int            | NO            |             |
| scShipmentType                   | creationMode                                      | varchar     | varchar(255)   | NO            |             |
| scShipmentType                   | description                                       | varchar     | varchar(255)   | NO            |             |
| scShipmentType                   | enableTEUsageStatusWhenReceiptCompleted           | varchar     | varchar(255)   | NO            |             |
| scShipmentType                   | name                                              | varchar     | varchar(255)   | NO            |             |
| scShipmentType                   | preReceivingChecklist_id                          | int         | int            | NO            |             |
| scShipmentType                   | receiptClosureAction                              | varchar     | varchar(255)   | NO            |             |
| scShipmentType                   | status                                            | varchar     | varchar(255)   | NO            |             |
| scShipmentType                   | teUsageStatusWhenReceiptCompleted                 | varchar     | varchar(255)   | NO            |             |
| scShippingJob                    | oid                                               | int         | int            | NO            | Primary Key |
| scShippingJob                    | bolQty                                            | int         | int            | NO            |             |
| scShippingJob                    | classoid                                          | int         | int            | NO            |             |
| scShippingJob                    | description                                       | text        | text           | NO            |             |
| scShippingJob                    | name                                              | varchar     | varchar(255)   | NO            |             |
| scShippingJob                    | packingSlip_id                                    | int         | int            | NO            |             |
| scShippingJob                    | packingSlipQty                                    | int         | int            | NO            |             |
| scShippingJob                    | site_id                                           | int         | int            | NO            |             |
| scShippingJob                    | siteConfiguration_id                              | int         | int            | NO            |             |
| scShippingJob                    | weightCapture                                     | varchar     | varchar(255)   | NO            |             |
| scShippingServiceLevel           | oid                                               | int         | int            | NO            | Primary Key |
| scShippingServiceLevel           | carrier_id                                        | int         | int            | NO            |             |
| scShippingServiceLevel           | classoid                                          | int         | int            | NO            |             |
| scShippingServiceLevel           | code                                              | varchar     | varchar(255)   | NO            |             |
| scShippingServiceLevel           | name                                              | varchar     | varchar(255)   | NO            |             |
| scShippingServiceLevel           | overrideShippableRule                             | varchar     | varchar(255)   | NO            |             |
| scShippingServiceLevel           | tmsCode                                           | varchar     | varchar(255)   | NO            |             |
| scShippingServiceLevel           | Type                                              | varchar     | varchar(255)   | NO            |             |
| scSite                           | oid                                               | int         | int            | NO            | Primary Key |
| scSite                           | accountNo                                         | varchar     | varchar(255)   | NO            | Foreign Key |
| scSite                           | gln                                               | varchar     | varchar(255)   | NO            | Foreign Key |
| scSite                           | language_id                                       | int         | int            | NO            | Foreign Key |
| scSite                           | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scSite                           | primaryContact_id                                 | int         | int            | NO            | Foreign Key |
| scSite                           | siteType_id                                       | int         | int            | NO            | Foreign Key |
| scSite                           | address_id                                        | int         | int            | NO            |             |
| scSite                           | asn_Dept                                          | varchar     | varchar(255)   | NO            |             |
| scSite                           | asn_Store                                         | varchar     | varchar(255)   | NO            |             |
| scSite                           | asnEnable                                         | varchar     | varchar(10)    | NO            |             |
| scSite                           | asnNbPalletLAbel                                  | int         | int            | NO            |             |
| scSite                           | banner                                            | varchar     | varchar(255)   | NO            |             |
| scSite                           | bannerGroup                                       | varchar     | varchar(255)   | NO            |             |
| scSite                           | carrierType                                       | varchar     | varchar(255)   | NO            |             |
| scSite                           | classoid                                          | int         | int            | NO            |             |
| scSite                           | createStamp                                       | datetime    | datetime       | NO            |             |
| scSite                           | createUser_id                                     | int         | int            | NO            |             |
| scSite                           | currency_id                                       | int         | int            | NO            |             |
| scSite                           | departmentNo                                      | varchar     | varchar(255)   | NO            |             |
| scSite                           | displayName                                       | varchar     | varchar(255)   | NO            |             |
| scSite                           | dunsNo                                            | varchar     | varchar(255)   | NO            |             |
| scSite                           | email                                             | varchar     | varchar(255)   | NO            |             |
| scSite                           | externalType                                      | varchar     | varchar(255)   | NO            |             |
| scSite                           | family                                            | varchar     | varchar(255)   | NO            |             |
| scSite                           | faxNo                                             | varchar     | varchar(255)   | NO            |             |
| scSite                           | freightCode                                       | varchar     | varchar(255)   | NO            |             |
| scSite                           | geoZone                                           | varchar     | varchar(255)   | NO            |             |
| scSite                           | gs1_Company_Prefix                                | varchar     | varchar(255)   | NO            |             |
| scSite                           | overrideShippableRule                             | varchar     | varchar(255)   | NO            |             |
| scSite                           | parent_id                                         | int         | int            | NO            |             |
| scSite                           | phoneNo                                           | varchar     | varchar(255)   | NO            |             |
| scSite                           | scac                                              | varchar     | varchar(255)   | NO            |             |
| scSite                           | status                                            | varchar     | varchar(255)   | NO            |             |
| scSite                           | storeNo                                           | varchar     | varchar(255)   | NO            |             |
| scSite                           | storeNumber                                       | varchar     | varchar(255)   | NO            |             |
| scSite                           | taxIdentificationNo                               | varchar     | varchar(255)   | NO            |             |
| scSite                           | updateStamp                                       | datetime    | datetime       | NO            |             |
| scSite                           | updateUser_id                                     | int         | int            | NO            |             |
| scSite                           | webSite                                           | varchar     | varchar(255)   | NO            |             |
| scSiteConfiguration              | oid                                               | int         | int            | NO            | Primary Key |
| scSiteConfiguration              | site_id                                           | int         | int            | NO            | Foreign Key |
| scSiteConfiguration              | accountNo                                         | varchar     | varchar(255)   | NO            |             |
| scSiteConfiguration              | allocationInvPolicy_id                            | int         | int            | NO            |             |
| scSiteConfiguration              | allocationJob_id                                  | int         | int            | NO            |             |
| scSiteConfiguration              | allowNumericLocationAlias                         | varchar     | varchar(10)    | NO            |             |
| scSiteConfiguration              | bigDecimalTolerance                               | varchar     | varchar(255)   | NO            |             |
| scSiteConfiguration              | calendarOptions_id                                | int         | int            | NO            |             |
| scSiteConfiguration              | classoid                                          | int         | int            | NO            |             |
| scSiteConfiguration              | consolidationJob_id                               | int         | int            | NO            |             |
| scSiteConfiguration              | countingJob_id                                    | int         | int            | NO            |             |
| scSiteConfiguration              | deliveryJob_id                                    | int         | int            | NO            |             |
| scSiteConfiguration              | dimensionUOM_id                                   | int         | int            | NO            |             |
| scSiteConfiguration              | isContainerTracking                               | varchar     | varchar(10)    | NO            |             |
| scSiteConfiguration              | itemConfiguration_id                              | int         | int            | NO            |             |
| scSiteConfiguration              | loadingJob_id                                     | int         | int            | NO            |             |
| scSiteConfiguration              | manufacturingJob_id                               | int         | int            | NO            |             |
| scSiteConfiguration              | maxGenericCOLabelToPrint                          | varchar     | varchar(255)   | NO            |             |
| scSiteConfiguration              | maxGenericMILabelToPrint                          | varchar     | varchar(255)   | NO            |             |
| scSiteConfiguration              | movingJob_id                                      | int         | int            | NO            |             |
| scSiteConfiguration              | name                                              | varchar     | varchar(255)   | NO            |             |
| scSiteConfiguration              | orderLineSequenceMode                             | varchar     | varchar(255)   | NO            |             |
| scSiteConfiguration              | packingJob_id                                     | int         | int            | NO            |             |
| scSiteConfiguration              | parent_id                                         | int         | int            | NO            |             |
| scSiteConfiguration              | pickingJob_id                                     | int         | int            | NO            |             |
| scSiteConfiguration              | putawayJob_id                                     | int         | int            | NO            |             |
| scSiteConfiguration              | receivingJob_id                                   | int         | int            | NO            |             |
| scSiteConfiguration              | replenishmentJob_id                               | int         | int            | NO            |             |
| scSiteConfiguration              | shippingJob_id                                    | int         | int            | NO            |             |
| scSiteConfiguration              | temperatureUOM_id                                 | int         | int            | NO            |             |
| scSiteConfiguration              | unloadingJob_id                                   | int         | int            | NO            |             |
| scSiteConfiguration              | weightUOM_id                                      | int         | int            | NO            |             |
| scSiteConfiguration              | zoneSequencing                                    | varchar     | varchar(255)   | NO            |             |
| scSiteOrderType                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scSiteOrderType                  | site_id                                           | int         | int            | NO            | Foreign Key |
| scSiteOrderType                  | classoid                                          | int         | int            | NO            |             |
| scSiteOrderType                  | defaultSOLIPriority                               | varchar     | varchar(255)   | NO            |             |
| scSiteOrderType                  | orderType_id                                      | int         | int            | NO            |             |
| scSiteOrderType                  | policy_id                                         | int         | int            | NO            |             |
| scSiteOrderType                  | receivingJob_id                                   | int         | int            | NO            |             |
| scSiteOrderType                  | wavingJob_id                                      | int         | int            | NO            |             |
| scSiteType                       | oid                                               | int         | int            | NO            | Primary Key |
| scSiteType                       | billingCustomer                                   | varchar     | varchar(10)    | NO            |             |
| scSiteType                       | billingLocation                                   | varchar     | varchar(10)    | NO            |             |
| scSiteType                       | broker                                            | varchar     | varchar(255)   | NO            |             |
| scSiteType                       | classoid                                          | int         | int            | NO            |             |
| scSiteType                       | customer                                          | varchar     | varchar(255)   | NO            |             |
| scSiteType                       | description                                       | text        | text           | NO            |             |
| scSiteType                       | displayName                                       | varchar     | varchar(255)   | NO            |             |
| scSiteType                       | hasUsers                                          | varchar     | varchar(10)    | NO            |             |
| scSiteType                       | internal                                          | varchar     | varchar(255)   | NO            |             |
| scSiteType                       | name                                              | varchar     | varchar(255)   | NO            |             |
| scSiteType                       | owner                                             | varchar     | varchar(10)    | NO            |             |
| scSiteType                       | status                                            | varchar     | varchar(255)   | NO            |             |
| scSiteType                       | type                                              | varchar     | varchar(255)   | NO            |             |
| scSiteType                       | vendor                                            | varchar     | varchar(255)   | NO            |             |
| scSiteWorkOrderType              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scSiteWorkOrderType              | site_id                                           | int         | int            | NO            | Foreign Key |
| scSiteWorkOrderType              | workOrderType_id                                  | int         | int            | NO            | Foreign Key |
| scSiteWorkOrderType              | classoid                                          | int         | int            | NO            |             |
| scSiteWorkOrderType              | manufacturingJob_id                               | int         | int            | NO            |             |
| scSnapshotConfiguration          | oid                                               | int         | int            | NO            | Primary Key |
| scSnapshotConfiguration          | classoid                                          | int         | int            | NO            |             |
| scSnapshotConfiguration          | description                                       | text        | text           | NO            |             |
| scSnapshotConfiguration          | locationType                                      | varchar     | varchar(255)   | NO            |             |
| scSnapshotConfiguration          | name                                              | varchar     | varchar(255)   | NO            |             |
| scSnapshotConfiguration          | owner_id                                          | int         | int            | NO            |             |
| scSnapshotConfiguration          | schedule_id                                       | int         | int            | NO            |             |
| scSnapshotConfiguration          | site_id                                           | int         | int            | NO            |             |
| scSnapshotConfiguration          | status                                            | varchar     | varchar(255)   | NO            |             |
| scSnapshotLevel                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scSnapshotLevel                  | classoid                                          | int         | int            | NO            |             |
| scSnapshotLevel                  | configuration_id                                  | int         | int            | NO            |             |
| scSnapshotLevel                  | sequence                                          | int         | int            | NO            |             |
| scSnapshotLevel                  | type                                              | varchar     | varchar(255)   | NO            |             |
| scSnapshotSchedule               | oid                                               | int         | int            | NO            | Primary Key |
| scSnapshotSchedule               | classoid                                          | int         | int            | NO            |             |
| scSnapshotSchedule               | description                                       | text        | text           | NO            |             |
| scSnapshotSchedule               | frequency_id                                      | int         | int            | NO            |             |
| scSnapshotSchedule               | name                                              | varchar     | varchar(255)   | NO            |             |
| scSnapshotSchedule               | scheduler_id                                      | int         | int            | NO            |             |
| scSnapshotSchedule               | status                                            | varchar     | varchar(255)   | NO            |             |
| scSnapshotSession                | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scSnapshotSession                | classoid                                          | int         | int            | NO            |             |
| scSnapshotSession                | completedDate                                     | datetime    | datetime       | NO            |             |
| scSnapshotSession                | configuration_id                                  | int         | int            | NO            |             |
| scSnapshotSession                | creationDate                                      | datetime    | datetime       | NO            |             |
| scSnapshotSession                | itemCount                                         | int         | int            | NO            |             |
| scSnapshotSession                | status                                            | varchar     | varchar(255)   | NO            |             |
| scSnapshotSession                | user_id                                           | int         | int            | NO            |             |
| scStandbyLPN                     | oid                                               | int         | int            | NO            | Primary Key |
| scStandbyLPN                     | lpn                                               | varchar     | varchar(255)   | NO            | Foreign Key |
| scStandbyLPN                     | active                                            | varchar     | varchar(10)    | NO            |             |
| scStandbyLPN                     | classoid                                          | int         | int            | NO            |             |
| scStandbyLPN                     | containerCode                                     | varchar     | varchar(255)   | NO            |             |
| scStandbyLPN                     | creationTime                                      | datetime    | datetime       | NO            |             |
| scStandbyLPN                     | expiryDate                                        | datetime    | datetime       | NO            |             |
| scStandbyLPN                     | filler                                            | varchar     | varchar(255)   | NO            |             |
| scStandbyLPN                     | lotNo                                             | varchar     | varchar(255)   | NO            |             |
| scStandbyLPN                     | materialMaster_id                                 | int         | int            | NO            |             |
| scStandbyLPN                     | palletNo                                          | varchar     | varchar(255)   | NO            |             |
| scStandbyLPN                     | productionDate                                    | datetime    | datetime       | NO            |             |
| scStandbyLPN                     | productionRun                                     | varchar     | varchar(255)   | NO            |             |
| scStandbyLPN                     | productionSite_id                                 | int         | int            | NO            |             |
| scStandbyLPN                     | quantity                                          | bigint      | bigint         | NO            |             |
| scStandbyLPN                     | receptionDate                                     | datetime    | datetime       | NO            |             |
| scStandbyLPN                     | uoi_id                                            | int         | int            | NO            |             |
| scStandbyLPN                     | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scStandbyLPNToSOLI               | oid                                               | int         | int            | NO            | Primary Key |
| scStandbyLPNToSOLI               | classoid                                          | int         | int            | NO            |             |
| scStandbyLPNToSOLI               | quantity                                          | bigint      | bigint         | NO            |             |
| scStandbyLPNToSOLI               | soli                                              | int         | int            | NO            |             |
| scStandbyLPNToSOLI               | standbylpn_id                                     | int         | int            | NO            |             |
| scStandbyLPNToSOLI               | uoi_id                                            | int         | int            | NO            |             |
| scStockCountSchedule             | oid                                               | int         | int            | NO            | Primary Key |
| scStockCountSchedule             | classoid                                          | int         | int            | NO            |             |
| scStockCountSchedule             | description                                       | text        | text           | NO            |             |
| scStockCountSchedule             | frequency_id                                      | int         | int            | NO            |             |
| scStockCountSchedule             | name                                              | varchar     | varchar(255)   | NO            |             |
| scStockCountSchedule             | scheduler_id                                      | int         | int            | NO            |             |
| scStockCountSchedule             | status                                            | varchar     | varchar(255)   | NO            |             |
| scSubAssembly                    | oid                                               | int         | int            | NO            | Primary Key |
| scSubAssembly                    | assembly_id                                       | int         | int            | NO            | Foreign Key |
| scSubAssembly                    | classoid                                          | int         | int            | NO            |             |
| scSubAssembly                    | item_id                                           | int         | int            | NO            |             |
| scSubAssembly                    | name                                              | varchar     | varchar(255)   | NO            |             |
| scSubAssembly                    | sequence                                          | int         | int            | NO            |             |
| scTransportEquipment             | oid                                               | int         | int            | NO            | Primary Key |
| scTransportEquipment             | load_id                                           | int         | int            | NO            | Foreign Key |
| scTransportEquipment             | location_id                                       | int         | int            | NO            | Foreign Key |
| scTransportEquipment             | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scTransportEquipment             | site_id                                           | int         | int            | NO            | Foreign Key |
| scTransportEquipment             | type_id                                           | int         | int            | NO            | Foreign Key |
| scTransportEquipment             | capacity                                          | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipment             | capacityUsed                                      | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipment             | classoid                                          | int         | int            | NO            |             |
| scTransportEquipment             | currentPKLH_id                                    | int         | int            | NO            |             |
| scTransportEquipment             | dimensionUOM_id                                   | int         | int            | NO            |             |
| scTransportEquipment             | items                                             | int         | int            | NO            |             |
| scTransportEquipment             | lastUsageComment                                  | text        | text           | NO            |             |
| scTransportEquipment             | lastUsageDate                                     | datetime    | datetime       | NO            |             |
| scTransportEquipment             | lastUsageMovement_id                              | int         | int            | NO            |             |
| scTransportEquipment             | licenseNo                                         | varchar     | varchar(255)   | NO            |             |
| scTransportEquipment             | maxWeight                                         | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipment             | parent_id                                         | int         | int            | NO            |             |
| scTransportEquipment             | status                                            | varchar     | varchar(255)   | NO            |             |
| scTransportEquipment             | transportEquipment_id                             | int         | int            | NO            |             |
| scTransportEquipment             | usageStatus                                       | varchar     | varchar(255)   | NO            |             |
| scTransportEquipment             | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipment             | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipment             | weightUOM_id                                      | int         | int            | NO            |             |
| scTransportEquipment             | zone_id                                           | int         | int            | NO            |             |
| scTransportEquipmentType         | oid                                               | int         | int            | NO            | Primary Key |
| scTransportEquipmentType         | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scTransportEquipmentType         | capacity                                          | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipmentType         | classoid                                          | int         | int            | NO            |             |
| scTransportEquipmentType         | description                                       | text        | text           | NO            |             |
| scTransportEquipmentType         | dimensionUOM_id                                   | int         | int            | NO            |             |
| scTransportEquipmentType         | interiorDepth                                     | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipmentType         | interiorHeight                                    | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipmentType         | interiorWidth                                     | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipmentType         | maxPallets                                        | int         | int            | NO            |             |
| scTransportEquipmentType         | maxWeight                                         | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipmentType         | status                                            | varchar     | varchar(255)   | NO            |             |
| scTransportEquipmentType         | type                                              | varchar     | varchar(255)   | NO            |             |
| scTransportEquipmentType         | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scTransportEquipmentType         | weightUOM_id                                      | int         | int            | NO            |             |
| scUKLI                           | oid                                               | int         | int            | NO            | Primary Key |
| scUKLI                           | mi_id                                             | int         | int            | NO            | Foreign Key |
| scUKLI                           | classoid                                          | int         | int            | NO            |             |
| scUKLI                           | createdDate                                       | datetime    | datetime       | NO            |             |
| scUKLI                           | initialQty                                        | bigint      | bigint         | NO            |             |
| scUKLI                           | location_id                                       | int         | int            | NO            |             |
| scUKLI                           | pkli_id                                           | int         | int            | NO            |             |
| scUKLI                           | site_id                                           | int         | int            | NO            |             |
| scUKLI                           | status                                            | varchar     | varchar(255)   | NO            |             |
| scUKLI                           | unpickedDate                                      | datetime    | datetime       | NO            |             |
| scUKLI                           | unpickedQty                                       | bigint      | bigint         | NO            |             |
| scUKLI                           | uoi_id                                            | int         | int            | NO            |             |
| scUKLI                           | user_id                                           | int         | int            | NO            |             |
| scUOI                            | oid                                               | int         | int            | NO            | Primary Key |
| scUOI                            | classoid                                          | int         | int            | NO            |             |
| scUOI                            | description                                       | text        | text           | NO            |             |
| scUOI                            | description_id                                    | int         | int            | NO            |             |
| scUOI                            | name                                              | varchar     | varchar(255)   | NO            |             |
| scUOI                            | name_id                                           | int         | int            | NO            |             |
| scUOI                            | uom_id                                            | int         | int            | NO            |             |
| scUOIConfig                      | oid                                               | int         | int            | NO            | Primary Key |
| scUOIConfig                      | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scUOIConfig                      | classoid                                          | int         | int            | NO            |             |
| scUOIConfig                      | depth                                             | decimal     | decimal(19,2)  | NO            |             |
| scUOIConfig                      | description                                       | varchar     | varchar(255)   | NO            |             |
| scUOIConfig                      | dimensionUOM_id                                   | int         | int            | NO            |             |
| scUOIConfig                      | displayName                                       | varchar     | varchar(255)   | NO            |             |
| scUOIConfig                      | handlingMaterial_id                               | int         | int            | NO            |             |
| scUOIConfig                      | height                                            | decimal     | decimal(19,2)  | NO            |             |
| scUOIConfig                      | inactiveDate                                      | varchar     | varchar(255)   | NO            |             |
| scUOIConfig                      | lastUpdated                                       | datetime    | datetime       | NO            |             |
| scUOIConfig                      | name                                              | varchar     | varchar(255)   | NO            |             |
| scUOIConfig                      | parent_id                                         | int         | int            | NO            |             |
| scUOIConfig                      | pickingLayer                                      | int         | int            | NO            |             |
| scUOIConfig                      | pickrule                                          | varchar     | varchar(255)   | NO            |             |
| scUOIConfig                      | quantity                                          | bigint      | bigint         | NO            |             |
| scUOIConfig                      | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scUOIConfig                      | status                                            | varchar     | varchar(255)   | NO            |             |
| scUOIConfig                      | uoi_id                                            | int         | int            | NO            |             |
| scUOIConfig                      | volume                                            | decimal     | decimal(19,2)  | NO            |             |
| scUOIConfig                      | volumetryBinding                                  | varchar     | varchar(255)   | NO            |             |
| scUOIConfig                      | weight                                            | decimal     | decimal(19,2)  | NO            |             |
| scUOIConfig                      | weightUOM_id                                      | int         | int            | NO            |             |
| scUOIConfig                      | width                                             | decimal     | decimal(19,2)  | NO            |             |
| scUOIConfigLocation              | oid                                               | int         | int            | NO            | Primary Key |
| scUOIConfigLocation              | uoiconfig_id                                      | int         | int            | NO            | Foreign Key |
| scUOIConfigLocation              | active                                            | varchar     | varchar(10)    | NO            |             |
| scUOIConfigLocation              | agropur_movingMaxQty                              | bigint      | bigint         | NO            |             |
| scUOIConfigLocation              | agropur_movingMinQty                              | bigint      | bigint         | NO            |             |
| scUOIConfigLocation              | allowreslot                                       | varchar     | varchar(10)    | NO            |             |
| scUOIConfigLocation              | binType_id                                        | int         | int            | NO            |             |
| scUOIConfigLocation              | classoid                                          | int         | int            | NO            |             |
| scUOIConfigLocation              | condition_id                                      | int         | int            | NO            |             |
| scUOIConfigLocation              | inPriority                                        | int         | int            | NO            |             |
| scUOIConfigLocation              | itemTemplateUOIConfigLocation_id                  | int         | int            | NO            |             |
| scUOIConfigLocation              | lastReplenCount                                   | datetime    | datetime       | NO            |             |
| scUOIConfigLocation              | location_id                                       | int         | int            | NO            |             |
| scUOIConfigLocation              | manuallyChanged                                   | varchar     | varchar(10)    | NO            |             |
| scUOIConfigLocation              | maxLocationInZone                                 | int         | int            | NO            |             |
| scUOIConfigLocation              | maxNbDay                                          | int         | int            | NO            |             |
| scUOIConfigLocation              | maxNumberOfLicencePlates                          | int         | int            | NO            |             |
| scUOIConfigLocation              | maxPickQty                                        | bigint      | bigint         | NO            |             |
| scUOIConfigLocation              | movingMaxQty                                      | decimal     | decimal(19,2)  | NO            |             |
| scUOIConfigLocation              | movingMinQty                                      | decimal     | decimal(19,2)  | NO            |             |
| scUOIConfigLocation              | outPriority                                       | int         | int            | NO            |             |
| scUOIConfigLocation              | owner_id                                          | int         | int            | NO            |             |
| scUOIConfigLocation              | replenCountFrequency                              | varchar     | varchar(255)   | NO            |             |
| scUOIConfigLocation              | repQty                                            | bigint      | bigint         | NO            |             |
| scUOIConfigLocation              | repTresholdQty                                    | bigint      | bigint         | NO            |             |
| scUOIConfigLocation              | site_id                                           | int         | int            | NO            |             |
| scUOIConfigLocation              | type                                              | varchar     | varchar(255)   | NO            |             |
| scUOIConfigLocation              | zone_id                                           | int         | int            | NO            |             |
| scUOM                            | oid                                               | int         | int            | NO            | Primary Key |
| scUOM                            | classoid                                          | int         | int            | NO            |             |
| scUOM                            | description                                       | varchar     | varchar(255)   | NO            |             |
| scUOM                            | name                                              | varchar     | varchar(255)   | NO            |             |
| scUOM                            | type                                              | varchar     | varchar(255)   | NO            |             |
| scUnloadingJob                   | oid                                               | int         | int            | NO            | Primary Key |
| scUnloadingJob                   | site_id                                           | int         | int            | NO            | Foreign Key |
| scUnloadingJob                   | classoid                                          | int         | int            | NO            |             |
| scUnloadingJob                   | description                                       | text        | text           | NO            |             |
| scUnloadingJob                   | name                                              | varchar     | varchar(255)   | NO            |             |
| scUnloadingJob                   | siteConfiguration_id                              | int         | int            | NO            |             |
| scUnloadingJob                   | status                                            | varchar     | varchar(255)   | NO            |             |
| scUnloadingJob                   | unloadingChecklist_id                             | int         | int            | NO            |             |
| scUnloadingJob                   | unloadingCondition_id                             | int         | int            | NO            |             |
| scUserSite                       | oid                                               | int         | int            | NO            | Primary Key |
| scUserSite                       | classoid                                          | int         | int            | NO            |             |
| scUserSite                       | site_id                                           | int         | int            | NO            |             |
| scUserSite                       | user_id                                           | int         | int            | NO            |             |
| scVendorRelation                 | oid                                               | int         | int            | NO            | Primary Key |
| scVendorRelation                 | receiver_id                                       | int         | int            | NO            | Foreign Key |
| scVendorRelation                 | vendor_id                                         | int         | int            | NO            | Foreign Key |
| scVendorRelation                 | checklistInbound                                  | int         | int            | NO            |             |
| scVendorRelation                 | checklistInboundByItem                            | int         | int            | NO            |             |
| scVendorRelation                 | checklistInboundByLOTNO                           | int         | int            | NO            |             |
| scVendorRelation                 | checklistInboundByReceivingDocument               | int         | int            | NO            |             |
| scVendorRelation                 | classoid                                          | int         | int            | NO            |             |
| scVendorRelation                 | name                                              | varchar     | varchar(255)   | NO            |             |
| scVendorRelation                 | vendorNo                                          | varchar     | varchar(255)   | NO            |             |
| scWMAsset                        | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scWMAsset                        | map_id                                            | int         | int            | NO            | Foreign Key |
| scWMAsset                        | absPositionX                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | absPositionY                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | absPositionZ                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | absRotationX                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | absRotationY                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | absRotationZ                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | assetClass                                        | varchar     | varchar(255)   | NO            |             |
| scWMAsset                        | assetKey                                          | char        | char(36)       | NO            |             |
| scWMAsset                        | centerPositionX                                   | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | centerPositionY                                   | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | centerPositionZ                                   | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | classoid                                          | int         | int            | NO            |             |
| scWMAsset                        | color_id                                          | int         | int            | NO            |             |
| scWMAsset                        | depth                                             | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | floor_id                                          | int         | int            | NO            |             |
| scWMAsset                        | height                                            | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | name                                              | varchar     | varchar(255)   | NO            |             |
| scWMAsset                        | parameters                                        | text        | text           | NO            |             |
| scWMAsset                        | parent_id                                         | int         | int            | NO            |             |
| scWMAsset                        | reference_id                                      | int         | int            | NO            |             |
| scWMAsset                        | relPositionX                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | relPositionY                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | relPositionZ                                      | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | rotationX                                         | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | rotationY                                         | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | rotationZ                                         | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | thickness                                         | decimal     | decimal(19,2)  | NO            |             |
| scWMAsset                        | type_id                                           | int         | int            | NO            |             |
| scWMAsset                        | velocity                                          | int         | int            | NO            |             |
| scWMAsset                        | width                                             | decimal     | decimal(19,2)  | NO            |             |
| scWMAssetType                    | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scWMAssetType                    | assetClass                                        | varchar     | varchar(255)   | NO            |             |
| scWMAssetType                    | assetId                                           | varchar     | varchar(255)   | NO            |             |
| scWMAssetType                    | classoid                                          | int         | int            | NO            |             |
| scWMAssetType                    | color_id                                          | int         | int            | NO            |             |
| scWMAssetType                    | depth                                             | decimal     | decimal(19,2)  | NO            |             |
| scWMAssetType                    | height                                            | decimal     | decimal(19,2)  | NO            |             |
| scWMAssetType                    | name                                              | varchar     | varchar(255)   | NO            |             |
| scWMAssetType                    | width                                             | decimal     | decimal(19,2)  | NO            |             |
| scWOH                            | oid                                               | int         | int            | NO            | Primary Key |
| scWOH                            | actionRequired                                    | text        | text           | NO            |             |
| scWOH                            | assembly_id                                       | int         | int            | NO            |             |
| scWOH                            | billToCostCenter_id                               | int         | int            | NO            |             |
| scWOH                            | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scWOH                            | classoid                                          | int         | int            | NO            |             |
| scWOH                            | description                                       | text        | text           | NO            |             |
| scWOH                            | duration                                          | int         | int            | NO            |             |
| scWOH                            | earliest                                          | datetime    | datetime       | NO            |             |
| scWOH                            | lastAdjustment_id                                 | int         | int            | NO            |             |
| scWOH                            | leadingStatus                                     | varchar     | varchar(255)   | NO            |             |
| scWOH                            | materialMaster_id                                 | int         | int            | NO            |             |
| scWOH                            | orderClass                                        | varchar     | varchar(255)   | NO            |             |
| scWOH                            | owner_id                                          | int         | int            | NO            |             |
| scWOH                            | parent_id                                         | int         | int            | NO            |             |
| scWOH                            | percentComplete                                   | varchar     | varchar(255)   | NO            |             |
| scWOH                            | pickTicketNo                                      | varchar     | varchar(255)   | NO            |             |
| scWOH                            | plannedEnd                                        | datetime    | datetime       | NO            |             |
| scWOH                            | plannedStart                                      | datetime    | datetime       | NO            |             |
| scWOH                            | priority                                          | varchar     | varchar(255)   | NO            |             |
| scWOH                            | productionQty                                     | bigint      | bigint         | NO            |             |
| scWOH                            | productionRoute_id                                | int         | int            | NO            |             |
| scWOH                            | productionType                                    | varchar     | varchar(255)   | NO            |             |
| scWOH                            | quantity                                          | bigint      | bigint         | NO            |             |
| scWOH                            | receivedQty                                       | bigint      | bigint         | NO            |             |
| scWOH                            | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scWOH                            | requester_id                                      | int         | int            | NO            |             |
| scWOH                            | requiredDate                                      | datetime    | datetime       | NO            |             |
| scWOH                            | seqChildren                                       | varchar     | varchar(255)   | NO            |             |
| scWOH                            | shippedDate                                       | datetime    | datetime       | NO            |             |
| scWOH                            | shipTo_id                                         | int         | int            | NO            |             |
| scWOH                            | slack                                             | int         | int            | NO            |             |
| scWOH                            | status                                            | varchar     | varchar(255)   | NO            |             |
| scWOH                            | supplier_id                                       | int         | int            | NO            |             |
| scWOH                            | toReceiveQty                                      | bigint      | bigint         | NO            |             |
| scWOH                            | trailingStatus                                    | varchar     | varchar(255)   | NO            |             |
| scWOH                            | type_id                                           | int         | int            | NO            |             |
| scWOH                            | unitPrice                                         | varchar     | varchar(255)   | NO            |             |
| scWOH                            | uoi_id                                            | int         | int            | NO            |             |
| scWOH                            | womh_id                                           | int         | int            | NO            |             |
| scWOH                            | workCenter_id                                     | int         | int            | NO            |             |
| scWOHAdjustment                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scWOHAdjustment                  | woh_id                                            | int         | int            | NO            | Foreign Key |
| scWOHAdjustment                  | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scWOHAdjustment                  | classoid                                          | int         | int            | NO            |             |
| scWOHAdjustment                  | eventDate                                         | datetime    | datetime       | NO            |             |
| scWOHAdjustment                  | leadingStatus                                     | varchar     | varchar(255)   | NO            |             |
| scWOHAdjustment                  | productionQty                                     | bigint      | bigint         | NO            |             |
| scWOHAdjustment                  | quantity                                          | bigint      | bigint         | NO            |             |
| scWOHAdjustment                  | receivedQty                                       | bigint      | bigint         | NO            |             |
| scWOHAdjustment                  | status                                            | varchar     | varchar(255)   | NO            |             |
| scWOHAdjustment                  | toReceiveQty                                      | bigint      | bigint         | NO            |             |
| scWOHAdjustment                  | trailingStatus                                    | varchar     | varchar(255)   | NO            |             |
| scWOHAdjustment                  | type                                              | varchar     | varchar(255)   | NO            |             |
| scWOHAdjustment                  | uoi_id                                            | int         | int            | NO            |             |
| scWOHAdjustment                  | user_id                                           | int         | int            | NO            |             |
| scWOS                            | oid                                               | int         | int            | NO            | Primary Key |
| scWOS                            | materialMaster_id                                 | int         | int            | NO            | Foreign Key |
| scWOS                            | site_id                                           | int         | int            | NO            | Foreign Key |
| scWOS                            | woh_id                                            | int         | int            | NO            | Foreign Key |
| scWOS                            | woms_id                                           | int         | int            | NO            | Foreign Key |
| scWOS                            | actionRequired                                    | text        | text           | NO            |             |
| scWOS                            | backOrder                                         | varchar     | varchar(255)   | NO            |             |
| scWOS                            | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scWOS                            | classoid                                          | int         | int            | NO            |             |
| scWOS                            | configurationItem_id                              | int         | int            | NO            |             |
| scWOS                            | dependency                                        | varchar     | varchar(255)   | NO            |             |
| scWOS                            | description                                       | text        | text           | NO            |             |
| scWOS                            | duration                                          | int         | int            | NO            |             |
| scWOS                            | earliest                                          | datetime    | datetime       | NO            |             |
| scWOS                            | executionDate                                     | datetime    | datetime       | NO            |             |
| scWOS                            | leadingStatus                                     | varchar     | varchar(255)   | NO            |             |
| scWOS                            | manufacturingJob_id                               | int         | int            | NO            |             |
| scWOS                            | outstandingQty                                    | bigint      | bigint         | NO            |             |
| scWOS                            | owner_id                                          | int         | int            | NO            |             |
| scWOS                            | percentComplete                                   | varchar     | varchar(255)   | NO            |             |
| scWOS                            | pickTicketNo                                      | varchar     | varchar(255)   | NO            |             |
| scWOS                            | plannedEnd                                        | datetime    | datetime       | NO            |             |
| scWOS                            | plannedStart                                      | datetime    | datetime       | NO            |             |
| scWOS                            | priority                                          | varchar     | varchar(255)   | NO            |             |
| scWOS                            | productionQty                                     | bigint      | bigint         | NO            |             |
| scWOS                            | quantity                                          | bigint      | bigint         | NO            |             |
| scWOS                            | receivedQty                                       | bigint      | bigint         | NO            |             |
| scWOS                            | referenceNo                                       | varchar     | varchar(255)   | NO            |             |
| scWOS                            | requester_id                                      | int         | int            | NO            |             |
| scWOS                            | requiredDate                                      | datetime    | datetime       | NO            |             |
| scWOS                            | seqChildren                                       | varchar     | varchar(255)   | NO            |             |
| scWOS                            | sequence                                          | varchar     | varchar(255)   | NO            |             |
| scWOS                            | shippedDate                                       | datetime    | datetime       | NO            |             |
| scWOS                            | shipTo_id                                         | int         | int            | NO            |             |
| scWOS                            | shipToDepartment_id                               | int         | int            | NO            |             |
| scWOS                            | slack                                             | int         | int            | NO            |             |
| scWOS                            | status                                            | varchar     | varchar(255)   | NO            |             |
| scWOS                            | supplier_id                                       | int         | int            | NO            |             |
| scWOS                            | toReceiveQty                                      | bigint      | bigint         | NO            |             |
| scWOS                            | trailingStatus                                    | varchar     | varchar(255)   | NO            |             |
| scWOS                            | unitPrice                                         | decimal     | decimal(19,2)  | NO            |             |
| scWOS                            | uoi_id                                            | int         | int            | NO            |             |
| scWOS                            | workCenter_id                                     | int         | int            | NO            |             |
| scWOS                            | workCenterType_id                                 | int         | int            | NO            |             |
| scWOSAdjustment                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scWOSAdjustment                  | parent_id                                         | int         | int            | NO            | Foreign Key |
| scWOSAdjustment                  | wos_id                                            | int         | int            | NO            | Foreign Key |
| scWOSAdjustment                  | cancelledQty                                      | bigint      | bigint         | NO            |             |
| scWOSAdjustment                  | classoid                                          | int         | int            | NO            |             |
| scWOSAdjustment                  | leadingStatus                                     | varchar     | varchar(255)   | NO            |             |
| scWOSAdjustment                  | outstandingQty                                    | bigint      | bigint         | NO            |             |
| scWOSAdjustment                  | productionQty                                     | bigint      | bigint         | NO            |             |
| scWOSAdjustment                  | quantity                                          | bigint      | bigint         | NO            |             |
| scWOSAdjustment                  | receivedQty                                       | bigint      | bigint         | NO            |             |
| scWOSAdjustment                  | status                                            | varchar     | varchar(255)   | NO            |             |
| scWOSAdjustment                  | toReceiveQty                                      | bigint      | bigint         | NO            |             |
| scWOSAdjustment                  | trailingStatus                                    | varchar     | varchar(255)   | NO            |             |
| scWOSAdjustment                  | uoi_id                                            | int         | int            | NO            |             |
| scWorkCenter                     | oid                                               | int         | int            | NO            | Primary Key |
| scWorkCenter                     | type_id                                           | int         | int            | NO            | Foreign Key |
| scWorkCenter                     | zone_id                                           | int         | int            | NO            | Foreign Key |
| scWorkCenter                     | classoid                                          | int         | int            | NO            |             |
| scWorkCenter                     | name                                              | varchar     | varchar(255)   | NO            |             |
| scWorkCenter                     | outBay_id                                         | int         | int            | NO            |             |
| scWorkCenter                     | productionBay_id                                  | int         | int            | NO            |             |
| scWorkCenter                     | scale_id                                          | int         | int            | NO            |             |
| scWorkCenter                     | site_id                                           | int         | int            | NO            |             |
| scWorkCenter                     | status                                            | varchar     | varchar(255)   | NO            |             |
| scWorkCenterPrinter              | oid                                               | int         | int            | NO            | Primary Key |
| scWorkCenterPrinter              | classoid                                          | int         | int            | NO            |             |
| scWorkCenterPrinter              | printer_id                                        | int         | int            | NO            |             |
| scWorkCenterPrinter              | printerFormat_id                                  | int         | int            | NO            |             |
| scWorkCenterPrinter              | printerType_id                                    | int         | int            | NO            |             |
| scWorkCenterPrinter              | workCenter_id                                     | int         | int            | NO            |             |
| scWorkCenterType                 | oid                                               | int         | int            | NO            | Primary Key |
| scWorkCenterType                 | classoid                                          | int         | int            | NO            |             |
| scWorkCenterType                 | description                                       | text        | text           | NO            |             |
| scWorkCenterType                 | name                                              | varchar     | varchar(255)   | NO            |             |
| scWorkCenterType                 | status                                            | varchar     | varchar(255)   | NO            |             |
| scWorkCenterType                 | type                                              | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | oid                                               | int         | int            | NO            | Primary Key |
| scWorkOrderType                  | cancellationStatus                                | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | classoid                                          | int         | int            | NO            |             |
| scWorkOrderType                  | consumptionMode                                   | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | consumptionPriority                               | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | description                                       | text        | text           | NO            |             |
| scWorkOrderType                  | inbayValidationMode                               | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | initialStatus                                     | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | modificationStatus                                | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | name                                              | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | orderClass                                        | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | orderCompletion                                   | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | orderCreation                                     | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | outputProcess                                     | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | owner                                             | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | productionType                                    | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | routeType_id                                      | int         | int            | NO            |             |
| scWorkOrderType                  | status                                            | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | transferCreation                                  | varchar     | varchar(255)   | NO            |             |
| scWorkOrderType                  | transferType_id                                   | int         | int            | NO            |             |
| scWorkOrderType                  | workCenterType_id                                 | int         | int            | NO            |             |
| scWorkcenterLoc                  | oid                                               | int         | int            | NO            | Primary Key |
| scWorkcenterLoc                  | classoid                                          | int         | int            | NO            |             |
| scWorkcenterLoc                  | location_id                                       | int         | int            | NO            |             |
| scWorkcenterLoc                  | type                                              | varchar     | varchar(255)   | NO            |             |
| scWorkcenterLoc                  | workcenter_id                                     | int         | int            | NO            |             |
| scZLocation                      | oid                                               | int         | int            | NO            | Primary Key |
| scZLocation                      | zlocation                                         | varchar     | varchar(255)   | NO            | Foreign Key |
| scZLocation                      | classoid                                          | int         | int            | NO            |             |
| scZLocation                      | object_id                                         | int         | int            | NO            |             |
| scZLocation                      | site_id                                           | int         | int            | NO            |             |
| scZone                           | oid                                               | int         | int            | NO            | Primary Key |
| scZone                           | costCenter_id                                     | int         | int            | NO            | Foreign Key |
| scZone                           | gln                                               | varchar     | varchar(255)   | NO            | Foreign Key |
| scZone                           | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| scZone                           | parent_id                                         | int         | int            | NO            | Foreign Key |
| scZone                           | site_id                                           | int         | int            | NO            | Foreign Key |
| scZone                           | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| scZone                           | allowMixAttributes                                | varchar     | varchar(10)    | NO            |             |
| scZone                           | allowMixExpiryDate                                | varchar     | varchar(10)    | NO            |             |
| scZone                           | allowMixItems                                     | varchar     | varchar(10)    | NO            |             |
| scZone                           | allowMixLotNo                                     | varchar     | varchar(10)    | NO            |             |
| scZone                           | allowMixMode                                      | varchar     | varchar(255)   | NO            |             |
| scZone                           | allowMixOwners                                    | varchar     | varchar(10)    | NO            |             |
| scZone                           | classoid                                          | int         | int            | NO            |             |
| scZone                           | description                                       | varchar     | varchar(255)   | NO            |             |
| scZone                           | enableAgingReport                                 | varchar     | varchar(10)    | NO            |             |
| scZone                           | replenishmentJob_id                               | int         | int            | NO            |             |
| scZone                           | type_id                                           | int         | int            | NO            |             |
| scZoneRelation                   | oid                                               | bigint      | bigint         | NO            | Primary Key |
| scZoneRelation                   | child_id                                          | int         | int            | NO            | Foreign Key |
| scZoneRelation                   | classoid                                          | int         | int            | NO            |             |
| scZoneRelation                   | parent_id                                         | int         | int            | NO            |             |
| scZoneRelation                   | relationType                                      | varchar     | varchar(255)   | NO            |             |
| scZoneRelation                   | sequence                                          | int         | int            | NO            |             |
| smAPIService                     | oid                                               | int         | int            | NO            | Primary Key |
| smAPIService                     | classoid                                          | int         | int            | NO            |             |
| smAPIService                     | description_id                                    | int         | int            | NO            |             |
| smAPIService                     | label_id                                          | int         | int            | NO            |             |
| smAPIService                     | module_id                                         | int         | int            | NO            |             |
| smAPIService                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smAPIService                     | type_id                                           | int         | int            | NO            |             |
| smAPIServiceInstance             | oid                                               | int         | int            | NO            | Primary Key |
| smAPIServiceInstance             | classoid                                          | int         | int            | NO            |             |
| smAPIServiceInstance             | instance_id                                       | int         | int            | NO            |             |
| smAPIServiceInstance             | module_id                                         | int         | int            | NO            |             |
| smAPIServiceInstance             | system_id                                         | int         | int            | NO            |             |
| smAPIServiceInstance             | systemAccount_id                                  | int         | int            | NO            |             |
| smAPIServiceInstance             | systemInstance_id                                 | int         | int            | NO            |             |
| smAPIServiceInterface            | oid                                               | int         | int            | NO            | Primary Key |
| smAPIServiceInterface            | classoid                                          | int         | int            | NO            |             |
| smAPIServiceInterface            | exporter_id                                       | int         | int            | NO            |             |
| smAPIServiceInterface            | interfaceExporter_id                              | int         | int            | NO            |             |
| smAPIServiceInterface            | module_id                                         | int         | int            | NO            |             |
| smAPIServiceInterface            | scriptText                                        | text        | text           | NO            |             |
| smAPIServiceInterface            | scriptType                                        | varchar     | varchar(255)   | NO            |             |
| smAPIServiceInterface            | service_id                                        | int         | int            | NO            |             |
| smAPIServiceInterface            | system_id                                         | int         | int            | NO            |             |
| smAPIServiceParameter            | oid                                               | int         | int            | NO            | Primary Key |
| smAPIServiceParameter            | classoid                                          | int         | int            | NO            |             |
| smAPIServiceParameter            | description_id                                    | int         | int            | NO            |             |
| smAPIServiceParameter            | direction                                         | varchar     | varchar(255)   | NO            |             |
| smAPIServiceParameter            | label_id                                          | int         | int            | NO            |             |
| smAPIServiceParameter            | module_id                                         | int         | int            | NO            |             |
| smAPIServiceParameter            | name                                              | varchar     | varchar(255)   | NO            |             |
| smAPIServiceParameter            | required                                          | varchar     | varchar(10)    | NO            |             |
| smAPIServiceParameter            | service_id                                        | int         | int            | NO            |             |
| smAPIServiceParameter            | type_id                                           | int         | int            | NO            |             |
| smAPIServiceSystem               | oid                                               | int         | int            | NO            | Primary Key |
| smAPIServiceSystem               | classoid                                          | int         | int            | NO            |             |
| smAPIServiceSystem               | description_id                                    | int         | int            | NO            |             |
| smAPIServiceSystem               | label_id                                          | int         | int            | NO            |             |
| smAPIServiceSystem               | module_id                                         | int         | int            | NO            |             |
| smAPIServiceSystem               | name                                              | varchar     | varchar(255)   | NO            |             |
| smAPIServiceSystem               | system_id                                         | int         | int            | NO            |             |
| smAPIServiceSystem               | type_id                                           | int         | int            | NO            |             |
| smAPIServiceType                 | oid                                               | int         | int            | NO            | Primary Key |
| smAPIServiceType                 | classoid                                          | int         | int            | NO            |             |
| smAPIServiceType                 | description_id                                    | int         | int            | NO            |             |
| smAPIServiceType                 | label_id                                          | int         | int            | NO            |             |
| smAPIServiceType                 | module_id                                         | int         | int            | NO            |             |
| smAPIServiceType                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smActionEvent                    | oid                                               | int         | int            | NO            | Primary Key |
| smActionEvent                    | action_id                                         | int         | int            | NO            |             |
| smActionEvent                    | active                                            | varchar     | varchar(10)    | NO            |             |
| smActionEvent                    | classoid                                          | int         | int            | NO            |             |
| smActionEvent                    | code                                              | varchar     | varchar(255)   | NO            |             |
| smActionEvent                    | description_id                                    | int         | int            | NO            |             |
| smActionEvent                    | label_id                                          | int         | int            | NO            |             |
| smActionEvent                    | message_id                                        | int         | int            | NO            |             |
| smActionEvent                    | module_id                                         | int         | int            | NO            |             |
| smActionEvent                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smActionEvent                    | reference_id                                      | int         | int            | NO            |             |
| smActionEvent                    | sequence                                          | int         | int            | NO            |             |
| smActionEvent                    | type_id                                           | int         | int            | NO            |             |
| smActionEventType                | oid                                               | int         | int            | NO            | Primary Key |
| smActionEventType                | action_id                                         | int         | int            | NO            |             |
| smActionEventType                | classoid                                          | int         | int            | NO            |             |
| smActionEventType                | code                                              | varchar     | varchar(255)   | NO            |             |
| smActionEventType                | description_id                                    | int         | int            | NO            |             |
| smActionEventType                | label_id                                          | int         | int            | NO            |             |
| smActionEventType                | message_id                                        | int         | int            | NO            |             |
| smActionEventType                | module_id                                         | int         | int            | NO            |             |
| smActionEventType                | name                                              | varchar     | varchar(255)   | NO            |             |
| smActionEventType                | reference_id                                      | int         | int            | NO            |             |
| smActionExecutionPool            | oid                                               | int         | int            | NO            | Primary Key |
| smActionExecutionPool            | action_id                                         | int         | int            | NO            |             |
| smActionExecutionPool            | classoid                                          | int         | int            | NO            |             |
| smActionExecutionPool            | module_id                                         | int         | int            | NO            |             |
| smActionExecutionPool            | pool_id                                           | int         | int            | NO            |             |
| smActionExecutionPool            | priority                                          | int         | int            | NO            |             |
| smActionInterceptor              | oid                                               | int         | int            | NO            | Primary Key |
| smActionInterceptor              | action_id                                         | int         | int            | NO            | Foreign Key |
| smActionInterceptor              | active                                            | varchar     | varchar(10)    | NO            |             |
| smActionInterceptor              | asyncMode                                         | varchar     | varchar(10)    | NO            |             |
| smActionInterceptor              | classoid                                          | int         | int            | NO            |             |
| smActionInterceptor              | description_id                                    | int         | int            | NO            |             |
| smActionInterceptor              | label_id                                          | int         | int            | NO            |             |
| smActionInterceptor              | module_id                                         | int         | int            | NO            |             |
| smActionInterceptor              | name                                              | varchar     | varchar(255)   | NO            |             |
| smActionInterceptor              | reference_id                                      | int         | int            | NO            |             |
| smActionInterceptor              | referenceType_id                                  | int         | int            | NO            |             |
| smActionInterceptor              | sequence                                          | int         | int            | NO            |             |
| smActionScript                   | oid                                               | int         | int            | NO            | Primary Key |
| smActionScript                   | action_id                                         | int         | int            | NO            |             |
| smActionScript                   | classoid                                          | int         | int            | NO            |             |
| smActionScript                   | content                                           | mediumtext  | mediumtext     | NO            |             |
| smActionScript                   | description_id                                    | int         | int            | NO            |             |
| smActionScript                   | label_id                                          | int         | int            | NO            |             |
| smActionScript                   | language_id                                       | int         | int            | NO            |             |
| smActionScript                   | module_id                                         | int         | int            | NO            |             |
| smActionScript                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smActionScript                   | parent_id                                         | int         | int            | NO            |             |
| smActionScript                   | scriptContext_id                                  | int         | int            | NO            |             |
| smActionScript                   | status                                            | varchar     | varchar(255)   | NO            |             |
| smActionValidator                | oid                                               | int         | int            | NO            | Primary Key |
| smActionValidator                | action_id                                         | int         | int            | NO            | Foreign Key |
| smActionValidator                | active                                            | varchar     | varchar(10)    | NO            |             |
| smActionValidator                | classoid                                          | int         | int            | NO            |             |
| smActionValidator                | description_id                                    | int         | int            | NO            |             |
| smActionValidator                | label_id                                          | int         | int            | NO            |             |
| smActionValidator                | module_id                                         | int         | int            | NO            |             |
| smActionValidator                | name                                              | varchar     | varchar(255)   | NO            |             |
| smActionValidator                | sequence                                          | int         | int            | NO            |             |
| smAllowedLookupCategory          | oid                                               | int         | int            | NO            | Primary Key |
| smAllowedLookupCategory          | category_id                                       | int         | int            | NO            |             |
| smAllowedLookupCategory          | classoid                                          | int         | int            | NO            |             |
| smAllowedLookupCategory          | context_id                                        | int         | int            | NO            |             |
| smAllowedLookupCategory          | module_id                                         | int         | int            | NO            |             |
| smAllowedLookupCategory          | name                                              | varchar     | varchar(255)   | NO            |             |
| smAllowedLookupCategory          | status                                            | varchar     | varchar(255)   | NO            |             |
| smAllowedLookupItem              | oid                                               | int         | int            | NO            | Primary Key |
| smAllowedLookupItem              | category_id                                       | int         | int            | NO            |             |
| smAllowedLookupItem              | classoid                                          | int         | int            | NO            |             |
| smAllowedLookupItem              | item_id                                           | int         | int            | NO            |             |
| smAllowedLookupItem              | module_id                                         | int         | int            | NO            |             |
| smAllowedLookupItem              | sequence                                          | int         | int            | NO            |             |
| smAllowedLookupItem              | status                                            | varchar     | varchar(255)   | NO            |             |
| smAppProfileEndpoint             | oid                                               | int         | int            | NO            | Primary Key |
| smAppProfileEndpoint             | classoid                                          | int         | int            | NO            |             |
| smAppProfileEndpoint             | module_id                                         | int         | int            | NO            |             |
| smAppProfileEndpoint             | type_id                                           | int         | int            | NO            |             |
| smAppProfileEndpoint             | userEndpoint_id                                   | int         | int            | NO            |             |
| smAppProfileEndpointType         | oid                                               | int         | int            | NO            | Primary Key |
| smAppProfileEndpointType         | classoid                                          | int         | int            | NO            |             |
| smAppProfileEndpointType         | defaultEndpoint_id                                | int         | int            | NO            |             |
| smAppProfileEndpointType         | endpointType_id                                   | int         | int            | NO            |             |
| smAppProfileEndpointType         | module_id                                         | int         | int            | NO            |             |
| smAppProfileEndpointType         | profile_id                                        | int         | int            | NO            |             |
| smAppService                     | oid                                               | int         | int            | NO            | Primary Key |
| smAppService                     | autoStart                                         | varchar     | varchar(10)    | NO            |             |
| smAppService                     | canPause                                          | varchar     | varchar(10)    | NO            |             |
| smAppService                     | canRestart                                        | varchar     | varchar(10)    | NO            |             |
| smAppService                     | canStop                                           | varchar     | varchar(10)    | NO            |             |
| smAppService                     | classoid                                          | int         | int            | NO            |             |
| smAppService                     | description_id                                    | int         | int            | NO            |             |
| smAppService                     | label_id                                          | int         | int            | NO            |             |
| smAppService                     | module_id                                         | int         | int            | NO            |             |
| smAppService                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smAppService                     | parent_id                                         | int         | int            | NO            |             |
| smAppService                     | sequence                                          | int         | int            | NO            |             |
| smAppService                     | type                                              | varchar     | varchar(255)   | NO            |             |
| smAppService                     | type_id                                           | int         | int            | NO            |             |
| smAppServiceMode                 | oid                                               | int         | int            | NO            | Primary Key |
| smAppServiceMode                 | applicationMode_id                                | int         | int            | NO            |             |
| smAppServiceMode                 | classoid                                          | int         | int            | NO            |             |
| smAppServiceMode                 | limited                                           | varchar     | varchar(10)    | NO            |             |
| smAppServiceMode                 | module_id                                         | int         | int            | NO            |             |
| smAppServiceMode                 | operationMode_id                                  | int         | int            | NO            |             |
| smAppServiceMode                 | sequence                                          | int         | int            | NO            |             |
| smAppServiceMode                 | service_id                                        | int         | int            | NO            |             |
| smApplication                    | oid                                               | int         | int            | NO            | Primary Key |
| smApplication                    | authenticationSystem_id                           | int         | int            | NO            |             |
| smApplication                    | classoid                                          | int         | int            | NO            |             |
| smApplication                    | description_id                                    | int         | int            | NO            |             |
| smApplication                    | label_id                                          | int         | int            | NO            |             |
| smApplication                    | module_id                                         | int         | int            | NO            |             |
| smApplication                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smApplication                    | notes_id                                          | int         | int            | NO            |             |
| smApplicationInstance            | oid                                               | int         | int            | NO            | Primary Key |
| smApplicationInstance            | active                                            | varchar     | varchar(10)    | NO            |             |
| smApplicationInstance            | application_id                                    | int         | int            | NO            |             |
| smApplicationInstance            | classoid                                          | int         | int            | NO            |             |
| smApplicationInstance            | description_id                                    | int         | int            | NO            |             |
| smApplicationInstance            | instanceModule_id                                 | int         | int            | NO            |             |
| smApplicationInstance            | label_id                                          | int         | int            | NO            |             |
| smApplicationInstance            | module_id                                         | int         | int            | NO            |             |
| smApplicationInstance            | name                                              | varchar     | varchar(255)   | NO            |             |
| smApplicationInstance            | profile_id                                        | int         | int            | NO            |             |
| smApplicationInstance            | serverGroup_id                                    | int         | int            | NO            |             |
| smApplicationInstance            | status                                            | varchar     | varchar(255)   | NO            |             |
| smApplicationMode                | oid                                               | int         | int            | NO            | Primary Key |
| smApplicationMode                | applicationModel_id                               | int         | int            | NO            |             |
| smApplicationMode                | classoid                                          | int         | int            | NO            |             |
| smApplicationMode                | module_id                                         | int         | int            | NO            |             |
| smApplicationMode                | operationMode_id                                  | int         | int            | NO            |             |
| smApplicationProfile             | oid                                               | int         | int            | NO            | Primary Key |
| smApplicationProfile             | application_id                                    | int         | int            | NO            |             |
| smApplicationProfile             | classoid                                          | int         | int            | NO            |             |
| smApplicationProfile             | description_id                                    | int         | int            | NO            |             |
| smApplicationProfile             | label_id                                          | int         | int            | NO            |             |
| smApplicationProfile             | module_id                                         | int         | int            | NO            |             |
| smApplicationProfile             | name                                              | varchar     | varchar(255)   | NO            |             |
| smApplicationServerGroup         | oid                                               | int         | int            | NO            | Primary Key |
| smApplicationServerGroup         | applicationModel_id                               | int         | int            | NO            |             |
| smApplicationServerGroup         | classoid                                          | int         | int            | NO            |             |
| smApplicationServerGroup         | description_id                                    | int         | int            | NO            |             |
| smApplicationServerGroup         | label_id                                          | int         | int            | NO            |             |
| smApplicationServerGroup         | module_id                                         | int         | int            | NO            |             |
| smApplicationServerGroup         | name                                              | varchar     | varchar(255)   | NO            |             |
| smArchivingStrategy              | oid                                               | int         | int            | NO            | Primary Key |
| smArchivingStrategy              | archiveGroup_id                                   | int         | int            | NO            |             |
| smArchivingStrategy              | classoid                                          | int         | int            | NO            |             |
| smArchivingStrategy              | dataGroup_id                                      | int         | int            | NO            |             |
| smArchivingStrategy              | description_id                                    | int         | int            | NO            |             |
| smArchivingStrategy              | label_id                                          | int         | int            | NO            |             |
| smArchivingStrategy              | module_id                                         | int         | int            | NO            |             |
| smArchivingStrategy              | name                                              | varchar     | varchar(255)   | NO            |             |
| smArchivingStrategyObject        | oid                                               | int         | int            | NO            | Primary Key |
| smArchivingStrategyObject        | classoid                                          | int         | int            | NO            |             |
| smArchivingStrategyObject        | description_id                                    | int         | int            | NO            |             |
| smArchivingStrategyObject        | label_id                                          | int         | int            | NO            |             |
| smArchivingStrategyObject        | module_id                                         | int         | int            | NO            |             |
| smArchivingStrategyObject        | name                                              | varchar     | varchar(255)   | NO            |             |
| smArchivingStrategyObject        | object_id                                         | int         | int            | NO            |             |
| smArchivingStrategyObject        | strategy_id                                       | int         | int            | NO            |             |
| smAttribute                      | oid                                               | int         | int            | NO            | Primary Key |
| smAttribute                      | column_id                                         | int         | int            | NO            | Foreign Key |
| smAttribute                      | object_id                                         | int         | int            | NO            | Foreign Key |
| smAttribute                      | type_id                                           | int         | int            | NO            | Foreign Key |
| smAttribute                      | chainAttribute_id                                 | int         | int            | NO            |             |
| smAttribute                      | classoid                                          | int         | int            | NO            |             |
| smAttribute                      | configurable                                      | varchar     | varchar(255)   | NO            |             |
| smAttribute                      | defaultvalue                                      | varchar     | varchar(255)   | NO            |             |
| smAttribute                      | description_id                                    | int         | int            | NO            |             |
| smAttribute                      | dynamic_id                                        | int         | int            | NO            |             |
| smAttribute                      | eventLogging                                      | varchar     | varchar(255)   | NO            |             |
| smAttribute                      | importtype                                        | varchar     | varchar(255)   | NO            |             |
| smAttribute                      | insertable                                        | varchar     | varchar(10)    | NO            |             |
| smAttribute                      | label_id                                          | int         | int            | NO            |             |
| smAttribute                      | massUpdatable                                     | varchar     | varchar(10)    | NO            |             |
| smAttribute                      | mode                                              | varchar     | varchar(255)   | NO            |             |
| smAttribute                      | module_id                                         | int         | int            | NO            |             |
| smAttribute                      | name                                              | varchar     | varchar(255)   | NO            |             |
| smAttribute                      | notes_id                                          | int         | int            | NO            |             |
| smAttribute                      | readonly                                          | varchar     | varchar(10)    | NO            |             |
| smAttribute                      | related_id                                        | int         | int            | NO            |             |
| smAttribute                      | relationType                                      | varchar     | varchar(255)   | NO            |             |
| smAttribute                      | required                                          | varchar     | varchar(10)    | NO            |             |
| smAttribute                      | restrictedValue                                   | varchar     | varchar(10)    | NO            |             |
| smAttribute                      | scriptText                                        | text        | text           | NO            |             |
| smAttribute                      | tagName                                           | varchar     | varchar(255)   | NO            |             |
| smAttribute                      | typeColumn_id                                     | int         | int            | NO            |             |
| smAttribute                      | updatable                                         | varchar     | varchar(10)    | NO            |             |
| smAttributeOptions               | oid                                               | int         | int            | NO            | Primary Key |
| smAttributeOptions               | attribute_id                                      | int         | int            | NO            |             |
| smAttributeOptions               | classoid                                          | int         | int            | NO            |             |
| smAttributeOptions               | module_id                                         | int         | int            | NO            |             |
| smAttributeOptions               | name                                              | varchar     | varchar(255)   | NO            |             |
| smAttributeOptions               | value                                             | varchar     | varchar(255)   | NO            |             |
| smAuthSystemInstance             | oid                                               | int         | int            | NO            | Primary Key |
| smAuthSystemInstance             | classoid                                          | int         | int            | NO            |             |
| smAuthSystemInstance             | instance_id                                       | int         | int            | NO            |             |
| smAuthSystemInstance             | module_id                                         | int         | int            | NO            |             |
| smAuthSystemInstance             | system_id                                         | int         | int            | NO            |             |
| smAuthenticationSystem           | oid                                               | int         | int            | NO            | Primary Key |
| smAuthenticationSystem           | classoid                                          | int         | int            | NO            |             |
| smAuthenticationSystem           | description_id                                    | int         | int            | NO            |             |
| smAuthenticationSystem           | domainNames                                       | varchar     | varchar(255)   | NO            |             |
| smAuthenticationSystem           | label_id                                          | int         | int            | NO            |             |
| smAuthenticationSystem           | module_id                                         | int         | int            | NO            |             |
| smAuthenticationSystem           | name                                              | varchar     | varchar(255)   | NO            |             |
| smAuthenticationSystem           | policy_id                                         | int         | int            | NO            |             |
| smAuthenticationSystem           | security_id                                       | int         | int            | NO            |             |
| smAuthenticationSystem           | sessiontype_id                                    | int         | int            | NO            |             |
| smAuthenticationSystem           | type_id                                           | int         | int            | NO            |             |
| smAuthenticationType             | oid                                               | int         | int            | NO            | Primary Key |
| smAuthenticationType             | classoid                                          | int         | int            | NO            |             |
| smAuthenticationType             | description_id                                    | int         | int            | NO            |             |
| smAuthenticationType             | label_id                                          | int         | int            | NO            |             |
| smAuthenticationType             | mode                                              | varchar     | varchar(255)   | NO            |             |
| smAuthenticationType             | module_id                                         | int         | int            | NO            |             |
| smAuthenticationType             | name                                              | varchar     | varchar(255)   | NO            |             |
| smBObjectInterface               | oid                                               | int         | int            | NO            | Primary Key |
| smBObjectInterface               | object_id                                         | int         | int            | NO            | Foreign Key |
| smBObjectInterface               | classoid                                          | int         | int            | NO            |             |
| smBObjectInterface               | interface_id                                      | int         | int            | NO            |             |
| smBObjectInterface               | module_id                                         | int         | int            | NO            |             |
| smBatchAction                    | oid                                               | int         | int            | NO            | Primary Key |
| smBatchAction                    | action_id                                         | int         | int            | NO            |             |
| smBatchAction                    | classoid                                          | int         | int            | NO            |             |
| smBatchAction                    | module_id                                         | int         | int            | NO            |             |
| smBatchAction                    | object_id                                         | int         | int            | NO            |             |
| smBatchAction                    | parameter_id                                      | int         | int            | NO            |             |
| smBatchAction                    | type                                              | varchar     | varchar(255)   | NO            |             |
| smBatchActionParam               | oid                                               | int         | int            | NO            | Primary Key |
| smBatchActionParam               | action_id                                         | int         | int            | NO            |             |
| smBatchActionParam               | attribute_id                                      | int         | int            | NO            |             |
| smBatchActionParam               | classoid                                          | int         | int            | NO            |             |
| smBatchActionParam               | module_id                                         | int         | int            | NO            |             |
| smBatchActionParam               | parameter_id                                      | int         | int            | NO            |             |
| smBatchAttribute                 | oid                                               | int         | int            | NO            | Primary Key |
| smBatchAttribute                 | classoid                                          | int         | int            | NO            |             |
| smBatchAttribute                 | column_id                                         | int         | int            | NO            |             |
| smBatchAttribute                 | description_id                                    | int         | int            | NO            |             |
| smBatchAttribute                 | label_id                                          | int         | int            | NO            |             |
| smBatchAttribute                 | module_id                                         | int         | int            | NO            |             |
| smBatchAttribute                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smBatchAttribute                 | object_id                                         | int         | int            | NO            |             |
| smBatchAttribute                 | type_id                                           | int         | int            | NO            |             |
| smBatchConfiguration             | oid                                               | int         | int            | NO            | Primary Key |
| smBatchConfiguration             | classoid                                          | int         | int            | NO            |             |
| smBatchConfiguration             | description_id                                    | int         | int            | NO            |             |
| smBatchConfiguration             | label_id                                          | int         | int            | NO            |             |
| smBatchConfiguration             | module_id                                         | int         | int            | NO            |             |
| smBatchConfiguration             | name                                              | varchar     | varchar(255)   | NO            |             |
| smBatchObject                    | oid                                               | int         | int            | NO            | Primary Key |
| smBatchObject                    | classoid                                          | int         | int            | NO            |             |
| smBatchObject                    | description_id                                    | int         | int            | NO            |             |
| smBatchObject                    | label_id                                          | int         | int            | NO            |             |
| smBatchObject                    | module_id                                         | int         | int            | NO            |             |
| smBatchObject                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smBatchObject                    | query_id                                          | int         | int            | NO            |             |
| smBusinessObject                 | oid                                               | int         | int            | NO            | Primary Key |
| smBusinessObject                 | module_id                                         | int         | int            | NO            | Foreign Key |
| smBusinessObject                 | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smBusinessObject                 | parent_id                                         | int         | int            | NO            | Foreign Key |
| smBusinessObject                 | table_id                                          | int         | int            | NO            | Foreign Key |
| smBusinessObject                 | abstractClass                                     | varchar     | varchar(10)    | NO            |             |
| smBusinessObject                 | classoid                                          | int         | int            | NO            |             |
| smBusinessObject                 | deletable                                         | varchar     | varchar(10)    | NO            |             |
| smBusinessObject                 | description_id                                    | int         | int            | NO            |             |
| smBusinessObject                 | displayAttribute_id                               | int         | int            | NO            |             |
| smBusinessObject                 | displaydesc_id                                    | int         | int            | NO            |             |
| smBusinessObject                 | displayField                                      | varchar     | varchar(255)   | NO            |             |
| smBusinessObject                 | importable                                        | varchar     | varchar(255)   | NO            |             |
| smBusinessObject                 | label_id                                          | int         | int            | NO            |             |
| smBusinessObject                 | notes_id                                          | int         | int            | NO            |             |
| smBusinessObject                 | query_id                                          | int         | int            | NO            |             |
| smCache                          | oid                                               | int         | int            | NO            | Primary Key |
| smCache                          | type_id                                           | int         | int            | NO            | Foreign Key |
| smCache                          | classoid                                          | int         | int            | NO            |             |
| smCache                          | configuration_id                                  | int         | int            | NO            |             |
| smCache                          | description_id                                    | int         | int            | NO            |             |
| smCache                          | label_id                                          | int         | int            | NO            |             |
| smCache                          | loadingMode                                       | varchar     | varchar(255)   | NO            |             |
| smCache                          | module_id                                         | int         | int            | NO            |             |
| smCache                          | name                                              | varchar     | varchar(255)   | NO            |             |
| smCache                          | object_id                                         | int         | int            | NO            |             |
| smCacheConfiguration             | oid                                               | int         | int            | NO            | Primary Key |
| smCacheConfiguration             | classoid                                          | int         | int            | NO            |             |
| smCacheConfiguration             | description_id                                    | int         | int            | NO            |             |
| smCacheConfiguration             | label_id                                          | int         | int            | NO            |             |
| smCacheConfiguration             | module_id                                         | int         | int            | NO            |             |
| smCacheConfiguration             | name                                              | varchar     | varchar(255)   | NO            |             |
| smCacheConfiguration             | strategy_id                                       | int         | int            | NO            |             |
| smCacheConfiguration             | type_id                                           | int         | int            | NO            |             |
| smCacheItem                      | oid                                               | int         | int            | NO            | Primary Key |
| smCacheItem                      | cache_id                                          | int         | int            | NO            |             |
| smCacheItem                      | classoid                                          | int         | int            | NO            |             |
| smCacheItem                      | description_id                                    | int         | int            | NO            |             |
| smCacheItem                      | label_id                                          | int         | int            | NO            |             |
| smCacheItem                      | loadingMode                                       | varchar     | varchar(255)   | NO            |             |
| smCacheItem                      | module_id                                         | int         | int            | NO            |             |
| smCacheItem                      | name                                              | varchar     | varchar(255)   | NO            |             |
| smCacheItem                      | type_id                                           | int         | int            | NO            |             |
| smCacheableType                  | oid                                               | int         | int            | NO            | Primary Key |
| smCacheableType                  | classoid                                          | int         | int            | NO            |             |
| smCacheableType                  | module_id                                         | int         | int            | NO            |             |
| smCacheableType                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smCacheableType                  | strategy_id                                       | int         | int            | NO            |             |
| smCacheableType                  | type_id                                           | int         | int            | NO            |             |
| smCachingStrategy                | oid                                               | int         | int            | NO            | Primary Key |
| smCachingStrategy                | classoid                                          | int         | int            | NO            |             |
| smCachingStrategy                | configuration_id                                  | int         | int            | NO            |             |
| smCachingStrategy                | description_id                                    | int         | int            | NO            |             |
| smCachingStrategy                | label_id                                          | int         | int            | NO            |             |
| smCachingStrategy                | module_id                                         | int         | int            | NO            |             |
| smCachingStrategy                | name                                              | varchar     | varchar(255)   | NO            |             |
| smCachingStrategyInstance        | oid                                               | int         | int            | NO            | Primary Key |
| smCachingStrategyInstance        | classoid                                          | int         | int            | NO            |             |
| smCachingStrategyInstance        | configuration_id                                  | int         | int            | NO            |             |
| smCachingStrategyInstance        | instance_id                                       | int         | int            | NO            |             |
| smCachingStrategyInstance        | module_id                                         | int         | int            | NO            |             |
| smCachingStrategyInstance        | strategy_id                                       | int         | int            | NO            |             |
| smCategory                       | oid                                               | int         | int            | NO            | Primary Key |
| smCategory                       | active                                            | varchar     | varchar(10)    | NO            |             |
| smCategory                       | classoid                                          | int         | int            | NO            |             |
| smCategory                       | description_id                                    | int         | int            | NO            |             |
| smCategory                       | help_id                                           | int         | int            | NO            |             |
| smCategory                       | label_id                                          | int         | int            | NO            |             |
| smCategory                       | module_id                                         | int         | int            | NO            |             |
| smCategory                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smCategory                       | parent_id                                         | int         | int            | NO            |             |
| smCategory                       | protectionMode                                    | varchar     | varchar(255)   | NO            |             |
| smCategory                       | referenceId                                       | char        | char(36)       | NO            |             |
| smCategory                       | subtype_id                                        | int         | int            | NO            |             |
| smCategory                       | type                                              | varchar     | varchar(255)   | NO            |             |
| smCategory                       | type_id                                           | int         | int            | NO            |             |
| smCategory                       | versionNo                                         | int         | int            | NO            |             |
| smChainObject                    | oid                                               | int         | int            | NO            | Primary Key |
| smChainObject                    | chain_id                                          | int         | int            | NO            |             |
| smChainObject                    | classoid                                          | int         | int            | NO            |             |
| smChainObject                    | module_id                                         | int         | int            | NO            |             |
| smChainObject                    | object_id                                         | int         | int            | NO            |             |
| smChainObject                    | param_id                                          | int         | int            | NO            |             |
| smChainObject                    | virtual                                           | varchar     | varchar(10)    | NO            |             |
| smCodeTemplate                   | oid                                               | int         | int            | NO            | Primary Key |
| smCodeTemplate                   | classoid                                          | int         | int            | NO            |             |
| smCodeTemplate                   | description_id                                    | int         | int            | NO            |             |
| smCodeTemplate                   | filename                                          | varchar     | varchar(255)   | NO            |             |
| smCodeTemplate                   | label_id                                          | int         | int            | NO            |             |
| smCodeTemplate                   | module_id                                         | int         | int            | NO            |             |
| smCodeTemplate                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smCodeTemplate                   | object_id                                         | int         | int            | NO            |             |
| smCodeTemplate                   | template                                          | text        | text           | NO            |             |
| smCodeTemplateObject             | oid                                               | int         | int            | NO            | Primary Key |
| smCodeTemplateObject             | attribute_id                                      | int         | int            | NO            |             |
| smCodeTemplateObject             | classoid                                          | int         | int            | NO            |             |
| smCodeTemplateObject             | codeTemplate_id                                   | int         | int            | NO            |             |
| smCodeTemplateObject             | module_id                                         | int         | int            | NO            |             |
| smCodeTemplateObject             | object_id                                         | int         | int            | NO            |             |
| smCodeTemplateObject             | parent_id                                         | int         | int            | NO            |             |
| smColor                          | oid                                               | int         | int            | NO            | Primary Key |
| smColor                          | baseColor                                         | varchar     | varchar(255)   | NO            | Foreign Key |
| smColor                          | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smColor                          | classoid                                          | int         | int            | NO            |             |
| smColor                          | code                                              | varchar     | varchar(255)   | NO            |             |
| smColor                          | module_id                                         | int         | int            | NO            |             |
| smColor                          | shade                                             | varchar     | varchar(255)   | NO            |             |
| smColumnTemplate                 | oid                                               | int         | int            | NO            | Primary Key |
| smColumnTemplate                 | classoid                                          | int         | int            | NO            |             |
| smColumnTemplate                 | description_id                                    | int         | int            | NO            |             |
| smColumnTemplate                 | label_id                                          | int         | int            | NO            |             |
| smColumnTemplate                 | module_id                                         | int         | int            | NO            |             |
| smColumnTemplate                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smColumnTemplate                 | sequence                                          | int         | int            | NO            |             |
| smColumnTemplate                 | tableType_id                                      | int         | int            | NO            |             |
| smColumnTemplate                 | type_id                                           | int         | int            | NO            |             |
| smColumnTemplate                 | visible                                           | varchar     | varchar(10)    | NO            |             |
| smColumnType                     | oid                                               | int         | int            | NO            | Primary Key |
| smColumnType                     | classoid                                          | int         | int            | NO            |             |
| smColumnType                     | description_id                                    | int         | int            | NO            |             |
| smColumnType                     | label_id                                          | int         | int            | NO            |             |
| smColumnType                     | module_id                                         | int         | int            | NO            |             |
| smColumnType                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smComProtocol                    | oid                                               | int         | int            | NO            | Primary Key |
| smComProtocol                    | classoid                                          | int         | int            | NO            |             |
| smComProtocol                    | description_id                                    | int         | int            | NO            |             |
| smComProtocol                    | label_id                                          | int         | int            | NO            |             |
| smComProtocol                    | module_id                                         | int         | int            | NO            |             |
| smComProtocol                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smComProtocol                    | type                                              | varchar     | varchar(255)   | NO            |             |
| smConfiguredSystem               | oid                                               | int         | int            | NO            | Primary Key |
| smConfiguredSystem               | applicationModel_id                               | int         | int            | NO            |             |
| smConfiguredSystem               | classoid                                          | int         | int            | NO            |             |
| smConfiguredSystem               | description                                       | text        | text           | NO            |             |
| smConfiguredSystem               | module_id                                         | int         | int            | NO            |             |
| smConfiguredSystem               | name                                              | varchar     | varchar(255)   | NO            |             |
| smConfiguredSystem               | system_id                                         | int         | int            | NO            |             |
| smContext                        | oid                                               | int         | int            | NO            | Primary Key |
| smContext                        | classoid                                          | int         | int            | NO            |             |
| smContext                        | description_id                                    | int         | int            | NO            |             |
| smContext                        | label_id                                          | int         | int            | NO            |             |
| smContext                        | module_id                                         | int         | int            | NO            |             |
| smContext                        | name                                              | varchar     | varchar(255)   | NO            |             |
| smContext                        | parent_id                                         | int         | int            | NO            |             |
| smContextAction                  | oid                                               | int         | int            | NO            | Primary Key |
| smContextAction                  | context_id                                        | int         | int            | NO            | Foreign Key |
| smContextAction                  | classoid                                          | int         | int            | NO            |             |
| smContextAction                  | contextObject_id                                  | int         | int            | NO            |             |
| smContextAction                  | createObjectRequest                               | varchar     | varchar(10)    | NO            |             |
| smContextAction                  | description_id                                    | int         | int            | NO            |             |
| smContextAction                  | label_id                                          | int         | int            | NO            |             |
| smContextAction                  | language_id                                       | int         | int            | NO            |             |
| smContextAction                  | module_id                                         | int         | int            | NO            |             |
| smContextAction                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smContextAction                  | objectDescription_id                              | int         | int            | NO            |             |
| smContextAction                  | objectLabel_id                                    | int         | int            | NO            |             |
| smContextAction                  | objectLabelMode                                   | varchar     | varchar(255)   | NO            |             |
| smContextAction                  | objectName                                        | varchar     | varchar(255)   | NO            |             |
| smContextAction                  | result_id                                         | int         | int            | NO            |             |
| smContextAction                  | scriptContextAction_id                            | int         | int            | NO            |             |
| smContextAction                  | service_id                                        | int         | int            | NO            |             |
| smContextActionParam             | oid                                               | int         | int            | NO            | Primary Key |
| smContextActionParam             | action_id                                         | int         | int            | NO            | Foreign Key |
| smContextActionParam             | classoid                                          | int         | int            | NO            |             |
| smContextActionParam             | derivationScript                                  | text        | text           | NO            |             |
| smContextActionParam             | description_id                                    | int         | int            | NO            |             |
| smContextActionParam             | direction                                         | varchar     | varchar(255)   | NO            |             |
| smContextActionParam             | label_id                                          | int         | int            | NO            |             |
| smContextActionParam             | module_id                                         | int         | int            | NO            |             |
| smContextActionParam             | name                                              | varchar     | varchar(255)   | NO            |             |
| smContextActionParam             | required                                          | varchar     | varchar(10)    | NO            |             |
| smContextActionParam             | scriptAccess                                      | varchar     | varchar(255)   | NO            |             |
| smContextActionParam             | scriptName                                        | varchar     | varchar(255)   | NO            |             |
| smContextActionParam             | type_id                                           | int         | int            | NO            |             |
| smContextClass                   | oid                                               | int         | int            | NO            | Primary Key |
| smContextClass                   | class_id                                          | int         | int            | NO            |             |
| smContextClass                   | classoid                                          | int         | int            | NO            |             |
| smContextClass                   | context_id                                        | int         | int            | NO            |             |
| smContextClass                   | description_id                                    | int         | int            | NO            |             |
| smContextClass                   | label_id                                          | int         | int            | NO            |             |
| smContextClass                   | module_id                                         | int         | int            | NO            |             |
| smContextClass                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smContextClass                   | paramAttribute_id                                 | int         | int            | NO            |             |
| smContextClass                   | paramClass_id                                     | int         | int            | NO            |             |
| smContextError                   | oid                                               | int         | int            | NO            | Primary Key |
| smContextError                   | action_id                                         | int         | int            | NO            |             |
| smContextError                   | classoid                                          | int         | int            | NO            |             |
| smContextError                   | context_id                                        | int         | int            | NO            |             |
| smContextError                   | description_id                                    | int         | int            | NO            |             |
| smContextError                   | label_id                                          | int         | int            | NO            |             |
| smContextError                   | module_id                                         | int         | int            | NO            |             |
| smContextError                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smCron                           | oid                                               | int         | int            | NO            | Primary Key |
| smCron                           | classoid                                          | int         | int            | NO            |             |
| smCron                           | description_id                                    | int         | int            | NO            |             |
| smCron                           | frequency                                         | varchar     | varchar(255)   | NO            |             |
| smCron                           | frequency_id                                      | int         | int            | NO            |             |
| smCron                           | label_id                                          | int         | int            | NO            |             |
| smCron                           | module_id                                         | int         | int            | NO            |             |
| smCron                           | name                                              | varchar     | varchar(255)   | NO            |             |
| smCron                           | reference_id                                      | int         | int            | NO            |             |
| smCron                           | scheduler_id                                      | int         | int            | NO            |             |
| smCron                           | status                                            | varchar     | varchar(255)   | NO            |             |
| smCron                           | type                                              | varchar     | varchar(255)   | NO            |             |
| smCronFrequency                  | oid                                               | int         | int            | NO            | Primary Key |
| smCronFrequency                  | classoid                                          | int         | int            | NO            |             |
| smCronFrequency                  | description_id                                    | int         | int            | NO            |             |
| smCronFrequency                  | frequency                                         | varchar     | varchar(255)   | NO            |             |
| smCronFrequency                  | label_id                                          | int         | int            | NO            |             |
| smCronFrequency                  | module_id                                         | int         | int            | NO            |             |
| smCronFrequency                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smCronScheduler                  | oid                                               | int         | int            | NO            | Primary Key |
| smCronScheduler                  | classoid                                          | int         | int            | NO            |             |
| smCronScheduler                  | delayedStart                                      | int         | int            | NO            |             |
| smCronScheduler                  | description_id                                    | int         | int            | NO            |             |
| smCronScheduler                  | label_id                                          | int         | int            | NO            |             |
| smCronScheduler                  | mode                                              | varchar     | varchar(255)   | NO            |             |
| smCronScheduler                  | module_id                                         | int         | int            | NO            |             |
| smCronScheduler                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smCronScheduler                  | priority                                          | varchar     | varchar(255)   | NO            |             |
| smCronScheduler                  | threadCount                                       | int         | int            | NO            |             |
| smCronScheduler                  | type                                              | varchar     | varchar(255)   | NO            |             |
| smCurrentModule                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| smCurrentModule                  | buildDate                                         | datetime    | datetime       | NO            |             |
| smCurrentModule                  | buildNo                                           | int         | int            | NO            |             |
| smCurrentModule                  | classoid                                          | int         | int            | NO            |             |
| smCurrentModule                  | lastModified                                      | char        | char(36)       | NO            |             |
| smCurrentModule                  | module_id                                         | int         | int            | NO            |             |
| smCurrentModule                  | moduleVersion_id                                  | int         | int            | NO            |             |
| smCurrentModule                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smCurrentModule                  | status                                            | varchar     | varchar(255)   | NO            |             |
| smCurrentModule                  | timestamp                                         | varchar     | varchar(255)   | NO            |             |
| smCurrentModule                  | version                                           | varchar     | varchar(255)   | NO            |             |
| smCustomAttribute                | oid                                               | int         | int            | NO            | Primary Key |
| smCustomAttribute                | attribute_id                                      | int         | int            | NO            |             |
| smCustomAttribute                | classoid                                          | int         | int            | NO            |             |
| smCustomAttribute                | datasource_id                                     | int         | int            | NO            |             |
| smCustomAttribute                | defaultValue                                      | varchar     | varchar(255)   | NO            |             |
| smCustomAttribute                | description_id                                    | int         | int            | NO            |             |
| smCustomAttribute                | label_id                                          | int         | int            | NO            |             |
| smCustomAttribute                | module_id                                         | int         | int            | NO            |             |
| smCustomAttribute                | name                                              | varchar     | varchar(255)   | NO            |             |
| smCustomAttribute                | object_id                                         | int         | int            | NO            |             |
| smCustomAttribute                | type_id                                           | int         | int            | NO            |             |
| smCustomAttributeValue           | oid                                               | int         | int            | NO            | Primary Key |
| smCustomAttributeValue           | object_id                                         | int         | int            | NO            | Foreign Key |
| smCustomAttributeValue           | attribute_id                                      | int         | int            | NO            |             |
| smCustomAttributeValue           | classoid                                          | int         | int            | NO            |             |
| smCustomAttributeValue           | custom_id                                         | int         | int            | NO            |             |
| smCustomAttributeValue           | module_id                                         | int         | int            | NO            |             |
| smCustomAttributeValue           | value                                             | text        | text           | NO            |             |
| smCustomizedObject               | oid                                               | int         | int            | NO            | Primary Key |
| smCustomizedObject               | classoid                                          | int         | int            | NO            |             |
| smCustomizedObject               | customizationCount                                | int         | int            | NO            |             |
| smCustomizedObject               | description_id                                    | int         | int            | NO            |             |
| smCustomizedObject               | feature_id                                        | int         | int            | NO            |             |
| smCustomizedObject               | label_id                                          | int         | int            | NO            |             |
| smCustomizedObject               | module_id                                         | int         | int            | NO            |             |
| smCustomizedObject               | name                                              | varchar     | varchar(255)   | NO            |             |
| smCustomizedObject               | object_id                                         | int         | int            | NO            |             |
| smCustomizedObject               | source_id                                         | int         | int            | NO            |             |
| smCustomizedObject               | status                                            | varchar     | varchar(255)   | NO            |             |
| smCustomizedObject               | type_id                                           | int         | int            | NO            |             |
| smDataGroup                      | oid                                               | int         | int            | NO            | Primary Key |
| smDataGroup                      | classoid                                          | int         | int            | NO            |             |
| smDataGroup                      | datastore_id                                      | int         | int            | NO            |             |
| smDataGroup                      | defaultGroup                                      | varchar     | varchar(10)    | NO            |             |
| smDataGroup                      | description_id                                    | int         | int            | NO            |             |
| smDataGroup                      | label_id                                          | int         | int            | NO            |             |
| smDataGroup                      | location_id                                       | int         | int            | NO            |             |
| smDataGroup                      | module_id                                         | int         | int            | NO            |             |
| smDataGroup                      | name                                              | varchar     | varchar(255)   | NO            |             |
| smDataGroup                      | type_id                                           | int         | int            | NO            |             |
| smDataGroupLocation              | oid                                               | int         | int            | NO            | Primary Key |
| smDataGroupLocation              | classoid                                          | int         | int            | NO            |             |
| smDataGroupLocation              | dataGroup_id                                      | int         | int            | NO            |             |
| smDataGroupLocation              | datastoreConf_id                                  | int         | int            | NO            |             |
| smDataGroupLocation              | location_id                                       | int         | int            | NO            |             |
| smDataGroupLocation              | module_id                                         | int         | int            | NO            |             |
| smDataGroupLocation              | partition_id                                      | int         | int            | NO            |             |
| smDataGroupType                  | oid                                               | int         | int            | NO            | Primary Key |
| smDataGroupType                  | classoid                                          | int         | int            | NO            |             |
| smDataGroupType                  | description_id                                    | int         | int            | NO            |             |
| smDataGroupType                  | label_id                                          | int         | int            | NO            |             |
| smDataGroupType                  | module_id                                         | int         | int            | NO            |             |
| smDataGroupType                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smDataMask                       | oid                                               | int         | int            | NO            | Primary Key |
| smDataMask                       | classoid                                          | int         | int            | NO            |             |
| smDataMask                       | description_id                                    | int         | int            | NO            |             |
| smDataMask                       | format                                            | varchar     | varchar(255)   | NO            |             |
| smDataMask                       | label_id                                          | int         | int            | NO            |             |
| smDataMask                       | module_id                                         | int         | int            | NO            |             |
| smDataMask                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smDataMask                       | type_id                                           | int         | int            | NO            |             |
| smDataMaskType                   | oid                                               | int         | int            | NO            | Primary Key |
| smDataMaskType                   | classoid                                          | int         | int            | NO            |             |
| smDataMaskType                   | description_id                                    | int         | int            | NO            |             |
| smDataMaskType                   | label_id                                          | int         | int            | NO            |             |
| smDataMaskType                   | module_id                                         | int         | int            | NO            |             |
| smDataMaskType                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smDataMaskTypeParam              | oid                                               | int         | int            | NO            | Primary Key |
| smDataMaskTypeParam              | classoid                                          | int         | int            | NO            |             |
| smDataMaskTypeParam              | dataMaskType_id                                   | int         | int            | NO            |             |
| smDataMaskTypeParam              | description_id                                    | int         | int            | NO            |             |
| smDataMaskTypeParam              | label_id                                          | int         | int            | NO            |             |
| smDataMaskTypeParam              | module_id                                         | int         | int            | NO            |             |
| smDataMaskTypeParam              | name                                              | varchar     | varchar(255)   | NO            |             |
| smDataMaskTypeParam              | type_id                                           | int         | int            | NO            |             |
| smDataPartition                  | oid                                               | int         | int            | NO            | Primary Key |
| smDataPartition                  | classoid                                          | int         | int            | NO            |             |
| smDataPartition                  | dataGroup_id                                      | int         | int            | NO            |             |
| smDataPartition                  | description_id                                    | int         | int            | NO            |             |
| smDataPartition                  | label_id                                          | int         | int            | NO            |             |
| smDataPartition                  | module_id                                         | int         | int            | NO            |             |
| smDataPartition                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smDataPartition                  | partitionNo                                       | int         | int            | NO            |             |
| smDataPartition                  | type_id                                           | int         | int            | NO            |             |
| smDataPartitionType              | oid                                               | int         | int            | NO            | Primary Key |
| smDataPartitionType              | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smDataPartitionType              | classoid                                          | int         | int            | NO            |             |
| smDataPartitionType              | description_id                                    | int         | int            | NO            |             |
| smDataPartitionType              | label_id                                          | int         | int            | NO            |             |
| smDataPartitionType              | module_id                                         | int         | int            | NO            |             |
| smDataTypeColumn                 | oid                                               | int         | int            | NO            | Primary Key |
| smDataTypeColumn                 | classoid                                          | int         | int            | NO            |             |
| smDataTypeColumn                 | columntype_id                                     | int         | int            | NO            |             |
| smDataTypeColumn                 | datatype_id                                       | int         | int            | NO            |             |
| smDataTypeColumn                 | module_id                                         | int         | int            | NO            |             |
| smDatastore                      | oid                                               | int         | int            | NO            | Primary Key |
| smDatastore                      | applicationModel_id                               | int         | int            | NO            |             |
| smDatastore                      | classoid                                          | int         | int            | NO            |             |
| smDatastore                      | defaultAPI_id                                     | int         | int            | NO            |             |
| smDatastore                      | description_id                                    | int         | int            | NO            |             |
| smDatastore                      | label_id                                          | int         | int            | NO            |             |
| smDatastore                      | module_id                                         | int         | int            | NO            |             |
| smDatastore                      | name                                              | varchar     | varchar(255)   | NO            |             |
| smDatastore                      | type_id                                           | int         | int            | NO            |             |
| smDatastoreAPI                   | oid                                               | int         | int            | NO            | Primary Key |
| smDatastoreAPI                   | classoid                                          | int         | int            | NO            |             |
| smDatastoreAPI                   | datastore_id                                      | int         | int            | NO            |             |
| smDatastoreAPI                   | module_id                                         | int         | int            | NO            |             |
| smDatastoreAPI                   | persistenceAPI_id                                 | int         | int            | NO            |             |
| smDatastoreConf                  | oid                                               | int         | int            | NO            | Primary Key |
| smDatastoreConf                  | classoid                                          | int         | int            | NO            |             |
| smDatastoreConf                  | datastore_id                                      | int         | int            | NO            |             |
| smDatastoreConf                  | datastoreAPI_id                                   | int         | int            | NO            |             |
| smDatastoreConf                  | description_id                                    | int         | int            | NO            |             |
| smDatastoreConf                  | label_id                                          | int         | int            | NO            |             |
| smDatastoreConf                  | module_id                                         | int         | int            | NO            |             |
| smDatastoreConf                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smDatastoreConf                  | storageEngine_id                                  | int         | int            | NO            |             |
| smDatastoreInstance              | oid                                               | int         | int            | NO            | Primary Key |
| smDatastoreInstance              | classoid                                          | int         | int            | NO            |             |
| smDatastoreInstance              | datastore_id                                      | int         | int            | NO            |             |
| smDatastoreInstance              | datastoreConf_id                                  | int         | int            | NO            |             |
| smDatastoreInstance              | instance_id                                       | int         | int            | NO            |             |
| smDatastoreInstance              | module_id                                         | int         | int            | NO            |             |
| smDatastoreLocation              | oid                                               | int         | int            | NO            | Primary Key |
| smDatastoreLocation              | classoid                                          | int         | int            | NO            |             |
| smDatastoreLocation              | datastoreConf_id                                  | int         | int            | NO            |             |
| smDatastoreLocation              | description_id                                    | int         | int            | NO            |             |
| smDatastoreLocation              | label_id                                          | int         | int            | NO            |             |
| smDatastoreLocation              | module_id                                         | int         | int            | NO            |             |
| smDatastoreLocation              | name                                              | varchar     | varchar(255)   | NO            |             |
| smDatastorePartitionType         | oid                                               | int         | int            | NO            | Primary Key |
| smDatastorePartitionType         | classoid                                          | int         | int            | NO            |             |
| smDatastorePartitionType         | datastoreConf_id                                  | int         | int            | NO            |             |
| smDatastorePartitionType         | module_id                                         | int         | int            | NO            |             |
| smDatastorePartitionType         | partitionType_id                                  | int         | int            | NO            |             |
| smDatePreset                     | oid                                               | int         | int            | NO            | Primary Key |
| smDatePreset                     | classoid                                          | int         | int            | NO            |             |
| smDatePreset                     | label_id                                          | int         | int            | NO            |             |
| smDatePreset                     | module_id                                         | int         | int            | NO            |             |
| smDatePreset                     | parent_id                                         | int         | int            | NO            |             |
| smDatePreset                     | relativeDate_id                                   | int         | int            | NO            |             |
| smDatePreset                     | sequence                                          | int         | int            | NO            |             |
| smDeviceModel                    | oid                                               | int         | int            | NO            | Primary Key |
| smDeviceModel                    | classoid                                          | int         | int            | NO            |             |
| smDeviceModel                    | description_id                                    | int         | int            | NO            |             |
| smDeviceModel                    | label_id                                          | int         | int            | NO            |             |
| smDeviceModel                    | module_id                                         | int         | int            | NO            |             |
| smDeviceModel                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smDeviceModel                    | protocol_id                                       | int         | int            | NO            |             |
| smDeviceModel                    | type_id                                           | int         | int            | NO            |             |
| smDeviceProtocol                 | oid                                               | int         | int            | NO            | Primary Key |
| smDeviceProtocol                 | classoid                                          | int         | int            | NO            |             |
| smDeviceProtocol                 | description_id                                    | int         | int            | NO            |             |
| smDeviceProtocol                 | label_id                                          | int         | int            | NO            |             |
| smDeviceProtocol                 | module_id                                         | int         | int            | NO            |             |
| smDeviceProtocol                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smDiagnostic                     | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnostic                     | classoid                                          | int         | int            | NO            |             |
| smDiagnostic                     | description_id                                    | int         | int            | NO            |             |
| smDiagnostic                     | label_id                                          | int         | int            | NO            |             |
| smDiagnostic                     | module_id                                         | int         | int            | NO            |             |
| smDiagnostic                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smDiagnostic                     | unit_id                                           | int         | int            | NO            |             |
| smDiagnosticGranularity          | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnosticGranularity          | diagnostic_id                                     | int         | int            | NO            | Foreign Key |
| smDiagnosticGranularity          | classoid                                          | int         | int            | NO            |             |
| smDiagnosticGranularity          | description_id                                    | int         | int            | NO            |             |
| smDiagnosticGranularity          | label_id                                          | int         | int            | NO            |             |
| smDiagnosticGranularity          | module_id                                         | int         | int            | NO            |             |
| smDiagnosticGranularity          | name                                              | varchar     | varchar(255)   | NO            |             |
| smDiagnosticGranularity          | sequence                                          | int         | int            | NO            |             |
| smDiagnosticInstance             | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnosticInstance             | active                                            | varchar     | varchar(10)    | NO            |             |
| smDiagnosticInstance             | classoid                                          | int         | int            | NO            |             |
| smDiagnosticInstance             | description_id                                    | int         | int            | NO            |             |
| smDiagnosticInstance             | diagnostic_id                                     | int         | int            | NO            |             |
| smDiagnosticInstance             | diagnosticGroup_id                                | int         | int            | NO            |             |
| smDiagnosticInstance             | label_id                                          | int         | int            | NO            |             |
| smDiagnosticInstance             | module_id                                         | int         | int            | NO            |             |
| smDiagnosticInstance             | name                                              | varchar     | varchar(255)   | NO            |             |
| smDiagnosticInstance             | overrideThreshold                                 | varchar     | varchar(10)    | NO            |             |
| smDiagnosticInstanceCron         | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnosticInstanceCron         | classoid                                          | int         | int            | NO            |             |
| smDiagnosticInstanceCron         | cron_id                                           | int         | int            | NO            |             |
| smDiagnosticInstanceCron         | instance_id                                       | int         | int            | NO            |             |
| smDiagnosticInstanceCron         | module_id                                         | int         | int            | NO            |             |
| smDiagnosticInstanceCron         | sequence                                          | int         | int            | NO            |             |
| smDiagnosticIssueType            | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnosticIssueType            | classoid                                          | int         | int            | NO            |             |
| smDiagnosticIssueType            | defaultResolution_id                              | int         | int            | NO            |             |
| smDiagnosticIssueType            | description_id                                    | int         | int            | NO            |             |
| smDiagnosticIssueType            | diagnostic_id                                     | int         | int            | NO            |             |
| smDiagnosticIssueType            | label_id                                          | int         | int            | NO            |             |
| smDiagnosticIssueType            | module_id                                         | int         | int            | NO            |             |
| smDiagnosticIssueType            | name                                              | varchar     | varchar(255)   | NO            |             |
| smDiagnosticIssueType            | resolutionMode                                    | varchar     | varchar(255)   | NO            |             |
| smDiagnosticIssueTypeParam       | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnosticIssueTypeParam       | classoid                                          | int         | int            | NO            |             |
| smDiagnosticIssueTypeParam       | description_id                                    | int         | int            | NO            |             |
| smDiagnosticIssueTypeParam       | issueType_id                                      | int         | int            | NO            |             |
| smDiagnosticIssueTypeParam       | label_id                                          | int         | int            | NO            |             |
| smDiagnosticIssueTypeParam       | module_id                                         | int         | int            | NO            |             |
| smDiagnosticIssueTypeParam       | name                                              | varchar     | varchar(255)   | NO            |             |
| smDiagnosticIssueTypeParam       | type_id                                           | int         | int            | NO            |             |
| smDiagnosticResolution           | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnosticResolution           | classoid                                          | int         | int            | NO            |             |
| smDiagnosticResolution           | description_id                                    | int         | int            | NO            |             |
| smDiagnosticResolution           | issueType_id                                      | int         | int            | NO            |             |
| smDiagnosticResolution           | label_id                                          | int         | int            | NO            |             |
| smDiagnosticResolution           | module_id                                         | int         | int            | NO            |             |
| smDiagnosticResolution           | name                                              | varchar     | varchar(255)   | NO            |             |
| smDiagnosticThreshold            | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnosticThreshold            | archiveResult                                     | varchar     | varchar(10)    | NO            |             |
| smDiagnosticThreshold            | classoid                                          | int         | int            | NO            |             |
| smDiagnosticThreshold            | diagnostic_id                                     | int         | int            | NO            |             |
| smDiagnosticThreshold            | instance_id                                       | int         | int            | NO            |             |
| smDiagnosticThreshold            | maximumValue                                      | decimal     | decimal(19,2)  | NO            |             |
| smDiagnosticThreshold            | message_id                                        | int         | int            | NO            |             |
| smDiagnosticThreshold            | messageLevel_id                                   | int         | int            | NO            |             |
| smDiagnosticThreshold            | minimumValue                                      | decimal     | decimal(19,2)  | NO            |             |
| smDiagnosticThreshold            | module_id                                         | int         | int            | NO            |             |
| smDiagnosticUnit                 | oid                                               | int         | int            | NO            | Primary Key |
| smDiagnosticUnit                 | classoid                                          | int         | int            | NO            |             |
| smDiagnosticUnit                 | description_id                                    | int         | int            | NO            |             |
| smDiagnosticUnit                 | label_id                                          | int         | int            | NO            |             |
| smDiagnosticUnit                 | module_id                                         | int         | int            | NO            |             |
| smDiagnosticUnit                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smDiagnosticUnit                 | symbol                                            | varchar     | varchar(255)   | NO            |             |
| smDictionary                     | oid                                               | int         | int            | NO            | Primary Key |
| smDictionary                     | classoid                                          | int         | int            | NO            |             |
| smDictionary                     | description_id                                    | int         | int            | NO            |             |
| smDictionary                     | label_id                                          | int         | int            | NO            |             |
| smDictionary                     | module_id                                         | int         | int            | NO            |             |
| smDictionary                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smDictionaryItem                 | oid                                               | int         | int            | NO            | Primary Key |
| smDictionaryItem                 | classoid                                          | int         | int            | NO            |             |
| smDictionaryItem                 | description_id                                    | int         | int            | NO            |             |
| smDictionaryItem                 | dictionary_id                                     | int         | int            | NO            |             |
| smDictionaryItem                 | label_id                                          | int         | int            | NO            |             |
| smDictionaryItem                 | module_id                                         | int         | int            | NO            |             |
| smDictionaryItem                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocSectionType                 | oid                                               | int         | int            | NO            | Primary Key |
| smDocSectionType                 | bottomleft_id                                     | int         | int            | NO            |             |
| smDocSectionType                 | bottomright_id                                    | int         | int            | NO            |             |
| smDocSectionType                 | classoid                                          | int         | int            | NO            |             |
| smDocSectionType                 | description_id                                    | int         | int            | NO            |             |
| smDocSectionType                 | label_id                                          | int         | int            | NO            |             |
| smDocSectionType                 | language_id                                       | int         | int            | NO            |             |
| smDocSectionType                 | module_id                                         | int         | int            | NO            |             |
| smDocSectionType                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocSectionType                 | orientation                                       | varchar     | varchar(255)   | NO            |             |
| smDocSectionType                 | topleft_id                                        | int         | int            | NO            |             |
| smDocSectionType                 | topright_id                                       | int         | int            | NO            |             |
| smDocStylesheet                  | oid                                               | int         | int            | NO            | Primary Key |
| smDocStylesheet                  | classoid                                          | int         | int            | NO            |             |
| smDocStylesheet                  | document_id                                       | int         | int            | NO            |             |
| smDocStylesheet                  | format_id                                         | int         | int            | NO            |             |
| smDocStylesheet                  | module_id                                         | int         | int            | NO            |             |
| smDocStylesheet                  | stylesheet                                        | text        | text           | NO            |             |
| smDocTemplateType                | oid                                               | int         | int            | NO            | Primary Key |
| smDocTemplateType                | classoid                                          | int         | int            | NO            |             |
| smDocTemplateType                | coverPage_id                                      | int         | int            | NO            |             |
| smDocTemplateType                | description_id                                    | int         | int            | NO            |             |
| smDocTemplateType                | folder_id                                         | int         | int            | NO            |             |
| smDocTemplateType                | format_id                                         | int         | int            | NO            |             |
| smDocTemplateType                | label_id                                          | int         | int            | NO            |             |
| smDocTemplateType                | module_id                                         | int         | int            | NO            |             |
| smDocTemplateType                | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocTemplateType                | repository_id                                     | int         | int            | NO            |             |
| smDocTemplateType                | tableOfContents_id                                | int         | int            | NO            |             |
| smDocument                       | oid                                               | int         | int            | NO            | Primary Key |
| smDocument                       | classoid                                          | int         | int            | NO            |             |
| smDocument                       | defaultAttribute_id                               | int         | int            | NO            |             |
| smDocument                       | description_id                                    | int         | int            | NO            |             |
| smDocument                       | fileName                                          | varchar     | varchar(255)   | NO            |             |
| smDocument                       | filetype_id                                       | int         | int            | NO            |             |
| smDocument                       | folder_id                                         | int         | int            | NO            |             |
| smDocument                       | label_id                                          | int         | int            | NO            |             |
| smDocument                       | language                                          | varchar     | varchar(255)   | NO            |             |
| smDocument                       | module_id                                         | int         | int            | NO            |             |
| smDocument                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocument                       | owner_id                                          | int         | int            | NO            |             |
| smDocument                       | parent_id                                         | int         | int            | NO            |             |
| smDocument                       | referenceId                                       | char        | char(36)       | NO            |             |
| smDocument                       | repository_id                                     | int         | int            | NO            |             |
| smDocument                       | status                                            | varchar     | varchar(255)   | NO            |             |
| smDocument                       | title_id                                          | int         | int            | NO            |             |
| smDocument                       | type_id                                           | int         | int            | NO            |             |
| smDocument                       | version                                           | int         | int            | NO            |             |
| smDocumentAttribute              | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentAttribute              | classoid                                          | int         | int            | NO            |             |
| smDocumentAttribute              | defaultValue                                      | varchar     | varchar(255)   | NO            |             |
| smDocumentAttribute              | description_id                                    | int         | int            | NO            |             |
| smDocumentAttribute              | document_id                                       | int         | int            | NO            |             |
| smDocumentAttribute              | label_id                                          | int         | int            | NO            |             |
| smDocumentAttribute              | module_id                                         | int         | int            | NO            |             |
| smDocumentAttribute              | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentAttribute              | section_id                                        | int         | int            | NO            |             |
| smDocumentAttribute              | type_id                                           | int         | int            | NO            |             |
| smDocumentDef                    | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentDef                    | classoid                                          | int         | int            | NO            |             |
| smDocumentDef                    | delimiter                                         | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | description_id                                    | int         | int            | NO            |             |
| smDocumentDef                    | docName                                           | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | docSchema                                         | text        | text           | NO            |             |
| smDocumentDef                    | enclosure                                         | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | encoding                                          | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | example                                           | text        | text           | NO            |             |
| smDocumentDef                    | headerType                                        | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | label_id                                          | int         | int            | NO            |             |
| smDocumentDef                    | lineSeparator                                     | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | module_id                                         | int         | int            | NO            |             |
| smDocumentDef                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | namespace_id                                      | int         | int            | NO            |             |
| smDocumentDef                    | notes_id                                          | int         | int            | NO            |             |
| smDocumentDef                    | owner_id                                          | int         | int            | NO            |             |
| smDocumentDef                    | query_id                                          | int         | int            | NO            |             |
| smDocumentDef                    | reference_id                                      | int         | int            | NO            |             |
| smDocumentDef                    | status                                            | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | strictMode                                        | varchar     | varchar(255)   | NO            |             |
| smDocumentDef                    | type_id                                           | int         | int            | NO            |             |
| smDocumentDefChild               | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentDefChild               | document_id                                       | int         | int            | NO            | Foreign Key |
| smDocumentDefChild               | appField                                          | varchar     | varchar(255)   | NO            |             |
| smDocumentDefChild               | classoid                                          | int         | int            | NO            |             |
| smDocumentDefChild               | column_id                                         | int         | int            | NO            |             |
| smDocumentDefChild               | defaultValue                                      | varchar     | varchar(255)   | NO            |             |
| smDocumentDefChild               | description_id                                    | int         | int            | NO            |             |
| smDocumentDefChild               | exampleValue                                      | varchar     | varchar(255)   | NO            |             |
| smDocumentDefChild               | hostField                                         | varchar     | varchar(255)   | NO            |             |
| smDocumentDefChild               | label_id                                          | int         | int            | NO            |             |
| smDocumentDefChild               | maxOccurrence                                     | int         | int            | NO            |             |
| smDocumentDefChild               | module_id                                         | int         | int            | NO            |             |
| smDocumentDefChild               | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentDefChild               | namespace_id                                      | int         | int            | NO            |             |
| smDocumentDefChild               | noderef_id                                        | int         | int            | NO            |             |
| smDocumentDefChild               | notes_id                                          | int         | int            | NO            |             |
| smDocumentDefChild               | parent_id                                         | int         | int            | NO            |             |
| smDocumentDefChild               | path                                              | text        | text           | NO            |             |
| smDocumentDefChild               | reference_id                                      | int         | int            | NO            |             |
| smDocumentDefChild               | required                                          | varchar     | varchar(10)    | NO            |             |
| smDocumentDefChild               | sequence                                          | int         | int            | NO            |             |
| smDocumentDefChild               | type                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentDefChild               | visible                                           | varchar     | varchar(10)    | NO            |             |
| smDocumentDefChildRel            | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentDefChildRel            | child_id                                          | int         | int            | NO            |             |
| smDocumentDefChildRel            | classoid                                          | int         | int            | NO            |             |
| smDocumentDefChildRel            | module_id                                         | int         | int            | NO            |             |
| smDocumentDefChildRel            | object_id                                         | int         | int            | NO            |             |
| smDocumentDefChildRel            | value                                             | text        | text           | NO            |             |
| smDocumentDefRel                 | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentDefRel                 | classoid                                          | int         | int            | NO            |             |
| smDocumentDefRel                 | document_id                                       | int         | int            | NO            |             |
| smDocumentDefRel                 | module_id                                         | int         | int            | NO            |             |
| smDocumentDefRel                 | object_id                                         | int         | int            | NO            |             |
| smDocumentDefRel                 | type                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentDefRel                 | version                                           | varchar     | varchar(255)   | NO            |             |
| smDocumentDefType                | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentDefType                | classoid                                          | int         | int            | NO            |             |
| smDocumentDefType                | description_id                                    | int         | int            | NO            |             |
| smDocumentDefType                | format                                            | varchar     | varchar(255)   | NO            |             |
| smDocumentDefType                | label_id                                          | int         | int            | NO            |             |
| smDocumentDefType                | module_id                                         | int         | int            | NO            |             |
| smDocumentDefType                | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentDefType                | type                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentFormat                 | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentFormat                 | classoid                                          | int         | int            | NO            |             |
| smDocumentFormat                 | description_id                                    | int         | int            | NO            |             |
| smDocumentFormat                 | filetype_id                                       | int         | int            | NO            |             |
| smDocumentFormat                 | label_id                                          | int         | int            | NO            |             |
| smDocumentFormat                 | module_id                                         | int         | int            | NO            |             |
| smDocumentFormat                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentLanguage               | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentLanguage               | classoid                                          | int         | int            | NO            |             |
| smDocumentLanguage               | description_id                                    | int         | int            | NO            |             |
| smDocumentLanguage               | label_id                                          | int         | int            | NO            |             |
| smDocumentLanguage               | module_id                                         | int         | int            | NO            |             |
| smDocumentLanguage               | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentSection                | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentSection                | classoid                                          | int         | int            | NO            |             |
| smDocumentSection                | description_id                                    | int         | int            | NO            |             |
| smDocumentSection                | docref_id                                         | int         | int            | NO            |             |
| smDocumentSection                | document_id                                       | int         | int            | NO            |             |
| smDocumentSection                | hidden                                            | varchar     | varchar(10)    | NO            |             |
| smDocumentSection                | label_id                                          | int         | int            | NO            |             |
| smDocumentSection                | language_id                                       | int         | int            | NO            |             |
| smDocumentSection                | module_id                                         | int         | int            | NO            |             |
| smDocumentSection                | name                                              | varchar     | varchar(255)   | NO            |             |
| smDocumentSection                | notes_id                                          | int         | int            | NO            |             |
| smDocumentSection                | numberingMode                                     | varchar     | varchar(255)   | NO            |             |
| smDocumentSection                | orientation                                       | varchar     | varchar(255)   | NO            |             |
| smDocumentSection                | pageBreak                                         | varchar     | varchar(255)   | NO            |             |
| smDocumentSection                | parent_id                                         | int         | int            | NO            |             |
| smDocumentSection                | readOnly                                          | varchar     | varchar(10)    | NO            |             |
| smDocumentSection                | section                                           | varchar     | varchar(255)   | NO            |             |
| smDocumentSection                | sectionref_id                                     | int         | int            | NO            |             |
| smDocumentSection                | sequence                                          | int         | int            | NO            |             |
| smDocumentSection                | type_id                                           | int         | int            | NO            |             |
| smDocumentVarType                | oid                                               | int         | int            | NO            | Primary Key |
| smDocumentVarType                | classoid                                          | int         | int            | NO            |             |
| smDocumentVarType                | defaultValue_id                                   | int         | int            | NO            |             |
| smDocumentVarType                | description_id                                    | int         | int            | NO            |             |
| smDocumentVarType                | document_id                                       | int         | int            | NO            |             |
| smDocumentVarType                | format_id                                         | int         | int            | NO            |             |
| smDocumentVarType                | label_id                                          | int         | int            | NO            |             |
| smDocumentVarType                | module_id                                         | int         | int            | NO            |             |
| smDocumentVarType                | name                                              | varchar     | varchar(255)   | NO            |             |
| smEmailSettings                  | oid                                               | int         | int            | NO            | Primary Key |
| smEmailSettings                  | classoid                                          | int         | int            | NO            |             |
| smEmailSettings                  | encryption                                        | varchar     | varchar(255)   | NO            |             |
| smEmailSettings                  | hostName                                          | varchar     | varchar(255)   | NO            |             |
| smEmailSettings                  | module_id                                         | int         | int            | NO            |             |
| smEmailSettings                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smEmailSettings                  | port                                              | int         | int            | NO            |             |
| smEndpointTypeRecipientType      | oid                                               | int         | int            | NO            | Primary Key |
| smEndpointTypeRecipientType      | classoid                                          | int         | int            | NO            |             |
| smEndpointTypeRecipientType      | endpointType_id                                   | int         | int            | NO            |             |
| smEndpointTypeRecipientType      | module_id                                         | int         | int            | NO            |             |
| smEndpointTypeRecipientType      | recipientType_id                                  | int         | int            | NO            |             |
| smEnumerationGroupItem           | oid                                               | int         | int            | NO            | Primary Key |
| smEnumerationGroupItem           | classoid                                          | int         | int            | NO            |             |
| smEnumerationGroupItem           | enumerationGroup_id                               | int         | int            | NO            |             |
| smEnumerationGroupItem           | item_id                                           | int         | int            | NO            |             |
| smEnumerationGroupItem           | module_id                                         | int         | int            | NO            |             |
| smEnumerationValue               | oid                                               | int         | int            | NO            | Primary Key |
| smEnumerationValue               | enumeration_id                                    | int         | int            | NO            | Foreign Key |
| smEnumerationValue               | classoid                                          | int         | int            | NO            |             |
| smEnumerationValue               | description_id                                    | int         | int            | NO            |             |
| smEnumerationValue               | label_id                                          | int         | int            | NO            |             |
| smEnumerationValue               | module_id                                         | int         | int            | NO            |             |
| smEnumerationValue               | name                                              | varchar     | varchar(255)   | NO            |             |
| smEnumerationValue               | sequence                                          | int         | int            | NO            |             |
| smEnumerationValue               | value                                             | varchar     | varchar(255)   | NO            |             |
| smExecutionPool                  | oid                                               | int         | int            | NO            | Primary Key |
| smExecutionPool                  | active                                            | varchar     | varchar(10)    | NO            |             |
| smExecutionPool                  | cancellation                                      | varchar     | varchar(255)   | NO            |             |
| smExecutionPool                  | classoid                                          | int         | int            | NO            |             |
| smExecutionPool                  | description_id                                    | int         | int            | NO            |             |
| smExecutionPool                  | interruptible                                     | varchar     | varchar(10)    | NO            |             |
| smExecutionPool                  | label_id                                          | int         | int            | NO            |             |
| smExecutionPool                  | maxItems                                          | int         | int            | NO            |             |
| smExecutionPool                  | maxItemsPerGroup                                  | int         | int            | NO            |             |
| smExecutionPool                  | module_id                                         | int         | int            | NO            |             |
| smExecutionPool                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smExecutionPool                  | scheduler_id                                      | int         | int            | NO            |             |
| smExecutionPool                  | strategy_id                                       | int         | int            | NO            |             |
| smExecutionPool                  | type_id                                           | int         | int            | NO            |             |
| smExecutionPoolType              | oid                                               | int         | int            | NO            | Primary Key |
| smExecutionPoolType              | classoid                                          | int         | int            | NO            |             |
| smExecutionPoolType              | description_id                                    | int         | int            | NO            |             |
| smExecutionPoolType              | label_id                                          | int         | int            | NO            |             |
| smExecutionPoolType              | module_id                                         | int         | int            | NO            |             |
| smExecutionPoolType              | name                                              | varchar     | varchar(255)   | NO            |             |
| smExecutionPoolTypeAction        | oid                                               | int         | int            | NO            | Primary Key |
| smExecutionPoolTypeAction        | action_id                                         | int         | int            | NO            |             |
| smExecutionPoolTypeAction        | classoid                                          | int         | int            | NO            |             |
| smExecutionPoolTypeAction        | module_id                                         | int         | int            | NO            |             |
| smExecutionPoolTypeAction        | type_id                                           | int         | int            | NO            |             |
| smExportField                    | oid                                               | int         | int            | NO            | Primary Key |
| smExportField                    | classoid                                          | int         | int            | NO            |             |
| smExportField                    | description_id                                    | int         | int            | NO            |             |
| smExportField                    | label_id                                          | int         | int            | NO            |             |
| smExportField                    | module_id                                         | int         | int            | NO            |             |
| smExportField                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smExportField                    | trigger_id                                        | int         | int            | NO            |             |
| smExportField                    | type_id                                           | int         | int            | NO            |             |
| smExportTrigger                  | oid                                               | int         | int            | NO            | Primary Key |
| smExportTrigger                  | active                                            | varchar     | varchar(10)    | NO            |             |
| smExportTrigger                  | classoid                                          | int         | int            | NO            |             |
| smExportTrigger                  | defaultdoc_id                                     | int         | int            | NO            |             |
| smExportTrigger                  | definition_id                                     | int         | int            | NO            |             |
| smExportTrigger                  | description_id                                    | int         | int            | NO            |             |
| smExportTrigger                  | document_id                                       | int         | int            | NO            |             |
| smExportTrigger                  | example                                           | text        | text           | NO            |             |
| smExportTrigger                  | importable                                        | varchar     | varchar(10)    | NO            |             |
| smExportTrigger                  | label_id                                          | int         | int            | NO            |             |
| smExportTrigger                  | module_id                                         | int         | int            | NO            |             |
| smExportTrigger                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smExportTrigger                  | notes_id                                          | int         | int            | NO            |             |
| smExportTrigger                  | object_id                                         | int         | int            | NO            |             |
| smExportTrigger                  | query                                             | text        | text           | NO            |             |
| smExportTrigger                  | queryType                                         | varchar     | varchar(255)   | NO            |             |
| smExportTrigger                  | response_id                                       | int         | int            | NO            |             |
| smExportTrigger                  | type_id                                           | int         | int            | NO            |             |
| smExporterDestination            | oid                                               | int         | int            | NO            | Primary Key |
| smExporterDestination            | active                                            | varchar     | varchar(10)    | NO            |             |
| smExporterDestination            | classoid                                          | int         | int            | NO            |             |
| smExporterDestination            | creationMode                                      | varchar     | varchar(255)   | NO            |             |
| smExporterDestination            | defaultResponse                                   | varchar     | varchar(255)   | NO            |             |
| smExporterDestination            | destination_id                                    | int         | int            | NO            |             |
| smExporterDestination            | exporter_id                                       | int         | int            | NO            |             |
| smExporterDestination            | exporterIndex                                     | int         | int            | NO            |             |
| smExporterDestination            | interface_id                                      | int         | int            | NO            |             |
| smExporterDestination            | module_id                                         | int         | int            | NO            |             |
| smExporterDestination            | msgLogging                                        | varchar     | varchar(255)   | NO            |             |
| smExporterDestination            | name                                              | varchar     | varchar(255)   | NO            |             |
| smExporterDestination            | system_id                                         | int         | int            | NO            |             |
| smExporterTrigger                | oid                                               | int         | int            | NO            | Primary Key |
| smExporterTrigger                | actionEvent_id                                    | int         | int            | NO            | Foreign Key |
| smExporterTrigger                | exporter_id                                       | int         | int            | NO            | Foreign Key |
| smExporterTrigger                | active                                            | varchar     | varchar(10)    | NO            |             |
| smExporterTrigger                | classoid                                          | int         | int            | NO            |             |
| smExporterTrigger                | description_id                                    | int         | int            | NO            |             |
| smExporterTrigger                | label_id                                          | int         | int            | NO            |             |
| smExporterTrigger                | module_id                                         | int         | int            | NO            |             |
| smExporterTrigger                | name                                              | varchar     | varchar(255)   | NO            |             |
| smExporterTrigger                | reference_id                                      | int         | int            | NO            |             |
| smExporterTrigger                | sequence                                          | int         | int            | NO            |             |
| smExternalSystem                 | oid                                               | int         | int            | NO            | Primary Key |
| smExternalSystem                 | classoid                                          | int         | int            | NO            |             |
| smExternalSystem                 | description_id                                    | int         | int            | NO            |             |
| smExternalSystem                 | label_id                                          | int         | int            | NO            |             |
| smExternalSystem                 | module_id                                         | int         | int            | NO            |             |
| smExternalSystem                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smExternalSystem                 | template                                          | varchar     | varchar(10)    | NO            |             |
| smExternalSystem                 | template_id                                       | int         | int            | NO            |             |
| smExternalSystem                 | type_id                                           | int         | int            | NO            |             |
| smFeatureTactic                  | oid                                               | int         | int            | NO            | Primary Key |
| smFeatureTactic                  | feature_id                                        | int         | int            | NO            | Foreign Key |
| smFeatureTactic                  | tactic_id                                         | int         | int            | NO            | Foreign Key |
| smFeatureTactic                  | classoid                                          | int         | int            | NO            |             |
| smFeatureTactic                  | description_id                                    | int         | int            | NO            |             |
| smFeatureTactic                  | label_id                                          | int         | int            | NO            |             |
| smFeatureTactic                  | module_id                                         | int         | int            | NO            |             |
| smFeatureTactic                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smFeatureTactic                  | referenceId                                       | char        | char(36)       | NO            |             |
| smFeatureTactic                  | sequence                                          | int         | int            | NO            |             |
| smFeatureTactic                  | useCase_id                                        | int         | int            | NO            |             |
| smFeatureTactic                  | versionNo                                         | int         | int            | NO            |             |
| smFeatureType                    | oid                                               | int         | int            | NO            | Primary Key |
| smFeatureType                    | classoid                                          | int         | int            | NO            |             |
| smFeatureType                    | description_id                                    | int         | int            | NO            |             |
| smFeatureType                    | label_id                                          | int         | int            | NO            |             |
| smFeatureType                    | module_id                                         | int         | int            | NO            |             |
| smFeatureType                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smFeatureType                    | parent_id                                         | int         | int            | NO            |             |
| smFeatureType                    | referenceId                                       | char        | char(36)       | NO            |             |
| smFeatureType                    | versionNo                                         | int         | int            | NO            |             |
| smFileDocType                    | oid                                               | int         | int            | NO            | Primary Key |
| smFileDocType                    | authentication                                    | varchar     | varchar(10)    | NO            |             |
| smFileDocType                    | classoid                                          | int         | int            | NO            |             |
| smFileDocType                    | description_id                                    | int         | int            | NO            |             |
| smFileDocType                    | folder_id                                         | int         | int            | NO            |             |
| smFileDocType                    | label_id                                          | int         | int            | NO            |             |
| smFileDocType                    | module_id                                         | int         | int            | NO            |             |
| smFileDocType                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smFileDocType                    | repository_id                                     | int         | int            | NO            |             |
| smFileDocTypeRelation            | oid                                               | int         | int            | NO            | Primary Key |
| smFileDocTypeRelation            | classoid                                          | int         | int            | NO            |             |
| smFileDocTypeRelation            | creationMode                                      | varchar     | varchar(255)   | NO            |             |
| smFileDocTypeRelation            | description_id                                    | int         | int            | NO            |             |
| smFileDocTypeRelation            | folder_id                                         | int         | int            | NO            |             |
| smFileDocTypeRelation            | label_id                                          | int         | int            | NO            |             |
| smFileDocTypeRelation            | module_id                                         | int         | int            | NO            |             |
| smFileDocTypeRelation            | object_id                                         | int         | int            | NO            |             |
| smFileDocTypeRelation            | repository_id                                     | int         | int            | NO            |             |
| smFileDocTypeRelation            | type_id                                           | int         | int            | NO            |             |
| smFileType                       | oid                                               | int         | int            | NO            | Primary Key |
| smFileType                       | classoid                                          | int         | int            | NO            |             |
| smFileType                       | description_id                                    | int         | int            | NO            |             |
| smFileType                       | extension                                         | varchar     | varchar(255)   | NO            |             |
| smFileType                       | label_id                                          | int         | int            | NO            |             |
| smFileType                       | module_id                                         | int         | int            | NO            |             |
| smFileType                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smFileType                       | type_id                                           | int         | int            | NO            |             |
| smHelpDocument                   | oid                                               | int         | int            | NO            | Primary Key |
| smHelpDocument                   | classoid                                          | int         | int            | NO            |             |
| smHelpDocument                   | description_id                                    | int         | int            | NO            |             |
| smHelpDocument                   | fileType_id                                       | int         | int            | NO            |             |
| smHelpDocument                   | folder_id                                         | int         | int            | NO            |             |
| smHelpDocument                   | label_id                                          | int         | int            | NO            |             |
| smHelpDocument                   | module_id                                         | int         | int            | NO            |             |
| smHelpDocument                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smHelpDocument                   | owner_id                                          | int         | int            | NO            |             |
| smHelpDocument                   | report_id                                         | int         | int            | NO            |             |
| smHelpDocument                   | reportRelation_id                                 | int         | int            | NO            |             |
| smHelpDocument                   | repository_id                                     | int         | int            | NO            |             |
| smHelpDocument                   | template_id                                       | int         | int            | NO            |             |
| smHelpTopic                      | oid                                               | int         | int            | NO            | Primary Key |
| smHelpTopic                      | document_id                                       | int         | int            | NO            | Foreign Key |
| smHelpTopic                      | parent_id                                         | int         | int            | NO            | Foreign Key |
| smHelpTopic                      | classoid                                          | int         | int            | NO            |             |
| smHelpTopic                      | description_id                                    | int         | int            | NO            |             |
| smHelpTopic                      | docref_id                                         | int         | int            | NO            |             |
| smHelpTopic                      | hidden                                            | varchar     | varchar(10)    | NO            |             |
| smHelpTopic                      | keywords                                          | varchar     | varchar(255)   | NO            |             |
| smHelpTopic                      | label_id                                          | int         | int            | NO            |             |
| smHelpTopic                      | language_id                                       | int         | int            | NO            |             |
| smHelpTopic                      | module_id                                         | int         | int            | NO            |             |
| smHelpTopic                      | name                                              | varchar     | varchar(255)   | NO            |             |
| smHelpTopic                      | notes_id                                          | int         | int            | NO            |             |
| smHelpTopic                      | numberingMode                                     | varchar     | varchar(255)   | NO            |             |
| smHelpTopic                      | orientation                                       | varchar     | varchar(255)   | NO            |             |
| smHelpTopic                      | pageBreak                                         | varchar     | varchar(255)   | NO            |             |
| smHelpTopic                      | section                                           | varchar     | varchar(255)   | NO            |             |
| smHelpTopic                      | sequence                                          | int         | int            | NO            |             |
| smHelpTopic                      | type_id                                           | int         | int            | NO            |             |
| smImporter                       | oid                                               | int         | int            | NO            | Primary Key |
| smImporter                       | active                                            | varchar     | varchar(10)    | NO            |             |
| smImporter                       | classoid                                          | int         | int            | NO            |             |
| smImporter                       | defaultdoc_id                                     | int         | int            | NO            |             |
| smImporter                       | description_id                                    | int         | int            | NO            |             |
| smImporter                       | document_id                                       | int         | int            | NO            |             |
| smImporter                       | label_id                                          | int         | int            | NO            |             |
| smImporter                       | module_id                                         | int         | int            | NO            |             |
| smImporter                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smImporter                       | notes_id                                          | int         | int            | NO            |             |
| smImporter                       | object_id                                         | int         | int            | NO            |             |
| smImporter                       | status                                            | text        | text           | NO            |             |
| smImporter                       | type                                              | varchar     | varchar(255)   | NO            |             |
| smImporter                       | type_id                                           | int         | int            | NO            |             |
| smImporterRel                    | oid                                               | int         | int            | NO            | Primary Key |
| smImporterRel                    | classoid                                          | int         | int            | NO            |             |
| smImporterRel                    | document_id                                       | int         | int            | NO            |             |
| smImporterRel                    | importer_id                                       | int         | int            | NO            |             |
| smImporterRel                    | module_id                                         | int         | int            | NO            |             |
| smImporterRel                    | sequence                                          | int         | int            | NO            |             |
| smImporterRel                    | template_id                                       | int         | int            | NO            |             |
| smImporterSource                 | oid                                               | int         | int            | NO            | Primary Key |
| smImporterSource                 | active                                            | varchar     | varchar(10)    | NO            |             |
| smImporterSource                 | classoid                                          | int         | int            | NO            |             |
| smImporterSource                 | config_id                                         | int         | int            | NO            |             |
| smImporterSource                 | exporter_id                                       | int         | int            | NO            |             |
| smImporterSource                 | importer_id                                       | int         | int            | NO            |             |
| smImporterSource                 | importerIndex                                     | int         | int            | NO            |             |
| smImporterSource                 | interface_id                                      | int         | int            | NO            |             |
| smImporterSource                 | module_id                                         | int         | int            | NO            |             |
| smImporterSource                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smImporterSource                 | system_id                                         | int         | int            | NO            |             |
| smIndex                          | oid                                               | int         | int            | NO            | Primary Key |
| smIndex                          | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smIndex                          | object_id                                         | int         | int            | NO            | Foreign Key |
| smIndex                          | classoid                                          | int         | int            | NO            |             |
| smIndex                          | description                                       | text        | text           | NO            |             |
| smIndex                          | module_id                                         | int         | int            | NO            |             |
| smIndex                          | uniqueIdx                                         | varchar     | varchar(10)    | NO            |             |
| smIndex                          | validation                                        | varchar     | varchar(255)   | NO            |             |
| smIndexAttribute                 | oid                                               | int         | int            | NO            | Primary Key |
| smIndexAttribute                 | index_id                                          | int         | int            | NO            | Foreign Key |
| smIndexAttribute                 | attribute_id                                      | int         | int            | NO            |             |
| smIndexAttribute                 | classoid                                          | int         | int            | NO            |             |
| smIndexAttribute                 | description_id                                    | int         | int            | NO            |             |
| smIndexAttribute                 | indexPosition                                     | int         | int            | NO            |             |
| smIndexAttribute                 | label_id                                          | int         | int            | NO            |             |
| smIndexAttribute                 | methodName                                        | varchar     | varchar(255)   | NO            |             |
| smIndexAttribute                 | module_id                                         | int         | int            | NO            |             |
| smIndexAttribute                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smIndexAttribute                 | optional                                          | varchar     | varchar(10)    | NO            |             |
| smIndexAttribute                 | type_id                                           | int         | int            | NO            |             |
| smInterfaceInstance              | oid                                               | int         | int            | NO            | Primary Key |
| smInterfaceInstance              | active                                            | varchar     | varchar(10)    | NO            |             |
| smInterfaceInstance              | classoid                                          | int         | int            | NO            |             |
| smInterfaceInstance              | interface_id                                      | int         | int            | NO            |             |
| smInterfaceInstance              | module_id                                         | int         | int            | NO            |             |
| smInterfaceInstance              | system_id                                         | int         | int            | NO            |             |
| smInterfaceTrigger               | oid                                               | int         | int            | NO            | Primary Key |
| smInterfaceTrigger               | classoid                                          | int         | int            | NO            |             |
| smInterfaceTrigger               | interface_id                                      | int         | int            | NO            |             |
| smInterfaceTrigger               | module_id                                         | int         | int            | NO            |             |
| smInterfaceTrigger               | notes_id                                          | int         | int            | NO            |             |
| smInterfaceTrigger               | status                                            | varchar     | varchar(255)   | NO            |             |
| smInterfaceTrigger               | trigger_id                                        | int         | int            | NO            |             |
| smKPI                            | oid                                               | int         | int            | NO            | Primary Key |
| smKPI                            | active                                            | varchar     | varchar(10)    | NO            |             |
| smKPI                            | classoid                                          | int         | int            | NO            |             |
| smKPI                            | description_id                                    | int         | int            | NO            |             |
| smKPI                            | filters                                           | text        | text           | NO            |             |
| smKPI                            | icon                                              | varchar     | varchar(255)   | NO            |             |
| smKPI                            | label_id                                          | int         | int            | NO            |             |
| smKPI                            | module_id                                         | int         | int            | NO            |             |
| smKPI                            | name                                              | varchar     | varchar(255)   | NO            |             |
| smKPI                            | parent_id                                         | int         | int            | NO            |             |
| smKPI                            | script                                            | text        | text           | NO            |             |
| smKPI                            | sequence                                          | int         | int            | NO            |             |
| smKeyGenerator                   | oid                                               | int         | int            | NO            | Primary Key |
| smKeyGenerator                   | classoid                                          | int         | int            | NO            |             |
| smKeyGenerator                   | description_id                                    | int         | int            | NO            |             |
| smKeyGenerator                   | label_id                                          | int         | int            | NO            |             |
| smKeyGenerator                   | module_id                                         | int         | int            | NO            |             |
| smKeyGenerator                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smLicense                        | oid                                               | int         | int            | NO            | Primary Key |
| smLicense                        | active                                            | varchar     | varchar(10)    | NO            |             |
| smLicense                        | classoid                                          | int         | int            | NO            |             |
| smLicense                        | description_id                                    | int         | int            | NO            |             |
| smLicense                        | label_id                                          | int         | int            | NO            |             |
| smLicense                        | licenseKey                                        | varchar     | varchar(255)   | NO            |             |
| smLicense                        | module_id                                         | int         | int            | NO            |             |
| smLicense                        | name                                              | varchar     | varchar(255)   | NO            |             |
| smLicenseObject                  | oid                                               | int         | int            | NO            | Primary Key |
| smLicenseObject                  | access                                            | varchar     | varchar(255)   | NO            |             |
| smLicenseObject                  | classoid                                          | int         | int            | NO            |             |
| smLicenseObject                  | license_id                                        | int         | int            | NO            |             |
| smLicenseObject                  | module_id                                         | int         | int            | NO            |             |
| smLicenseObject                  | object_id                                         | int         | int            | NO            |             |
| smLicenseObject                  | parent_id                                         | int         | int            | NO            |             |
| smLocaleAttribute                | oid                                               | int         | int            | NO            | Primary Key |
| smLocaleAttribute                | classoid                                          | int         | int            | NO            |             |
| smLocaleAttribute                | description_id                                    | int         | int            | NO            |             |
| smLocaleAttribute                | label_id                                          | int         | int            | NO            |             |
| smLocaleAttribute                | module_id                                         | int         | int            | NO            |             |
| smLocaleAttribute                | name                                              | varchar     | varchar(255)   | NO            |             |
| smLocaleAttribute                | type                                              | varchar     | varchar(255)   | NO            |             |
| smLocalizableItem                | oid                                               | int         | int            | NO            | Primary Key |
| smLocalizableItem                | attribute_id                                      | int         | int            | NO            | Foreign Key |
| smLocalizableItem                | owner_id                                          | int         | int            | NO            | Foreign Key |
| smLocalizableItem                | classoid                                          | int         | int            | NO            |             |
| smLocalizableItem                | module_id                                         | int         | int            | NO            |             |
| smLocalizableItem                | readonly                                          | varchar     | varchar(10)    | NO            |             |
| smLocalizableValue               | oid                                               | int         | int            | NO            | Primary Key |
| smLocalizableValue               | localizable_id                                    | int         | int            | NO            | Foreign Key |
| smLocalizableValue               | autotranslated                                    | varchar     | varchar(10)    | NO            |             |
| smLocalizableValue               | classoid                                          | int         | int            | NO            |             |
| smLocalizableValue               | language                                          | varchar     | varchar(255)   | NO            |             |
| smLocalizableValue               | message                                           | mediumtext  | mediumtext     | NO            |             |
| smLocalizableValue               | module_id                                         | int         | int            | NO            |             |
| smLogger                         | oid                                               | int         | int            | NO            | Primary Key |
| smLogger                         | active                                            | varchar     | varchar(10)    | NO            |             |
| smLogger                         | classoid                                          | int         | int            | NO            |             |
| smLogger                         | description_id                                    | int         | int            | NO            |             |
| smLogger                         | label_id                                          | int         | int            | NO            |             |
| smLogger                         | module_id                                         | int         | int            | NO            |             |
| smLogger                         | name                                              | varchar     | varchar(255)   | NO            |             |
| smLogger                         | user_id                                           | int         | int            | NO            |             |
| smLookupCategory                 | oid                                               | int         | int            | NO            | Primary Key |
| smLookupCategory                 | classoid                                          | int         | int            | NO            |             |
| smLookupCategory                 | description_id                                    | int         | int            | NO            |             |
| smLookupCategory                 | label_id                                          | int         | int            | NO            |             |
| smLookupCategory                 | module_id                                         | int         | int            | NO            |             |
| smLookupCategory                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smLookupCategory                 | object_id                                         | int         | int            | NO            |             |
| smLookupCategoryRel              | oid                                               | int         | int            | NO            | Primary Key |
| smLookupCategoryRel              | child_id                                          | int         | int            | NO            |             |
| smLookupCategoryRel              | classoid                                          | int         | int            | NO            |             |
| smLookupCategoryRel              | module_id                                         | int         | int            | NO            |             |
| smLookupCategoryRel              | parent_id                                         | int         | int            | NO            |             |
| smLookupContext                  | oid                                               | int         | int            | NO            | Primary Key |
| smLookupContext                  | classoid                                          | int         | int            | NO            |             |
| smLookupContext                  | description_id                                    | int         | int            | NO            |             |
| smLookupContext                  | label_id                                          | int         | int            | NO            |             |
| smLookupContext                  | module_id                                         | int         | int            | NO            |             |
| smLookupContext                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smLookupContextParam             | oid                                               | int         | int            | NO            | Primary Key |
| smLookupContextParam             | classoid                                          | int         | int            | NO            |             |
| smLookupContextParam             | context_id                                        | int         | int            | NO            |             |
| smLookupContextParam             | description_id                                    | int         | int            | NO            |             |
| smLookupContextParam             | label_id                                          | int         | int            | NO            |             |
| smLookupContextParam             | module_id                                         | int         | int            | NO            |             |
| smLookupContextParam             | name                                              | varchar     | varchar(255)   | NO            |             |
| smLookupContextParam             | type_id                                           | int         | int            | NO            |             |
| smLookupItem                     | oid                                               | int         | int            | NO            | Primary Key |
| smLookupItem                     | category_id                                       | int         | int            | NO            |             |
| smLookupItem                     | classoid                                          | int         | int            | NO            |             |
| smLookupItem                     | description_id                                    | int         | int            | NO            |             |
| smLookupItem                     | label_id                                          | int         | int            | NO            |             |
| smLookupItem                     | module_id                                         | int         | int            | NO            |             |
| smLookupItem                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smLookupItem                     | status                                            | varchar     | varchar(255)   | NO            |             |
| smMessage                        | oid                                               | int         | int            | NO            | Primary Key |
| smMessage                        | messageGroup_id                                   | int         | int            | NO            | Foreign Key |
| smMessage                        | classoid                                          | int         | int            | NO            |             |
| smMessage                        | code                                              | int         | int            | NO            |             |
| smMessage                        | description_id                                    | int         | int            | NO            |             |
| smMessage                        | error_id                                          | int         | int            | NO            |             |
| smMessage                        | hasParameters                                     | varchar     | varchar(10)    | NO            |             |
| smMessage                        | label_id                                          | int         | int            | NO            |             |
| smMessage                        | level_id                                          | int         | int            | NO            |             |
| smMessage                        | message_id                                        | int         | int            | NO            |             |
| smMessage                        | module_id                                         | int         | int            | NO            |             |
| smMessage                        | msgType                                           | varchar     | varchar(255)   | NO            |             |
| smMessage                        | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessage                        | object_id                                         | int         | int            | NO            |             |
| smMessage                        | title_id                                          | int         | int            | NO            |             |
| smMessage                        | type_id                                           | int         | int            | NO            |             |
| smMessageCategory                | oid                                               | int         | int            | NO            | Primary Key |
| smMessageCategory                | asyncMode                                         | varchar     | varchar(10)    | NO            |             |
| smMessageCategory                | classoid                                          | int         | int            | NO            |             |
| smMessageCategory                | description_id                                    | int         | int            | NO            |             |
| smMessageCategory                | format_id                                         | int         | int            | NO            |             |
| smMessageCategory                | label_id                                          | int         | int            | NO            |             |
| smMessageCategory                | module_id                                         | int         | int            | NO            |             |
| smMessageCategory                | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageCategoryRecipientType   | oid                                               | int         | int            | NO            | Primary Key |
| smMessageCategoryRecipientType   | classoid                                          | int         | int            | NO            |             |
| smMessageCategoryRecipientType   | messageCategory_id                                | int         | int            | NO            |             |
| smMessageCategoryRecipientType   | module_id                                         | int         | int            | NO            |             |
| smMessageCategoryRecipientType   | recipientType_id                                  | int         | int            | NO            |             |
| smMessageEndpoint                | oid                                               | int         | int            | NO            | Primary Key |
| smMessageEndpoint                | classoid                                          | int         | int            | NO            |             |
| smMessageEndpoint                | defaultEndpoint                                   | varchar     | varchar(10)    | NO            |             |
| smMessageEndpoint                | description_id                                    | int         | int            | NO            |             |
| smMessageEndpoint                | label_id                                          | int         | int            | NO            |             |
| smMessageEndpoint                | module_id                                         | int         | int            | NO            |             |
| smMessageEndpoint                | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageEndpoint                | persistence                                       | varchar     | varchar(255)   | NO            |             |
| smMessageEndpoint                | type_id                                           | int         | int            | NO            |             |
| smMessageEndpointInstance        | oid                                               | int         | int            | NO            | Primary Key |
| smMessageEndpointInstance        | classoid                                          | int         | int            | NO            |             |
| smMessageEndpointInstance        | endpoint_id                                       | int         | int            | NO            |             |
| smMessageEndpointInstance        | instance_id                                       | int         | int            | NO            |             |
| smMessageEndpointInstance        | module_id                                         | int         | int            | NO            |             |
| smMessageEndpointSubscription    | oid                                               | int         | int            | NO            | Primary Key |
| smMessageEndpointSubscription    | classoid                                          | int         | int            | NO            |             |
| smMessageEndpointSubscription    | endpoint_id                                       | int         | int            | NO            |             |
| smMessageEndpointSubscription    | module_id                                         | int         | int            | NO            |             |
| smMessageEndpointSubscription    | subscriptionGroup_id                              | int         | int            | NO            |             |
| smMessageEndpointType            | oid                                               | int         | int            | NO            | Primary Key |
| smMessageEndpointType            | classoid                                          | int         | int            | NO            |             |
| smMessageEndpointType            | description_id                                    | int         | int            | NO            |             |
| smMessageEndpointType            | label_id                                          | int         | int            | NO            |             |
| smMessageEndpointType            | module_id                                         | int         | int            | NO            |             |
| smMessageEndpointType            | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageFormat                  | oid                                               | int         | int            | NO            | Primary Key |
| smMessageFormat                  | classoid                                          | int         | int            | NO            |             |
| smMessageFormat                  | message_id                                        | int         | int            | NO            |             |
| smMessageFormat                  | module_id                                         | int         | int            | NO            |             |
| smMessageFormat                  | type_id                                           | int         | int            | NO            |             |
| smMessageFormatType              | oid                                               | int         | int            | NO            | Primary Key |
| smMessageFormatType              | classoid                                          | int         | int            | NO            |             |
| smMessageFormatType              | description_id                                    | int         | int            | NO            |             |
| smMessageFormatType              | filetype_id                                       | int         | int            | NO            |             |
| smMessageFormatType              | label_id                                          | int         | int            | NO            |             |
| smMessageFormatType              | module_id                                         | int         | int            | NO            |             |
| smMessageFormatType              | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageGroup                   | oid                                               | int         | int            | NO            | Primary Key |
| smMessageGroup                   | category_id                                       | int         | int            | NO            |             |
| smMessageGroup                   | classoid                                          | int         | int            | NO            |             |
| smMessageGroup                   | description_id                                    | int         | int            | NO            |             |
| smMessageGroup                   | label_id                                          | int         | int            | NO            |             |
| smMessageGroup                   | module_id                                         | int         | int            | NO            |             |
| smMessageGroup                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageGroup                   | owner_id                                          | int         | int            | NO            |             |
| smMessageGroup                   | type_id                                           | int         | int            | NO            |             |
| smMessageLevel                   | oid                                               | int         | int            | NO            | Primary Key |
| smMessageLevel                   | action                                            | varchar     | varchar(255)   | NO            |             |
| smMessageLevel                   | category_id                                       | int         | int            | NO            |             |
| smMessageLevel                   | classoid                                          | int         | int            | NO            |             |
| smMessageLevel                   | description_id                                    | int         | int            | NO            |             |
| smMessageLevel                   | label_id                                          | int         | int            | NO            |             |
| smMessageLevel                   | module_id                                         | int         | int            | NO            |             |
| smMessageLevel                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageLevel                   | priority                                          | int         | int            | NO            |             |
| smMessageParam                   | oid                                               | int         | int            | NO            | Primary Key |
| smMessageParam                   | classoid                                          | int         | int            | NO            |             |
| smMessageParam                   | defaultValue                                      | varchar     | varchar(255)   | NO            |             |
| smMessageParam                   | description_id                                    | int         | int            | NO            |             |
| smMessageParam                   | label_id                                          | int         | int            | NO            |             |
| smMessageParam                   | message_id                                        | int         | int            | NO            |             |
| smMessageParam                   | module_id                                         | int         | int            | NO            |             |
| smMessageParam                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageParam                   | required                                          | varchar     | varchar(10)    | NO            |             |
| smMessageParam                   | sequence                                          | int         | int            | NO            |             |
| smMessageParam                   | type_id                                           | int         | int            | NO            |             |
| smMessageRecipientAccount        | oid                                               | int         | int            | NO            | Primary Key |
| smMessageRecipientAccount        | accountName                                       | varchar     | varchar(255)   | NO            |             |
| smMessageRecipientAccount        | classoid                                          | int         | int            | NO            |             |
| smMessageRecipientAccount        | module_id                                         | int         | int            | NO            |             |
| smMessageRecipientAccount        | recipient_id                                      | int         | int            | NO            |             |
| smMessageRecipientAccount        | type_id                                           | int         | int            | NO            |             |
| smMessageRecipientType           | oid                                               | int         | int            | NO            | Primary Key |
| smMessageRecipientType           | classoid                                          | int         | int            | NO            |             |
| smMessageRecipientType           | description_id                                    | int         | int            | NO            |             |
| smMessageRecipientType           | label_id                                          | int         | int            | NO            |             |
| smMessageRecipientType           | module_id                                         | int         | int            | NO            |             |
| smMessageRecipientType           | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageRecipientType           | object_id                                         | int         | int            | NO            |             |
| smMessageSubscription            | oid                                               | int         | int            | NO            | Primary Key |
| smMessageSubscription            | classoid                                          | int         | int            | NO            |             |
| smMessageSubscription            | message_id                                        | int         | int            | NO            |             |
| smMessageSubscription            | messageGroup_id                                   | int         | int            | NO            |             |
| smMessageSubscription            | module_id                                         | int         | int            | NO            |             |
| smMessageSubscription            | subscriptionGroup_id                              | int         | int            | NO            |             |
| smMessageSubscriptionGroup       | oid                                               | int         | int            | NO            | Primary Key |
| smMessageSubscriptionGroup       | category_id                                       | int         | int            | NO            |             |
| smMessageSubscriptionGroup       | classoid                                          | int         | int            | NO            |             |
| smMessageSubscriptionGroup       | description_id                                    | int         | int            | NO            |             |
| smMessageSubscriptionGroup       | label_id                                          | int         | int            | NO            |             |
| smMessageSubscriptionGroup       | level_id                                          | int         | int            | NO            |             |
| smMessageSubscriptionGroup       | module_id                                         | int         | int            | NO            |             |
| smMessageSubscriptionGroup       | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageSubscriptionGroup       | recipient_id                                      | int         | int            | NO            |             |
| smMessageSubscriptionGroup       | recipientType_id                                  | int         | int            | NO            |             |
| smMessageSubscriptionRecipient   | oid                                               | int         | int            | NO            | Primary Key |
| smMessageSubscriptionRecipient   | account_id                                        | int         | int            | NO            |             |
| smMessageSubscriptionRecipient   | classoid                                          | int         | int            | NO            |             |
| smMessageSubscriptionRecipient   | module_id                                         | int         | int            | NO            |             |
| smMessageSubscriptionRecipient   | subscriptionGroup_id                              | int         | int            | NO            |             |
| smMessageType                    | oid                                               | int         | int            | NO            | Primary Key |
| smMessageType                    | category                                          | varchar     | varchar(255)   | NO            |             |
| smMessageType                    | category_id                                       | int         | int            | NO            |             |
| smMessageType                    | classoid                                          | int         | int            | NO            |             |
| smMessageType                    | description_id                                    | int         | int            | NO            |             |
| smMessageType                    | label_id                                          | int         | int            | NO            |             |
| smMessageType                    | module_id                                         | int         | int            | NO            |             |
| smMessageType                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smMessageType                    | object_id                                         | int         | int            | NO            |             |
| smMessageType                    | priority                                          | int         | int            | NO            |             |
| smMigrationScript                | oid                                               | int         | int            | NO            | Primary Key |
| smMigrationScript                | classoid                                          | int         | int            | NO            |             |
| smMigrationScript                | description_id                                    | int         | int            | NO            |             |
| smMigrationScript                | module_id                                         | int         | int            | NO            |             |
| smMigrationScript                | name                                              | varchar     | varchar(255)   | NO            |             |
| smMigrationScript                | required                                          | varchar     | varchar(10)    | NO            |             |
| smMigrationScript                | scriptText                                        | text        | text           | NO            |             |
| smMigrationScript                | scriptType                                        | varchar     | varchar(255)   | NO            |             |
| smMigrationScript                | sequence                                          | int         | int            | NO            |             |
| smMigrationScript                | triggerName                                       | varchar     | varchar(255)   | NO            |             |
| smMigrationScript                | version_id                                        | int         | int            | NO            |             |
| smMimeType                       | oid                                               | int         | int            | NO            | Primary Key |
| smMimeType                       | baseType                                          | varchar     | varchar(255)   | NO            |             |
| smMimeType                       | classoid                                          | int         | int            | NO            |             |
| smMimeType                       | description_id                                    | int         | int            | NO            |             |
| smMimeType                       | label_id                                          | int         | int            | NO            |             |
| smMimeType                       | module_id                                         | int         | int            | NO            |             |
| smMimeType                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smMimeType                       | subType                                           | varchar     | varchar(255)   | NO            |             |
| smModule                         | oid                                               | int         | int            | NO            | Primary Key |
| smModule                         | classoid                                          | int         | int            | NO            |             |
| smModule                         | lastImported                                      | varchar     | varchar(255)   | NO            |             |
| smModule                         | module_id                                         | int         | int            | NO            |             |
| smModule                         | name                                              | varchar     | varchar(255)   | NO            |             |
| smModule                         | package                                           | varchar     | varchar(255)   | NO            |             |
| smModule                         | range_start                                       | int         | int            | NO            |             |
| smModule                         | range_stop                                        | int         | int            | NO            |             |
| smModule                         | readonly                                          | varchar     | varchar(10)    | NO            |             |
| smModule                         | runtime                                           | varchar     | varchar(10)    | NO            |             |
| smModule                         | type                                              | varchar     | varchar(255)   | NO            |             |
| smModule                         | version_id                                        | int         | int            | NO            |             |
| smModuleDependency               | oid                                               | int         | int            | NO            | Primary Key |
| smModuleDependency               | classoid                                          | int         | int            | NO            |             |
| smModuleDependency               | module_id                                         | int         | int            | NO            |             |
| smModuleDependency               | parent_id                                         | int         | int            | NO            |             |
| smModuleLibrary                  | oid                                               | int         | int            | NO            | Primary Key |
| smModuleLibrary                  | classoid                                          | int         | int            | NO            |             |
| smModuleLibrary                  | description                                       | text        | text           | NO            |             |
| smModuleLibrary                  | license                                           | varchar     | varchar(255)   | NO            |             |
| smModuleLibrary                  | licenseURL                                        | varchar     | varchar(255)   | NO            |             |
| smModuleLibrary                  | module_id                                         | int         | int            | NO            |             |
| smModuleLibrary                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smModuleLibrary                  | organization                                      | varchar     | varchar(255)   | NO            |             |
| smModuleLibrary                  | parent_id                                         | int         | int            | NO            |             |
| smModuleLibrary                  | revision                                          | varchar     | varchar(255)   | NO            |             |
| smModuleRecordableGroup          | oid                                               | int         | int            | NO            | Primary Key |
| smModuleRecordableGroup          | classoid                                          | int         | int            | NO            |             |
| smModuleRecordableGroup          | module_id                                         | int         | int            | NO            |             |
| smModuleRecordableGroup          | name                                              | varchar     | varchar(255)   | NO            |             |
| smModuleRecordableGroup          | recordableGroup_id                                | int         | int            | NO            |             |
| smModuleVersion                  | oid                                               | int         | int            | NO            | Primary Key |
| smModuleVersion                  | classoid                                          | int         | int            | NO            |             |
| smModuleVersion                  | module_id                                         | int         | int            | NO            |             |
| smModuleVersion                  | sequence                                          | int         | int            | NO            |             |
| smModuleVersion                  | version                                           | varchar     | varchar(255)   | NO            |             |
| smObjectAPIServiceType           | oid                                               | int         | int            | NO            | Primary Key |
| smObjectAPIServiceType           | classoid                                          | int         | int            | NO            |             |
| smObjectAPIServiceType           | description_id                                    | int         | int            | NO            |             |
| smObjectAPIServiceType           | label_id                                          | int         | int            | NO            |             |
| smObjectAPIServiceType           | module_id                                         | int         | int            | NO            |             |
| smObjectAPIServiceType           | name                                              | varchar     | varchar(255)   | NO            |             |
| smObjectAPIServiceType           | object_id                                         | int         | int            | NO            |             |
| smObjectAPIServiceType           | type_id                                           | int         | int            | NO            |             |
| smObjectCategory                 | oid                                               | int         | int            | NO            | Primary Key |
| smObjectCategory                 | category_id                                       | int         | int            | NO            |             |
| smObjectCategory                 | classoid                                          | int         | int            | NO            |             |
| smObjectCategory                 | module_id                                         | int         | int            | NO            |             |
| smObjectCategory                 | object_id                                         | int         | int            | NO            |             |
| smObjectContext                  | oid                                               | int         | int            | NO            | Primary Key |
| smObjectContext                  | contextClass_id                                   | int         | int            | NO            | Foreign Key |
| smObjectContext                  | object_id                                         | int         | int            | NO            | Foreign Key |
| smObjectContext                  | classoid                                          | int         | int            | NO            |             |
| smObjectContext                  | context_id                                        | int         | int            | NO            |             |
| smObjectContext                  | description_id                                    | int         | int            | NO            |             |
| smObjectContext                  | label_id                                          | int         | int            | NO            |             |
| smObjectContext                  | module_id                                         | int         | int            | NO            |             |
| smObjectContext                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smObjectContextAction            | oid                                               | int         | int            | NO            | Primary Key |
| smObjectContextAction            | context_id                                        | int         | int            | NO            | Foreign Key |
| smObjectContextAction            | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smObjectContextAction            | action_id                                         | int         | int            | NO            |             |
| smObjectContextAction            | className                                         | varchar     | varchar(255)   | NO            |             |
| smObjectContextAction            | classoid                                          | int         | int            | NO            |             |
| smObjectContextAction            | description_id                                    | int         | int            | NO            |             |
| smObjectContextAction            | executionMode                                     | varchar     | varchar(255)   | NO            |             |
| smObjectContextAction            | executionPool_id                                  | int         | int            | NO            |             |
| smObjectContextAction            | label_id                                          | int         | int            | NO            |             |
| smObjectContextAction            | module_id                                         | int         | int            | NO            |             |
| smObjectContextAction            | script_id                                         | int         | int            | NO            |             |
| smObjectGroup                    | oid                                               | int         | int            | NO            | Primary Key |
| smObjectGroup                    | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smObjectGroup                    | classoid                                          | int         | int            | NO            |             |
| smObjectGroup                    | description_id                                    | int         | int            | NO            |             |
| smObjectGroup                    | label_id                                          | int         | int            | NO            |             |
| smObjectGroup                    | module_id                                         | int         | int            | NO            |             |
| smObjectGroup                    | object_id                                         | int         | int            | NO            |             |
| smObjectGroupItem                | oid                                               | int         | int            | NO            | Primary Key |
| smObjectGroupItem                | attribute_id                                      | int         | int            | NO            |             |
| smObjectGroupItem                | classoid                                          | int         | int            | NO            |             |
| smObjectGroupItem                | description_id                                    | int         | int            | NO            |             |
| smObjectGroupItem                | item_id                                           | int         | int            | NO            |             |
| smObjectGroupItem                | label_id                                          | int         | int            | NO            |             |
| smObjectGroupItem                | module_id                                         | int         | int            | NO            |             |
| smObjectGroupItem                | name                                              | varchar     | varchar(255)   | NO            |             |
| smObjectGroupItem                | objectGroup_id                                    | int         | int            | NO            |             |
| smObjectGroupItem                | sequence                                          | int         | int            | NO            |             |
| smObjectLogger                   | oid                                               | int         | int            | NO            | Primary Key |
| smObjectLogger                   | object_id                                         | int         | int            | NO            | Foreign Key |
| smObjectLogger                   | objectGroup_id                                    | int         | int            | NO            | Foreign Key |
| smObjectLogger                   | classoid                                          | int         | int            | NO            |             |
| smObjectLogger                   | description_id                                    | int         | int            | NO            |             |
| smObjectLogger                   | label_id                                          | int         | int            | NO            |             |
| smObjectLogger                   | module_id                                         | int         | int            | NO            |             |
| smObjectLogger                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smObjectParameter                | oid                                               | int         | int            | NO            | Primary Key |
| smObjectParameter                | action_id                                         | int         | int            | NO            | Foreign Key |
| smObjectParameter                | classoid                                          | int         | int            | NO            |             |
| smObjectParameter                | description_id                                    | int         | int            | NO            |             |
| smObjectParameter                | direction                                         | varchar     | varchar(255)   | NO            |             |
| smObjectParameter                | label_id                                          | int         | int            | NO            |             |
| smObjectParameter                | module_id                                         | int         | int            | NO            |             |
| smObjectParameter                | name                                              | varchar     | varchar(255)   | NO            |             |
| smObjectParameter                | object_id                                         | int         | int            | NO            |             |
| smObjectParameter                | objectContext_id                                  | int         | int            | NO            |             |
| smObjectParameter                | sequence                                          | int         | int            | NO            |             |
| smObjectParameter                | type_id                                           | int         | int            | NO            |             |
| smOperationMode                  | oid                                               | int         | int            | NO            | Primary Key |
| smOperationMode                  | classoid                                          | int         | int            | NO            |             |
| smOperationMode                  | description_id                                    | int         | int            | NO            |             |
| smOperationMode                  | label_id                                          | int         | int            | NO            |             |
| smOperationMode                  | module_id                                         | int         | int            | NO            |             |
| smOperationMode                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smParameter                      | oid                                               | int         | int            | NO            | Primary Key |
| smParameter                      | service_id                                        | int         | int            | NO            | Foreign Key |
| smParameter                      | classoid                                          | int         | int            | NO            |             |
| smParameter                      | defaultValue                                      | varchar     | varchar(255)   | NO            |             |
| smParameter                      | description_id                                    | int         | int            | NO            |             |
| smParameter                      | displayOrder                                      | int         | int            | NO            |             |
| smParameter                      | label_id                                          | int         | int            | NO            |             |
| smParameter                      | methodName                                        | varchar     | varchar(255)   | NO            |             |
| smParameter                      | module_id                                         | int         | int            | NO            |             |
| smParameter                      | name                                              | varchar     | varchar(255)   | NO            |             |
| smParameter                      | required                                          | varchar     | varchar(10)    | NO            |             |
| smParameter                      | type_id                                           | int         | int            | NO            |             |
| smPasswordPolicy                 | oid                                               | int         | int            | NO            | Primary Key |
| smPasswordPolicy                 | changeInitialPassword                             | varchar     | varchar(10)    | NO            |             |
| smPasswordPolicy                 | classoid                                          | int         | int            | NO            |             |
| smPasswordPolicy                 | daysBeforeExpiry                                  | int         | int            | NO            |             |
| smPasswordPolicy                 | description_id                                    | int         | int            | NO            |             |
| smPasswordPolicy                 | encoding                                          | varchar     | varchar(255)   | NO            |             |
| smPasswordPolicy                 | generationMode                                    | varchar     | varchar(255)   | NO            |             |
| smPasswordPolicy                 | hashingAlgorithm                                  | varchar     | varchar(255)   | NO            |             |
| smPasswordPolicy                 | label_id                                          | int         | int            | NO            |             |
| smPasswordPolicy                 | module_id                                         | int         | int            | NO            |             |
| smPasswordPolicy                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smPasswordPolicy                 | status                                            | varchar     | varchar(255)   | NO            |             |
| smPasswordPolicy                 | type_id                                           | int         | int            | NO            |             |
| smPasswordPolicyType             | oid                                               | int         | int            | NO            | Primary Key |
| smPasswordPolicyType             | classoid                                          | int         | int            | NO            |             |
| smPasswordPolicyType             | description_id                                    | int         | int            | NO            |             |
| smPasswordPolicyType             | label_id                                          | int         | int            | NO            |             |
| smPasswordPolicyType             | module_id                                         | int         | int            | NO            |             |
| smPasswordPolicyType             | name                                              | varchar     | varchar(255)   | NO            |             |
| smPermissionType                 | oid                                               | int         | int            | NO            | Primary Key |
| smPermissionType                 | classoid                                          | int         | int            | NO            |             |
| smPermissionType                 | description_id                                    | int         | int            | NO            |             |
| smPermissionType                 | label_id                                          | int         | int            | NO            |             |
| smPermissionType                 | module_id                                         | int         | int            | NO            |             |
| smPermissionType                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smPermissionType                 | object_id                                         | int         | int            | NO            |             |
| smPermissionType                 | objectGroup_id                                    | int         | int            | NO            |             |
| smPersistedColumn                | oid                                               | int         | int            | NO            | Primary Key |
| smPersistedColumn                | table_id                                          | int         | int            | NO            | Foreign Key |
| smPersistedColumn                | classoid                                          | int         | int            | NO            |             |
| smPersistedColumn                | dbType                                            | varchar     | varchar(255)   | NO            |             |
| smPersistedColumn                | description                                       | text        | text           | NO            |             |
| smPersistedColumn                | module_id                                         | int         | int            | NO            |             |
| smPersistedColumn                | name                                              | varchar     | varchar(255)   | NO            |             |
| smPersistedColumn                | sequence                                          | int         | int            | NO            |             |
| smPersistedColumn                | template_id                                       | int         | int            | NO            |             |
| smPersistedColumn                | type_id                                           | int         | int            | NO            |             |
| smPersistedIndex                 | oid                                               | int         | int            | NO            | Primary Key |
| smPersistedIndex                 | classoid                                          | int         | int            | NO            |             |
| smPersistedIndex                 | description                                       | varchar     | varchar(255)   | NO            |             |
| smPersistedIndex                 | idxFillFactor                                     | int         | int            | NO            |             |
| smPersistedIndex                 | module_id                                         | int         | int            | NO            |             |
| smPersistedIndex                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smPersistedIndex                 | table_id                                          | int         | int            | NO            |             |
| smPersistedIndex                 | uniqueIndex                                       | varchar     | varchar(10)    | NO            |             |
| smPersistedIndexCol              | oid                                               | int         | int            | NO            | Primary Key |
| smPersistedIndexCol              | classoid                                          | int         | int            | NO            |             |
| smPersistedIndexCol              | column_id                                         | int         | int            | NO            |             |
| smPersistedIndexCol              | columnOrder                                       | int         | int            | NO            |             |
| smPersistedIndexCol              | index_id                                          | int         | int            | NO            |             |
| smPersistedIndexCol              | module_id                                         | int         | int            | NO            |             |
| smPersistedTable                 | oid                                               | int         | int            | NO            | Primary Key |
| smPersistedTable                 | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smPersistedTable                 | type_id                                           | int         | int            | NO            | Foreign Key |
| smPersistedTable                 | archivable                                        | varchar     | varchar(10)    | NO            |             |
| smPersistedTable                 | classoid                                          | int         | int            | NO            |             |
| smPersistedTable                 | dataGroup_id                                      | int         | int            | NO            |             |
| smPersistedTable                 | datastore_id                                      | int         | int            | NO            |             |
| smPersistedTable                 | description                                       | text        | text           | NO            |             |
| smPersistedTable                 | incrementNo                                       | int         | int            | NO            |             |
| smPersistedTable                 | module_id                                         | int         | int            | NO            |             |
| smPersistedTable                 | partitionType_id                                  | int         | int            | NO            |             |
| smPersistedTable                 | version_id                                        | int         | int            | NO            |             |
| smPlatformLanguage               | classoid                                          | int         | int            | NO            |             |
| smPlatformLanguage               | language_id                                       | int         | int            | NO            |             |
| smPlatformLanguage               | module_id                                         | int         | int            | NO            |             |
| smPlatformLanguage               | oid                                               | int         | int            | NO            |             |
| smPlatformLanguage               | platform_id                                       | int         | int            | NO            |             |
| smPrinterFormat                  | oid                                               | int         | int            | NO            | Primary Key |
| smPrinterFormat                  | classoid                                          | int         | int            | NO            |             |
| smPrinterFormat                  | description_id                                    | int         | int            | NO            |             |
| smPrinterFormat                  | label_id                                          | int         | int            | NO            |             |
| smPrinterFormat                  | module_id                                         | int         | int            | NO            |             |
| smPrinterFormat                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smPrinterFormat                  | printerType_id                                    | int         | int            | NO            |             |
| smPrinterType                    | oid                                               | int         | int            | NO            | Primary Key |
| smPrinterType                    | classoid                                          | int         | int            | NO            |             |
| smPrinterType                    | description_id                                    | int         | int            | NO            |             |
| smPrinterType                    | label_id                                          | int         | int            | NO            |             |
| smPrinterType                    | module_id                                         | int         | int            | NO            |             |
| smPrinterType                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smProcVar                        | oid                                               | int         | int            | NO            | Primary Key |
| smProcVar                        | attribute_id                                      | int         | int            | NO            |             |
| smProcVar                        | classoid                                          | int         | int            | NO            |             |
| smProcVar                        | description_id                                    | int         | int            | NO            |             |
| smProcVar                        | initialvalue                                      | varchar     | varchar(255)   | NO            |             |
| smProcVar                        | label_id                                          | int         | int            | NO            |             |
| smProcVar                        | module_id                                         | int         | int            | NO            |             |
| smProcVar                        | name                                              | varchar     | varchar(255)   | NO            |             |
| smProcVar                        | path                                              | varchar     | varchar(255)   | NO            |             |
| smProcVar                        | process_id                                        | int         | int            | NO            |             |
| smProcVar                        | type_id                                           | int         | int            | NO            |             |
| smProcess                        | oid                                               | int         | int            | NO            | Primary Key |
| smProcess                        | category                                          | varchar     | varchar(255)   | NO            |             |
| smProcess                        | classoid                                          | int         | int            | NO            |             |
| smProcess                        | code                                              | varchar     | varchar(255)   | NO            |             |
| smProcess                        | inputMode                                         | varchar     | varchar(255)   | NO            |             |
| smProcess                        | label_id                                          | int         | int            | NO            |             |
| smProcess                        | module_id                                         | int         | int            | NO            |             |
| smProcess                        | name                                              | varchar     | varchar(255)   | NO            |             |
| smProcess                        | outputMode                                        | varchar     | varchar(255)   | NO            |             |
| smProcess                        | parent_id                                         | int         | int            | NO            |             |
| smProcess                        | processType_id                                    | int         | int            | NO            |             |
| smProcess                        | purpose_id                                        | int         | int            | NO            |             |
| smProcess                        | state_id                                          | int         | int            | NO            |             |
| smProcess                        | type                                              | varchar     | varchar(255)   | NO            |             |
| smProcessAttribute               | oid                                               | int         | int            | NO            | Primary Key |
| smProcessAttribute               | attribute_id                                      | int         | int            | NO            |             |
| smProcessAttribute               | classoid                                          | int         | int            | NO            |             |
| smProcessAttribute               | description_id                                    | int         | int            | NO            |             |
| smProcessAttribute               | module_id                                         | int         | int            | NO            |             |
| smProcessAttribute               | object_id                                         | int         | int            | NO            |             |
| smProcessAttribute               | process_id                                        | int         | int            | NO            |             |
| smProcessAttribute               | value                                             | varchar     | varchar(255)   | NO            |             |
| smProcessType                    | oid                                               | int         | int            | NO            | Primary Key |
| smProcessType                    | classoid                                          | int         | int            | NO            |             |
| smProcessType                    | description_id                                    | int         | int            | NO            |             |
| smProcessType                    | label_id                                          | int         | int            | NO            |             |
| smProcessType                    | module_id                                         | int         | int            | NO            |             |
| smProcessType                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smProfiler                       | oid                                               | int         | int            | NO            | Primary Key |
| smProfiler                       | active                                            | varchar     | varchar(10)    | NO            |             |
| smProfiler                       | classoid                                          | int         | int            | NO            |             |
| smProfiler                       | context_id                                        | int         | int            | NO            |             |
| smProfiler                       | description_id                                    | int         | int            | NO            |             |
| smProfiler                       | label_id                                          | int         | int            | NO            |             |
| smProfiler                       | level                                             | varchar     | varchar(255)   | NO            |             |
| smProfiler                       | maxTime                                           | int         | int            | NO            |             |
| smProfiler                       | minimumLevel_id                                   | int         | int            | NO            |             |
| smProfiler                       | minTime                                           | int         | int            | NO            |             |
| smProfiler                       | module_id                                         | int         | int            | NO            |             |
| smProfiler                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smProfiler                       | object_id                                         | int         | int            | NO            |             |
| smProfiler                       | printStack                                        | varchar     | varchar(255)   | NO            |             |
| smProfiler                       | type_id                                           | int         | int            | NO            |             |
| smProfiler                       | verbosity                                         | varchar     | varchar(255)   | NO            |             |
| smProfilerFilter                 | oid                                               | int         | int            | NO            | Primary Key |
| smProfilerFilter                 | active                                            | varchar     | varchar(10)    | NO            |             |
| smProfilerFilter                 | classoid                                          | int         | int            | NO            |             |
| smProfilerFilter                 | context_id                                        | int         | int            | NO            |             |
| smProfilerFilter                 | description_id                                    | int         | int            | NO            |             |
| smProfilerFilter                 | label_id                                          | int         | int            | NO            |             |
| smProfilerFilter                 | module_id                                         | int         | int            | NO            |             |
| smProfilerFilter                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smProfilerFilter                 | parent_id                                         | int         | int            | NO            |             |
| smProfilerFilter                 | profiler_id                                       | int         | int            | NO            |             |
| smProfilerFilter                 | type_id                                           | int         | int            | NO            |             |
| smProfilerFilterType             | oid                                               | int         | int            | NO            | Primary Key |
| smProfilerFilterType             | classoid                                          | int         | int            | NO            |             |
| smProfilerFilterType             | description_id                                    | int         | int            | NO            |             |
| smProfilerFilterType             | label_id                                          | int         | int            | NO            |             |
| smProfilerFilterType             | module_id                                         | int         | int            | NO            |             |
| smProfilerFilterType             | name                                              | varchar     | varchar(255)   | NO            |             |
| smProfilerLevel                  | oid                                               | int         | int            | NO            | Primary Key |
| smProfilerLevel                  | classoid                                          | int         | int            | NO            |             |
| smProfilerLevel                  | description_id                                    | int         | int            | NO            |             |
| smProfilerLevel                  | label_id                                          | int         | int            | NO            |             |
| smProfilerLevel                  | message_id                                        | int         | int            | NO            |             |
| smProfilerLevel                  | module_id                                         | int         | int            | NO            |             |
| smProfilerLevel                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smProfilerLevel                  | profiler_id                                       | int         | int            | NO            |             |
| smProfilerLevel                  | type_id                                           | int         | int            | NO            |             |
| smProfilerLevel                  | verbosity                                         | varchar     | varchar(255)   | NO            |             |
| smProfilerType                   | oid                                               | int         | int            | NO            | Primary Key |
| smProfilerType                   | classoid                                          | int         | int            | NO            |             |
| smProfilerType                   | description_id                                    | int         | int            | NO            |             |
| smProfilerType                   | label_id                                          | int         | int            | NO            |             |
| smProfilerType                   | module_id                                         | int         | int            | NO            |             |
| smProfilerType                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smProfilerTypeLevel              | oid                                               | int         | int            | NO            | Primary Key |
| smProfilerTypeLevel              | classoid                                          | int         | int            | NO            |             |
| smProfilerTypeLevel              | description_id                                    | int         | int            | NO            |             |
| smProfilerTypeLevel              | label_id                                          | int         | int            | NO            |             |
| smProfilerTypeLevel              | message_id                                        | int         | int            | NO            |             |
| smProfilerTypeLevel              | module_id                                         | int         | int            | NO            |             |
| smProfilerTypeLevel              | name                                              | varchar     | varchar(255)   | NO            |             |
| smProfilerTypeLevel              | sequence                                          | int         | int            | NO            |             |
| smProfilerTypeLevel              | type_id                                           | int         | int            | NO            |             |
| smQuery                          | oid                                               | int         | int            | NO            | Primary Key |
| smQuery                          | baseQuery_id                                      | int         | int            | NO            |             |
| smQuery                          | classoid                                          | int         | int            | NO            |             |
| smQuery                          | defaultSort_id                                    | int         | int            | NO            |             |
| smQuery                          | description_id                                    | int         | int            | NO            |             |
| smQuery                          | label_id                                          | int         | int            | NO            |             |
| smQuery                          | module_id                                         | int         | int            | NO            |             |
| smQuery                          | name                                              | varchar     | varchar(255)   | NO            |             |
| smQuery                          | object_id                                         | int         | int            | NO            |             |
| smQuery                          | parent_id                                         | int         | int            | NO            |             |
| smQuery                          | soloqlObject_id                                   | int         | int            | NO            |             |
| smQueryElement                   | oid                                               | int         | int            | NO            | Primary Key |
| smQueryElement                   | query_id                                          | int         | int            | NO            | Foreign Key |
| smQueryElement                   | attribute_id                                      | int         | int            | NO            |             |
| smQueryElement                   | classoid                                          | int         | int            | NO            |             |
| smQueryElement                   | description_id                                    | int         | int            | NO            |             |
| smQueryElement                   | displayMode                                       | varchar     | varchar(255)   | NO            |             |
| smQueryElement                   | function_id                                       | int         | int            | NO            |             |
| smQueryElement                   | label_id                                          | int         | int            | NO            |             |
| smQueryElement                   | module_id                                         | int         | int            | NO            |             |
| smQueryElement                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smQueryElement                   | object_id                                         | int         | int            | NO            |             |
| smQueryElement                   | relatedAttribute_id                               | int         | int            | NO            |             |
| smQueryElement                   | relatedObject_id                                  | int         | int            | NO            |             |
| smQueryElement                   | relation                                          | varchar     | varchar(255)   | NO            |             |
| smQueryElement                   | required                                          | varchar     | varchar(10)    | NO            |             |
| smQueryElement                   | sequence                                          | int         | int            | NO            |             |
| smQueryElement                   | type_id                                           | int         | int            | NO            |             |
| smQueryElement                   | value                                             | text        | text           | NO            |             |
| smQueryFilter                    | oid                                               | int         | int            | NO            | Primary Key |
| smQueryFilter                    | query_id                                          | int         | int            | NO            | Foreign Key |
| smQueryFilter                    | attribute_id                                      | int         | int            | NO            |             |
| smQueryFilter                    | attributeValue                                    | varchar     | varchar(255)   | NO            |             |
| smQueryFilter                    | classoid                                          | int         | int            | NO            |             |
| smQueryFilter                    | description_id                                    | int         | int            | NO            |             |
| smQueryFilter                    | label_id                                          | int         | int            | NO            |             |
| smQueryFilter                    | module_id                                         | int         | int            | NO            |             |
| smQueryFilter                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smQueryFilter                    | object_id                                         | int         | int            | NO            |             |
| smQueryFilter                    | operator                                          | varchar     | varchar(255)   | NO            |             |
| smQueryFilter                    | required                                          | varchar     | varchar(10)    | NO            |             |
| smQueryFilter                    | value                                             | text        | text           | NO            |             |
| smQueryFilter                    | widget_id                                         | int         | int            | NO            |             |
| smQuerySort                      | oid                                               | int         | int            | NO            | Primary Key |
| smQuerySort                      | classoid                                          | int         | int            | NO            |             |
| smQuerySort                      | description_id                                    | int         | int            | NO            |             |
| smQuerySort                      | label_id                                          | int         | int            | NO            |             |
| smQuerySort                      | module_id                                         | int         | int            | NO            |             |
| smQuerySort                      | name                                              | varchar     | varchar(255)   | NO            |             |
| smQuerySort                      | query_id                                          | int         | int            | NO            |             |
| smQuerySortColumn                | oid                                               | int         | int            | NO            | Primary Key |
| smQuerySortColumn                | classoid                                          | int         | int            | NO            |             |
| smQuerySortColumn                | column_id                                         | int         | int            | NO            |             |
| smQuerySortColumn                | module_id                                         | int         | int            | NO            |             |
| smQuerySortColumn                | parent_id                                         | int         | int            | NO            |             |
| smQuerySortColumn                | sequence                                          | int         | int            | NO            |             |
| smQuerySortColumn                | sortMode                                          | varchar     | varchar(255)   | NO            |             |
| smRecordableGroup                | oid                                               | int         | int            | NO            | Primary Key |
| smRecordableGroup                | classoid                                          | int         | int            | NO            |             |
| smRecordableGroup                | description_id                                    | int         | int            | NO            |             |
| smRecordableGroup                | label_id                                          | int         | int            | NO            |             |
| smRecordableGroup                | module_id                                         | int         | int            | NO            |             |
| smRecordableGroup                | name                                              | varchar     | varchar(255)   | NO            |             |
| smRecordableObject               | oid                                               | int         | int            | NO            | Primary Key |
| smRecordableObject               | classoid                                          | int         | int            | NO            |             |
| smRecordableObject               | group_id                                          | int         | int            | NO            |             |
| smRecordableObject               | module_id                                         | int         | int            | NO            |             |
| smRecordableObject               | object_id                                         | int         | int            | NO            |             |
| smRecordableObject               | sequence                                          | int         | int            | NO            |             |
| smRelativeDate                   | oid                                               | int         | int            | NO            | Primary Key |
| smRelativeDate                   | classoid                                          | int         | int            | NO            |             |
| smRelativeDate                   | description_id                                    | int         | int            | NO            |             |
| smRelativeDate                   | endDate                                           | varchar     | varchar(255)   | NO            |             |
| smRelativeDate                   | endValue                                          | int         | int            | NO            |             |
| smRelativeDate                   | label_id                                          | int         | int            | NO            |             |
| smRelativeDate                   | module_id                                         | int         | int            | NO            |             |
| smRelativeDate                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smRelativeDate                   | startDate                                         | varchar     | varchar(255)   | NO            |             |
| smRelativeDate                   | startValue                                        | int         | int            | NO            |             |
| smRelativeDate                   | timescale                                         | varchar     | varchar(255)   | NO            |             |
| smReport                         | oid                                               | int         | int            | NO            | Primary Key |
| smReport                         | parent_id                                         | int         | int            | NO            | Foreign Key |
| smReport                         | archivable                                        | varchar     | varchar(255)   | NO            |             |
| smReport                         | classoid                                          | int         | int            | NO            |             |
| smReport                         | description_id                                    | int         | int            | NO            |             |
| smReport                         | folder_id                                         | int         | int            | NO            |             |
| smReport                         | format_id                                         | int         | int            | NO            |             |
| smReport                         | group_id                                          | int         | int            | NO            |             |
| smReport                         | label_id                                          | int         | int            | NO            |             |
| smReport                         | module_id                                         | int         | int            | NO            |             |
| smReport                         | name                                              | varchar     | varchar(255)   | NO            |             |
| smReport                         | owner_id                                          | int         | int            | NO            |             |
| smReport                         | reportFormat_id                                   | int         | int            | NO            |             |
| smReport                         | repository_id                                     | int         | int            | NO            |             |
| smReport                         | type_id                                           | int         | int            | NO            |             |
| smReportAttribute                | oid                                               | int         | int            | NO            | Primary Key |
| smReportAttribute                | report_id                                         | int         | int            | NO            | Foreign Key |
| smReportAttribute                | classoid                                          | int         | int            | NO            |             |
| smReportAttribute                | defaultvalue                                      | varchar     | varchar(255)   | NO            |             |
| smReportAttribute                | description_id                                    | int         | int            | NO            |             |
| smReportAttribute                | label_id                                          | int         | int            | NO            |             |
| smReportAttribute                | module_id                                         | int         | int            | NO            |             |
| smReportAttribute                | name                                              | varchar     | varchar(255)   | NO            |             |
| smReportAttribute                | required                                          | varchar     | varchar(10)    | NO            |             |
| smReportAttribute                | type_id                                           | int         | int            | NO            |             |
| smReportFormat                   | oid                                               | int         | int            | NO            | Primary Key |
| smReportFormat                   | classoid                                          | int         | int            | NO            |             |
| smReportFormat                   | filetype_id                                       | int         | int            | NO            |             |
| smReportFormat                   | label_id                                          | int         | int            | NO            |             |
| smReportFormat                   | module_id                                         | int         | int            | NO            |             |
| smReportFormat                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smReportFormat                   | printerType_id                                    | int         | int            | NO            |             |
| smReportFormat                   | type_id                                           | int         | int            | NO            |             |
| smReportRelation                 | oid                                               | int         | int            | NO            | Primary Key |
| smReportRelation                 | attribute_id                                      | int         | int            | NO            |             |
| smReportRelation                 | classoid                                          | int         | int            | NO            |             |
| smReportRelation                 | creationMode                                      | varchar     | varchar(255)   | NO            |             |
| smReportRelation                 | description_id                                    | int         | int            | NO            |             |
| smReportRelation                 | folder_id                                         | int         | int            | NO            |             |
| smReportRelation                 | label_id                                          | int         | int            | NO            |             |
| smReportRelation                 | module_id                                         | int         | int            | NO            |             |
| smReportRelation                 | object_id                                         | int         | int            | NO            |             |
| smReportRelation                 | report_id                                         | int         | int            | NO            |             |
| smReportRelation                 | reportInstance_id                                 | int         | int            | NO            |             |
| smReportRelation                 | repository_id                                     | int         | int            | NO            |             |
| smReportRelation                 | versioningMode                                    | varchar     | varchar(255)   | NO            |             |
| smReportType                     | oid                                               | int         | int            | NO            | Primary Key |
| smReportType                     | classoid                                          | int         | int            | NO            |             |
| smReportType                     | description_id                                    | int         | int            | NO            |             |
| smReportType                     | format_id                                         | int         | int            | NO            |             |
| smReportType                     | label_id                                          | int         | int            | NO            |             |
| smReportType                     | module_id                                         | int         | int            | NO            |             |
| smReportType                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smReportType                     | printerType_id                                    | int         | int            | NO            |             |
| smRepository                     | oid                                               | int         | int            | NO            | Primary Key |
| smRepository                     | category_id                                       | int         | int            | NO            |             |
| smRepository                     | classoid                                          | int         | int            | NO            |             |
| smRepository                     | description_id                                    | int         | int            | NO            |             |
| smRepository                     | label_id                                          | int         | int            | NO            |             |
| smRepository                     | location_id                                       | int         | int            | NO            |             |
| smRepository                     | module_id                                         | int         | int            | NO            |             |
| smRepository                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smRepositoryCategory             | oid                                               | int         | int            | NO            | Primary Key |
| smRepositoryCategory             | classoid                                          | int         | int            | NO            |             |
| smRepositoryCategory             | description_id                                    | int         | int            | NO            |             |
| smRepositoryCategory             | label_id                                          | int         | int            | NO            |             |
| smRepositoryCategory             | module_id                                         | int         | int            | NO            |             |
| smRepositoryCategory             | name                                              | varchar     | varchar(255)   | NO            |             |
| smRepositoryLocation             | oid                                               | int         | int            | NO            | Primary Key |
| smRepositoryLocation             | classoid                                          | int         | int            | NO            |             |
| smRepositoryLocation             | defaultLocation                                   | varchar     | varchar(10)    | NO            |             |
| smRepositoryLocation             | mode                                              | varchar     | varchar(255)   | NO            |             |
| smRepositoryLocation             | module_id                                         | int         | int            | NO            |             |
| smRepositoryLocation             | name                                              | varchar     | varchar(255)   | NO            |             |
| smRepositoryLocation             | repository_id                                     | int         | int            | NO            |             |
| smRepositoryLocation             | sequence                                          | int         | int            | NO            |             |
| smRepositoryLocation             | status                                            | varchar     | varchar(255)   | NO            |             |
| smRepositoryLocation             | type_id                                           | int         | int            | NO            |             |
| smRepositoryType                 | oid                                               | int         | int            | NO            | Primary Key |
| smRepositoryType                 | classoid                                          | int         | int            | NO            |             |
| smRepositoryType                 | description_id                                    | int         | int            | NO            |             |
| smRepositoryType                 | externalURL                                       | varchar     | varchar(10)    | NO            |             |
| smRepositoryType                 | label_id                                          | int         | int            | NO            |             |
| smRepositoryType                 | module_id                                         | int         | int            | NO            |             |
| smRepositoryType                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smRole                           | oid                                               | int         | int            | NO            | Primary Key |
| smRole                           | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smRole                           | classoid                                          | int         | int            | NO            |             |
| smRole                           | description_id                                    | int         | int            | NO            |             |
| smRole                           | externalName                                      | varchar     | varchar(255)   | NO            |             |
| smRole                           | label_id                                          | int         | int            | NO            |             |
| smRole                           | module_id                                         | int         | int            | NO            |             |
| smRole                           | userType_id                                       | int         | int            | NO            |             |
| smRoleObject                     | oid                                               | int         | int            | NO            | Primary Key |
| smRoleObject                     | access                                            | varchar     | varchar(255)   | NO            |             |
| smRoleObject                     | classoid                                          | int         | int            | NO            |             |
| smRoleObject                     | module_id                                         | int         | int            | NO            |             |
| smRoleObject                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smRoleObject                     | object_id                                         | int         | int            | NO            |             |
| smRoleObject                     | parent_id                                         | int         | int            | NO            |             |
| smRoleObject                     | role_id                                           | int         | int            | NO            |             |
| smRoleObject                     | securityRight_id                                  | int         | int            | NO            |             |
| smRoleObject                     | type_id                                           | int         | int            | NO            |             |
| smScript                         | oid                                               | int         | int            | NO            | Primary Key |
| smScript                         | active                                            | varchar     | varchar(10)    | NO            |             |
| smScript                         | classoid                                          | int         | int            | NO            |             |
| smScript                         | description_id                                    | int         | int            | NO            |             |
| smScript                         | module_id                                         | int         | int            | NO            |             |
| smScript                         | object_id                                         | int         | int            | NO            |             |
| smScript                         | scriptText                                        | text        | text           | NO            |             |
| smScript                         | sequence                                          | int         | int            | NO            |             |
| smScript                         | triggerEvent                                      | varchar     | varchar(255)   | NO            |             |
| smScript                         | type                                              | varchar     | varchar(255)   | NO            |             |
| smScriptContext                  | oid                                               | int         | int            | NO            | Primary Key |
| smScriptContext                  | classoid                                          | int         | int            | NO            |             |
| smScriptContext                  | description_id                                    | int         | int            | NO            |             |
| smScriptContext                  | label_id                                          | int         | int            | NO            |             |
| smScriptContext                  | module_id                                         | int         | int            | NO            |             |
| smScriptContext                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smScriptContextAction            | oid                                               | int         | int            | NO            | Primary Key |
| smScriptContextAction            | action_id                                         | int         | int            | NO            |             |
| smScriptContextAction            | classoid                                          | int         | int            | NO            |             |
| smScriptContextAction            | initialContent                                    | text        | text           | NO            |             |
| smScriptContextAction            | module_id                                         | int         | int            | NO            |             |
| smScriptContextAction            | returnParam_id                                    | int         | int            | NO            |             |
| smScriptContextAction            | script_id                                         | int         | int            | NO            |             |
| smScriptLanguage                 | oid                                               | int         | int            | NO            | Primary Key |
| smScriptLanguage                 | classoid                                          | int         | int            | NO            |             |
| smScriptLanguage                 | language_id                                       | int         | int            | NO            |             |
| smScriptLanguage                 | module_id                                         | int         | int            | NO            |             |
| smScriptLanguage                 | scriptContext_id                                  | int         | int            | NO            |             |
| smScriptLanguage                 | status                                            | varchar     | varchar(255)   | NO            |             |
| smScriptingLang                  | oid                                               | int         | int            | NO            | Primary Key |
| smScriptingLang                  | classoid                                          | int         | int            | NO            |             |
| smScriptingLang                  | description_id                                    | int         | int            | NO            |             |
| smScriptingLang                  | label_id                                          | int         | int            | NO            |             |
| smScriptingLang                  | module_id                                         | int         | int            | NO            |             |
| smScriptingLang                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smScriptingLang                  | type                                              | varchar     | varchar(255)   | NO            |             |
| smSecret                         | oid                                               | int         | int            | NO            | Primary Key |
| smSecret                         | classoid                                          | int         | int            | NO            |             |
| smSecret                         | description_id                                    | int         | int            | NO            |             |
| smSecret                         | label_id                                          | int         | int            | NO            |             |
| smSecret                         | module_id                                         | int         | int            | NO            |             |
| smSecret                         | name                                              | varchar     | varchar(255)   | NO            |             |
| smSecret                         | password                                          | varchar     | varchar(255)   | NO            |             |
| smSecret                         | type                                              | varchar     | varchar(255)   | NO            |             |
| smSecret                         | username                                          | varchar     | varchar(255)   | NO            |             |
| smSecurableType                  | oid                                               | int         | int            | NO            | Primary Key |
| smSecurableType                  | attribute_id                                      | int         | int            | NO            |             |
| smSecurableType                  | classoid                                          | int         | int            | NO            |             |
| smSecurableType                  | description_id                                    | int         | int            | NO            |             |
| smSecurableType                  | label_id                                          | int         | int            | NO            |             |
| smSecurableType                  | module_id                                         | int         | int            | NO            |             |
| smSecurableType                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smSecurableType                  | object_id                                         | int         | int            | NO            |             |
| smSecurableType                  | parent_id                                         | int         | int            | NO            |             |
| smSecurableType                  | securityRight_id                                  | int         | int            | NO            |             |
| smSecurityPolicy                 | oid                                               | int         | int            | NO            | Primary Key |
| smSecurityPolicy                 | attemptsBeforeLock                                | int         | int            | NO            |             |
| smSecurityPolicy                 | auditMode                                         | varchar     | varchar(255)   | NO            |             |
| smSecurityPolicy                 | classoid                                          | int         | int            | NO            |             |
| smSecurityPolicy                 | description_id                                    | int         | int            | NO            |             |
| smSecurityPolicy                 | label_id                                          | int         | int            | NO            |             |
| smSecurityPolicy                 | module_id                                         | int         | int            | NO            |             |
| smSecurityPolicy                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smSecurityRight                  | oid                                               | int         | int            | NO            | Primary Key |
| smSecurityRight                  | classoid                                          | int         | int            | NO            |             |
| smSecurityRight                  | description_id                                    | int         | int            | NO            |             |
| smSecurityRight                  | label_id                                          | int         | int            | NO            |             |
| smSecurityRight                  | module_id                                         | int         | int            | NO            |             |
| smSecurityRight                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smSecurityRight                  | securableType_id                                  | int         | int            | NO            |             |
| smSecurityRight                  | sequence                                          | int         | int            | NO            |             |
| smSecurityRight                  | type                                              | varchar     | varchar(255)   | NO            |             |
| smServerConnectorType            | oid                                               | int         | int            | NO            | Primary Key |
| smServerConnectorType            | classoid                                          | int         | int            | NO            |             |
| smServerConnectorType            | defaultPort                                       | int         | int            | NO            |             |
| smServerConnectorType            | description_id                                    | int         | int            | NO            |             |
| smServerConnectorType            | label_id                                          | int         | int            | NO            |             |
| smServerConnectorType            | module_id                                         | int         | int            | NO            |             |
| smServerConnectorType            | name                                              | varchar     | varchar(255)   | NO            |             |
| smServerConnectorType            | protocol_id                                       | int         | int            | NO            |             |
| smServerEndpoint                 | oid                                               | int         | int            | NO            | Primary Key |
| smServerEndpoint                 | authentication                                    | varchar     | varchar(255)   | NO            |             |
| smServerEndpoint                 | classoid                                          | int         | int            | NO            |             |
| smServerEndpoint                 | description_id                                    | int         | int            | NO            |             |
| smServerEndpoint                 | label_id                                          | int         | int            | NO            |             |
| smServerEndpoint                 | module_id                                         | int         | int            | NO            |             |
| smServerEndpoint                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smServerEndpoint                 | serverProtocol_id                                 | int         | int            | NO            |             |
| smServerEndpoint                 | type_id                                           | int         | int            | NO            |             |
| smServerEndpoint                 | userEndpointType_id                               | int         | int            | NO            |             |
| smServerEndpointAction           | oid                                               | int         | int            | NO            | Primary Key |
| smServerEndpointAction           | action_id                                         | int         | int            | NO            |             |
| smServerEndpointAction           | authentication                                    | varchar     | varchar(255)   | NO            |             |
| smServerEndpointAction           | classoid                                          | int         | int            | NO            |             |
| smServerEndpointAction           | description_id                                    | int         | int            | NO            |             |
| smServerEndpointAction           | endpoint_id                                       | int         | int            | NO            |             |
| smServerEndpointAction           | label_id                                          | int         | int            | NO            |             |
| smServerEndpointAction           | module_id                                         | int         | int            | NO            |             |
| smServerEndpointAction           | name                                              | varchar     | varchar(255)   | NO            |             |
| smServerEndpointType             | oid                                               | int         | int            | NO            | Primary Key |
| smServerEndpointType             | classoid                                          | int         | int            | NO            |             |
| smServerEndpointType             | description_id                                    | int         | int            | NO            |             |
| smServerEndpointType             | label_id                                          | int         | int            | NO            |             |
| smServerEndpointType             | module_id                                         | int         | int            | NO            |             |
| smServerEndpointType             | name                                              | varchar     | varchar(255)   | NO            |             |
| smServerEndpointType             | protocol_id                                       | int         | int            | NO            |             |
| smService                        | oid                                               | int         | int            | NO            | Primary Key |
| smService                        | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smService                        | category                                          | varchar     | varchar(255)   | NO            |             |
| smService                        | classoid                                          | int         | int            | NO            |             |
| smService                        | description_id                                    | int         | int            | NO            |             |
| smService                        | index_id                                          | int         | int            | NO            |             |
| smService                        | label_id                                          | int         | int            | NO            |             |
| smService                        | module_id                                         | int         | int            | NO            |             |
| smService                        | returntype_id                                     | int         | int            | NO            |             |
| smSessionType                    | oid                                               | int         | int            | NO            | Primary Key |
| smSessionType                    | classoid                                          | int         | int            | NO            |             |
| smSessionType                    | description_id                                    | int         | int            | NO            |             |
| smSessionType                    | label_id                                          | int         | int            | NO            |             |
| smSessionType                    | loggingMode                                       | varchar     | varchar(255)   | NO            |             |
| smSessionType                    | module_id                                         | int         | int            | NO            |             |
| smSessionType                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smSessionType                    | stateless                                         | varchar     | varchar(10)    | NO            |             |
| smSessionType                    | timeout                                           | int         | int            | NO            |             |
| smSoloQLFunction                 | oid                                               | int         | int            | NO            | Primary Key |
| smSoloQLFunction                 | classoid                                          | int         | int            | NO            |             |
| smSoloQLFunction                 | description_id                                    | int         | int            | NO            |             |
| smSoloQLFunction                 | example                                           | varchar     | varchar(255)   | NO            |             |
| smSoloQLFunction                 | label_id                                          | int         | int            | NO            |             |
| smSoloQLFunction                 | module_id                                         | int         | int            | NO            |             |
| smSoloQLFunction                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smState                          | oid                                               | int         | int            | NO            | Primary Key |
| smState                          | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smState                          | stateIdentifier                                   | varchar     | varchar(255)   | NO            | Foreign Key |
| smState                          | classoid                                          | int         | int            | NO            |             |
| smState                          | defaultState                                      | varchar     | varchar(10)    | NO            |             |
| smState                          | label_id                                          | int         | int            | NO            |             |
| smState                          | module_id                                         | int         | int            | NO            |             |
| smState                          | notes_id                                          | int         | int            | NO            |             |
| smState                          | passthrough                                       | varchar     | varchar(10)    | NO            |             |
| smState                          | process_id                                        | int         | int            | NO            |             |
| smState                          | purpose_id                                        | int         | int            | NO            |             |
| smState                          | screenshot_id                                     | int         | int            | NO            |             |
| smState                          | subProcess_id                                     | int         | int            | NO            |             |
| smState                          | usage_id                                          | int         | int            | NO            |             |
| smState                          | voicelabel_id                                     | int         | int            | NO            |             |
| smStorageDataType                | oid                                               | int         | int            | NO            | Primary Key |
| smStorageDataType                | classoid                                          | int         | int            | NO            |             |
| smStorageDataType                | description_id                                    | int         | int            | NO            |             |
| smStorageDataType                | engine_id                                         | int         | int            | NO            |             |
| smStorageDataType                | label_id                                          | int         | int            | NO            |             |
| smStorageDataType                | module_id                                         | int         | int            | NO            |             |
| smStorageDataType                | name                                              | varchar     | varchar(255)   | NO            |             |
| smStorageEngine                  | oid                                               | int         | int            | NO            | Primary Key |
| smStorageEngine                  | classoid                                          | int         | int            | NO            |             |
| smStorageEngine                  | description_id                                    | int         | int            | NO            |             |
| smStorageEngine                  | label_id                                          | int         | int            | NO            |             |
| smStorageEngine                  | module_id                                         | int         | int            | NO            |             |
| smStorageEngine                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smStorageEngine                  | type_id                                           | int         | int            | NO            |             |
| smSysInterfaceObject             | oid                                               | int         | int            | NO            | Primary Key |
| smSysInterfaceObject             | asynchronous                                      | varchar     | varchar(10)    | NO            |             |
| smSysInterfaceObject             | classoid                                          | int         | int            | NO            |             |
| smSysInterfaceObject             | cron_id                                           | int         | int            | NO            |             |
| smSysInterfaceObject             | defaultErrorAction                                | varchar     | varchar(255)   | NO            |             |
| smSysInterfaceObject             | defaultResponse                                   | varchar     | varchar(255)   | NO            |             |
| smSysInterfaceObject             | description_id                                    | int         | int            | NO            |             |
| smSysInterfaceObject             | document_id                                       | int         | int            | NO            |             |
| smSysInterfaceObject             | documentMode                                      | varchar     | varchar(255)   | NO            |             |
| smSysInterfaceObject             | errorCron_id                                      | int         | int            | NO            |             |
| smSysInterfaceObject             | exporterTrigger                                   | varchar     | varchar(255)   | NO            |             |
| smSysInterfaceObject             | hostErrCron_id                                    | int         | int            | NO            |             |
| smSysInterfaceObject             | interface_id                                      | int         | int            | NO            |             |
| smSysInterfaceObject             | label_id                                          | int         | int            | NO            |             |
| smSysInterfaceObject             | module_id                                         | int         | int            | NO            |             |
| smSysInterfaceObject             | msgLogging                                        | varchar     | varchar(255)   | NO            |             |
| smSysInterfaceObject             | name                                              | varchar     | varchar(255)   | NO            |             |
| smSysInterfaceObject             | notes_id                                          | int         | int            | NO            |             |
| smSysInterfaceObject             | object_id                                         | int         | int            | NO            |             |
| smSysInterfaceObject             | operation_id                                      | int         | int            | NO            |             |
| smSysInterfaceObject             | requestCron_id                                    | int         | int            | NO            |             |
| smSysInterfaceObject             | requestExporter_id                                | int         | int            | NO            |             |
| smSysInterfaceObject             | response_id                                       | int         | int            | NO            |             |
| smSysInterfaceObject             | retryCount                                        | int         | int            | NO            |             |
| smSysInterfaceObject             | sequence                                          | int         | int            | NO            |             |
| smSysInterfaceObject             | status                                            | varchar     | varchar(255)   | NO            |             |
| smSystemAccount                  | oid                                               | int         | int            | NO            | Primary Key |
| smSystemAccount                  | classoid                                          | int         | int            | NO            |             |
| smSystemAccount                  | email                                             | varchar     | varchar(255)   | NO            |             |
| smSystemAccount                  | module_id                                         | int         | int            | NO            |             |
| smSystemAccount                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smSystemAccount                  | secret_id                                         | int         | int            | NO            |             |
| smSystemAccount                  | system_id                                         | int         | int            | NO            |             |
| smSystemInstance                 | oid                                               | int         | int            | NO            | Primary Key |
| smSystemInstance                 | active                                            | varchar     | varchar(10)    | NO            |             |
| smSystemInstance                 | classoid                                          | int         | int            | NO            |             |
| smSystemInstance                 | description                                       | varchar     | varchar(255)   | NO            |             |
| smSystemInstance                 | instance_id                                       | int         | int            | NO            |             |
| smSystemInstance                 | module_id                                         | int         | int            | NO            |             |
| smSystemInstance                 | system_id                                         | int         | int            | NO            |             |
| smSystemInterface                | oid                                               | int         | int            | NO            | Primary Key |
| smSystemInterface                | classoid                                          | int         | int            | NO            |             |
| smSystemInterface                | cron_id                                           | int         | int            | NO            |             |
| smSystemInterface                | defaultTrigger                                    | varchar     | varchar(255)   | NO            |             |
| smSystemInterface                | errorCron_id                                      | int         | int            | NO            |             |
| smSystemInterface                | format_id                                         | int         | int            | NO            |             |
| smSystemInterface                | mode                                              | varchar     | varchar(255)   | NO            |             |
| smSystemInterface                | module_id                                         | int         | int            | NO            |             |
| smSystemInterface                | name                                              | varchar     | varchar(255)   | NO            |             |
| smSystemInterface                | protocol_id                                       | int         | int            | NO            |             |
| smSystemInterface                | system_id                                         | int         | int            | NO            |             |
| smSystemInterface                | type_id                                           | int         | int            | NO            |             |
| smSystemInterface                | validation                                        | varchar     | varchar(255)   | NO            |             |
| smTableDataGroup                 | oid                                               | int         | int            | NO            | Primary Key |
| smTableDataGroup                 | classoid                                          | int         | int            | NO            |             |
| smTableDataGroup                 | dataGroup_id                                      | int         | int            | NO            |             |
| smTableDataGroup                 | module_id                                         | int         | int            | NO            |             |
| smTableDataGroup                 | table_id                                          | int         | int            | NO            |             |
| smTableType                      | oid                                               | int         | int            | NO            | Primary Key |
| smTableType                      | classoid                                          | int         | int            | NO            |             |
| smTableType                      | description_id                                    | int         | int            | NO            |             |
| smTableType                      | keygen_id                                         | int         | int            | NO            |             |
| smTableType                      | label_id                                          | int         | int            | NO            |             |
| smTableType                      | module_id                                         | int         | int            | NO            |             |
| smTableType                      | name                                              | varchar     | varchar(255)   | NO            |             |
| smTableType                      | parent_id                                         | int         | int            | NO            |             |
| smTableType                      | partitioningColumn_id                             | int         | int            | NO            |             |
| smTactic                         | oid                                               | int         | int            | NO            | Primary Key |
| smTactic                         | tacticGroup_id                                    | int         | int            | NO            | Foreign Key |
| smTactic                         | benefits_id                                       | int         | int            | NO            |             |
| smTactic                         | classoid                                          | int         | int            | NO            |             |
| smTactic                         | description_id                                    | int         | int            | NO            |             |
| smTactic                         | label_id                                          | int         | int            | NO            |             |
| smTactic                         | limitations_id                                    | int         | int            | NO            |             |
| smTactic                         | module_id                                         | int         | int            | NO            |             |
| smTactic                         | name                                              | varchar     | varchar(255)   | NO            |             |
| smTactic                         | referenceId                                       | char        | char(36)       | NO            |             |
| smTactic                         | sequence                                          | int         | int            | NO            |             |
| smTactic                         | versionNo                                         | int         | int            | NO            |             |
| smTacticConfiguration            | oid                                               | int         | int            | NO            | Primary Key |
| smTacticConfiguration            | attribute_id                                      | int         | int            | NO            | Foreign Key |
| smTacticConfiguration            | tactic_id                                         | int         | int            | NO            | Foreign Key |
| smTacticConfiguration            | classoid                                          | int         | int            | NO            |             |
| smTacticConfiguration            | description_id                                    | int         | int            | NO            |             |
| smTacticConfiguration            | label_id                                          | int         | int            | NO            |             |
| smTacticConfiguration            | module_id                                         | int         | int            | NO            |             |
| smTacticConfiguration            | name                                              | varchar     | varchar(255)   | NO            |             |
| smTacticConfiguration            | value                                             | text        | text           | NO            |             |
| smTacticGroup                    | oid                                               | int         | int            | NO            | Primary Key |
| smTacticGroup                    | applicationModule_id                              | int         | int            | NO            | Foreign Key |
| smTacticGroup                    | classoid                                          | int         | int            | NO            |             |
| smTacticGroup                    | description_id                                    | int         | int            | NO            |             |
| smTacticGroup                    | label_id                                          | int         | int            | NO            |             |
| smTacticGroup                    | module_id                                         | int         | int            | NO            |             |
| smTacticGroup                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smTacticGroup                    | referenceId                                       | char        | char(36)       | NO            |             |
| smTacticGroup                    | versionNo                                         | int         | int            | NO            |             |
| smTransaction                    | oid                                               | bigint      | bigint         | NO            | Primary Key |
| smTransaction                    | group_id                                          | int         | int            | NO            | Foreign Key |
| smTransaction                    | timestamp                                         | datetime    | datetime       | NO            | Foreign Key |
| smTransaction                    | upgrade_id                                        | int         | int            | NO            | Foreign Key |
| smTransaction                    | classoid                                          | int         | int            | NO            |             |
| smTransaction                    | globalKey                                         | char        | char(36)       | NO            |             |
| smTransaction                    | gmodule_id                                        | int         | int            | NO            |             |
| smTransaction                    | module_id                                         | int         | int            | NO            |             |
| smTransaction                    | user_id                                           | int         | int            | NO            |             |
| smTransactionField               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| smTransactionField               | attribute_id                                      | int         | int            | NO            | Foreign Key |
| smTransactionField               | object_id                                         | int         | int            | NO            | Foreign Key |
| smTransactionField               | objectKey                                         | int         | int            | NO            | Foreign Key |
| smTransactionField               | objectkey_id                                      | int         | int            | NO            | Foreign Key |
| smTransactionField               | transaction_id                                    | int         | int            | NO            | Foreign Key |
| smTransactionField               | version_id                                        | int         | int            | NO            | Foreign Key |
| smTransactionField               | classoid                                          | int         | int            | NO            |             |
| smTransactionField               | fromDisplayValue                                  | varchar     | varchar(255)   | NO            |             |
| smTransactionField               | fromValue                                         | mediumtext  | mediumtext     | NO            |             |
| smTransactionField               | operation                                         | varchar     | varchar(255)   | NO            |             |
| smTransactionField               | toDisplayValue                                    | varchar     | varchar(255)   | NO            |             |
| smTransactionField               | toValue                                           | mediumtext  | mediumtext     | NO            |             |
| smTransactionGroup               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| smTransactionGroup               | classoid                                          | int         | int            | NO            |             |
| smTransactionGroup               | createdDate                                       | datetime    | datetime       | NO            |             |
| smTransactionGroup               | description                                       | text        | text           | NO            |             |
| smTransactionGroup               | globalKey                                         | char        | char(36)       | NO            |             |
| smTransactionGroup               | gmodule_id                                        | int         | int            | NO            |             |
| smTransactionGroup               | keepActive                                        | varchar     | varchar(10)    | NO            |             |
| smTransactionGroup               | lastModified                                      | char        | char(36)       | NO            |             |
| smTransactionGroup               | module_id                                         | int         | int            | NO            |             |
| smTransactionGroup               | name                                              | varchar     | varchar(255)   | NO            |             |
| smTransactionGroup               | parent_id                                         | int         | int            | NO            |             |
| smTransactionGroup               | reference                                         | varchar     | varchar(255)   | NO            |             |
| smTransactionGroup               | status                                            | varchar     | varchar(255)   | NO            |             |
| smTransactionGroup               | type                                              | varchar     | varchar(255)   | NO            |             |
| smTransactionGroup               | updadeMode                                        | varchar     | varchar(255)   | NO            |             |
| smTransactionGroup               | user_id                                           | int         | int            | NO            |             |
| smTransition                     | oid                                               | int         | int            | NO            | Primary Key |
| smTransition                     | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smTransition                     | state_id                                          | int         | int            | NO            | Foreign Key |
| smTransition                     | classoid                                          | int         | int            | NO            |             |
| smTransition                     | description_id                                    | int         | int            | NO            |             |
| smTransition                     | destination_id                                    | int         | int            | NO            |             |
| smTransition                     | label_id                                          | int         | int            | NO            |             |
| smTransition                     | message_id                                        | int         | int            | NO            |             |
| smTransition                     | messageType                                       | varchar     | varchar(255)   | NO            |             |
| smTransition                     | module_id                                         | int         | int            | NO            |             |
| smTransition                     | priority                                          | varchar     | varchar(255)   | NO            |             |
| smTransition                     | type                                              | varchar     | varchar(255)   | NO            |             |
| smTransition                     | type_id                                           | int         | int            | NO            |             |
| smTransition                     | voicemessage_id                                   | int         | int            | NO            |             |
| smTransitionType                 | oid                                               | int         | int            | NO            | Primary Key |
| smTransitionType                 | classoid                                          | int         | int            | NO            |             |
| smTransitionType                 | description_id                                    | int         | int            | NO            |             |
| smTransitionType                 | label_id                                          | int         | int            | NO            |             |
| smTransitionType                 | module_id                                         | int         | int            | NO            |             |
| smTransitionType                 | name                                              | varchar     | varchar(255)   | NO            |             |
| smTransitionType                 | processType_id                                    | int         | int            | NO            |             |
| smTransportProtocol              | oid                                               | int         | int            | NO            | Primary Key |
| smTransportProtocol              | classoid                                          | int         | int            | NO            |             |
| smTransportProtocol              | description_id                                    | int         | int            | NO            |             |
| smTransportProtocol              | label_id                                          | int         | int            | NO            |             |
| smTransportProtocol              | module_id                                         | int         | int            | NO            |             |
| smTransportProtocol              | name                                              | varchar     | varchar(255)   | NO            |             |
| smType                           | oid                                               | int         | int            | NO            | Primary Key |
| smType                           | code                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smType                           | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smType                           | object_id                                         | int         | int            | NO            | Foreign Key |
| smType                           | type_id                                           | int         | int            | NO            | Foreign Key |
| smType                           | classname                                         | varchar     | varchar(255)   | NO            |             |
| smType                           | classoid                                          | int         | int            | NO            |             |
| smType                           | description_id                                    | int         | int            | NO            |             |
| smType                           | label_id                                          | int         | int            | NO            |             |
| smType                           | module_id                                         | int         | int            | NO            |             |
| smType                           | publicType                                        | varchar     | varchar(10)    | NO            |             |
| smUIAttribute                    | oid                                               | int         | int            | NO            | Primary Key |
| smUIAttribute                    | type_id                                           | int         | int            | NO            | Foreign Key |
| smUIAttribute                    | widget_id                                         | int         | int            | NO            | Foreign Key |
| smUIAttribute                    | classoid                                          | int         | int            | NO            |             |
| smUIAttribute                    | module_id                                         | int         | int            | NO            |             |
| smUIAttribute                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smUIAttribute                    | value                                             | text        | text           | NO            |             |
| smUIAttributeType                | oid                                               | int         | int            | NO            | Primary Key |
| smUIAttributeType                | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smUIAttributeType                | widget_id                                         | int         | int            | NO            | Foreign Key |
| smUIAttributeType                | classoid                                          | int         | int            | NO            |             |
| smUIAttributeType                | defaultValue                                      | varchar     | varchar(255)   | NO            |             |
| smUIAttributeType                | description_id                                    | int         | int            | NO            |             |
| smUIAttributeType                | label_id                                          | int         | int            | NO            |             |
| smUIAttributeType                | module_id                                         | int         | int            | NO            |             |
| smUIAttributeType                | required                                          | varchar     | varchar(10)    | NO            |             |
| smUIAttributeType                | type_id                                           | int         | int            | NO            |             |
| smUIIcon                         | oid                                               | int         | int            | NO            | Primary Key |
| smUIIcon                         | classoid                                          | int         | int            | NO            |             |
| smUIIcon                         | description_id                                    | int         | int            | NO            |             |
| smUIIcon                         | label_id                                          | int         | int            | NO            |             |
| smUIIcon                         | module_id                                         | int         | int            | NO            |             |
| smUIIcon                         | name                                              | varchar     | varchar(255)   | NO            |             |
| smUIIcon                         | style                                             | varchar     | varchar(255)   | NO            |             |
| smUIIcon                         | value                                             | varchar     | varchar(255)   | NO            |             |
| smUIPageType                     | oid                                               | int         | int            | NO            | Primary Key |
| smUIPageType                     | classoid                                          | int         | int            | NO            |             |
| smUIPageType                     | description_id                                    | int         | int            | NO            |             |
| smUIPageType                     | label_id                                          | int         | int            | NO            |             |
| smUIPageType                     | module_id                                         | int         | int            | NO            |             |
| smUIPageType                     | name                                              | varchar     | varchar(255)   | NO            |             |
| smUIRedirectionAlias             | oid                                               | int         | int            | NO            | Primary Key |
| smUIRedirectionAlias             | redirection_id                                    | int         | int            | NO            | Foreign Key |
| smUIRedirectionAlias             | classoid                                          | int         | int            | NO            |             |
| smUIRedirectionAlias             | destination_id                                    | int         | int            | NO            |             |
| smUIRedirectionAlias             | module_id                                         | int         | int            | NO            |             |
| smUIRedirectionAlias             | name                                              | varchar     | varchar(255)   | NO            |             |
| smUIStyle                        | oid                                               | int         | int            | NO            | Primary Key |
| smUIStyle                        | classoid                                          | int         | int            | NO            |             |
| smUIStyle                        | color_id                                          | int         | int            | NO            |             |
| smUIStyle                        | description_id                                    | int         | int            | NO            |             |
| smUIStyle                        | fontSize                                          | varchar     | varchar(255)   | NO            |             |
| smUIStyle                        | fontStyle                                         | varchar     | varchar(255)   | NO            |             |
| smUIStyle                        | fontWeight                                        | varchar     | varchar(255)   | NO            |             |
| smUIStyle                        | icon_id                                           | int         | int            | NO            |             |
| smUIStyle                        | label_id                                          | int         | int            | NO            |             |
| smUIStyle                        | module_id                                         | int         | int            | NO            |             |
| smUIStyle                        | name                                              | varchar     | varchar(255)   | NO            |             |
| smUIStyle                        | object_id                                         | int         | int            | NO            |             |
| smUIStyle                        | secondaryColor_id                                 | int         | int            | NO            |             |
| smUIStyle                        | textDecoration                                    | varchar     | varchar(255)   | NO            |             |
| smUIStyle                        | textVisibility                                    | varchar     | varchar(255)   | NO            |             |
| smUITheme                        | oid                                               | int         | int            | NO            | Primary Key |
| smUITheme                        | classoid                                          | int         | int            | NO            |             |
| smUITheme                        | description_id                                    | int         | int            | NO            |             |
| smUITheme                        | label_id                                          | int         | int            | NO            |             |
| smUITheme                        | module_id                                         | int         | int            | NO            |             |
| smUITheme                        | name                                              | varchar     | varchar(255)   | NO            |             |
| smUITheme                        | pageType_id                                       | int         | int            | NO            |             |
| smUITheme                        | primaryColor_id                                   | int         | int            | NO            |             |
| smUIWidget                       | oid                                               | int         | int            | NO            | Primary Key |
| smUIWidget                       | module_id                                         | int         | int            | NO            | Foreign Key |
| smUIWidget                       | object_id                                         | int         | int            | NO            | Foreign Key |
| smUIWidget                       | page_id                                           | int         | int            | NO            | Foreign Key |
| smUIWidget                       | parent_id                                         | int         | int            | NO            | Foreign Key |
| smUIWidget                       | widgetGroup_id                                    | int         | int            | NO            | Foreign Key |
| smUIWidget                       | widgetType_id                                     | int         | int            | NO            | Foreign Key |
| smUIWidget                       | classoid                                          | int         | int            | NO            |             |
| smUIWidget                       | description_id                                    | int         | int            | NO            |             |
| smUIWidget                       | header_id                                         | int         | int            | NO            |             |
| smUIWidget                       | helpTopic_id                                      | int         | int            | NO            |             |
| smUIWidget                       | label_id                                          | int         | int            | NO            |             |
| smUIWidget                       | layout_id                                         | int         | int            | NO            |             |
| smUIWidget                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smUIWidget                       | operation_id                                      | int         | int            | NO            |             |
| smUIWidget                       | pageOrder                                         | int         | int            | NO            |             |
| smUIWidget                       | query_id                                          | int         | int            | NO            |             |
| smUIWidget                       | queryElement_id                                   | int         | int            | NO            |             |
| smUIWidget                       | querySort_id                                      | int         | int            | NO            |             |
| smUIWidget                       | redirection_id                                    | int         | int            | NO            |             |
| smUIWidget                       | style_id                                          | int         | int            | NO            |             |
| smUIWidget                       | toolbar_id                                        | int         | int            | NO            |             |
| smUIWidget                       | type_id                                           | int         | int            | NO            |             |
| smUIWidget                       | variable_id                                       | int         | int            | NO            |             |
| smUIWidget                       | widgetGroup                                       | varchar     | varchar(255)   | NO            |             |
| smUIWidget                       | widgetType                                        | varchar     | varchar(255)   | NO            |             |
| smUIWidgetAttribute              | oid                                               | int         | int            | NO            | Primary Key |
| smUIWidgetAttribute              | attribute_id                                      | int         | int            | NO            | Foreign Key |
| smUIWidgetAttribute              | widget_id                                         | int         | int            | NO            | Foreign Key |
| smUIWidgetAttribute              | classoid                                          | int         | int            | NO            |             |
| smUIWidgetAttribute              | defaultValue                                      | varchar     | varchar(255)   | NO            |             |
| smUIWidgetAttribute              | module_id                                         | int         | int            | NO            |             |
| smUIWidgetDataType               | oid                                               | int         | int            | NO            | Primary Key |
| smUIWidgetDataType               | classoid                                          | int         | int            | NO            |             |
| smUIWidgetDataType               | module_id                                         | int         | int            | NO            |             |
| smUIWidgetDataType               | subType_id                                        | int         | int            | NO            |             |
| smUIWidgetDataType               | type                                              | varchar     | varchar(255)   | NO            |             |
| smUIWidgetDataType               | widgetType_id                                     | int         | int            | NO            |             |
| smUIWidgetGroup                  | oid                                               | int         | int            | NO            | Primary Key |
| smUIWidgetGroup                  | classoid                                          | int         | int            | NO            |             |
| smUIWidgetGroup                  | description_id                                    | int         | int            | NO            |             |
| smUIWidgetGroup                  | label_id                                          | int         | int            | NO            |             |
| smUIWidgetGroup                  | module_id                                         | int         | int            | NO            |             |
| smUIWidgetGroup                  | name                                              | varchar     | varchar(255)   | NO            |             |
| smUIWidgetGroup                  | sequence                                          | int         | int            | NO            |             |
| smUIWidgetGroup                  | widgetType_id                                     | int         | int            | NO            |             |
| smUIWidgetRelation               | oid                                               | int         | int            | NO            | Primary Key |
| smUIWidgetRelation               | child_id                                          | int         | int            | NO            |             |
| smUIWidgetRelation               | classoid                                          | int         | int            | NO            |             |
| smUIWidgetRelation               | module_id                                         | int         | int            | NO            |             |
| smUIWidgetRelation               | parent_id                                         | int         | int            | NO            |             |
| smUIWidgetRelation               | parentRelation_id                                 | int         | int            | NO            |             |
| smUIWidgetRelation               | widgetGroup_id                                    | int         | int            | NO            |             |
| smUIWidgetType                   | oid                                               | int         | int            | NO            | Primary Key |
| smUIWidgetType                   | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smUIWidgetType                   | abstractWidget                                    | varchar     | varchar(10)    | NO            |             |
| smUIWidgetType                   | classoid                                          | int         | int            | NO            |             |
| smUIWidgetType                   | description_id                                    | int         | int            | NO            |             |
| smUIWidgetType                   | label_id                                          | int         | int            | NO            |             |
| smUIWidgetType                   | module_id                                         | int         | int            | NO            |             |
| smUIWidgetType                   | pageType_id                                       | int         | int            | NO            |             |
| smUIWidgetType                   | parent_id                                         | int         | int            | NO            |             |
| smUIWidgetType                   | status                                            | varchar     | varchar(255)   | NO            |             |
| smUIWidgetType                   | widgetClass_id                                    | int         | int            | NO            |             |
| smUseCase                        | oid                                               | int         | int            | NO            | Primary Key |
| smUseCase                        | feature_id                                        | int         | int            | NO            | Foreign Key |
| smUseCase                        | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| smUseCase                        | classoid                                          | int         | int            | NO            |             |
| smUseCase                        | description_id                                    | int         | int            | NO            |             |
| smUseCase                        | label_id                                          | int         | int            | NO            |             |
| smUseCase                        | module_id                                         | int         | int            | NO            |             |
| smUseCase                        | parent_id                                         | int         | int            | NO            |             |
| smUseCase                        | process_id                                        | int         | int            | NO            |             |
| smUseCase                        | referenceId                                       | char        | char(36)       | NO            |             |
| smUseCase                        | testType_id                                       | int         | int            | NO            |             |
| smUseCase                        | type                                              | varchar     | varchar(255)   | NO            |             |
| smUseCase                        | versionNo                                         | int         | int            | NO            |             |
| smUseCaseStep                    | oid                                               | int         | int            | NO            | Primary Key |
| smUseCaseStep                    | useCase_id                                        | int         | int            | NO            | Foreign Key |
| smUseCaseStep                    | classoid                                          | int         | int            | NO            |             |
| smUseCaseStep                    | description_id                                    | int         | int            | NO            |             |
| smUseCaseStep                    | label_id                                          | int         | int            | NO            |             |
| smUseCaseStep                    | module_id                                         | int         | int            | NO            |             |
| smUseCaseStep                    | name                                              | varchar     | varchar(255)   | NO            |             |
| smUseCaseStep                    | parameters                                        | text        | text           | NO            |             |
| smUseCaseStep                    | reference_id                                      | int         | int            | NO            |             |
| smUseCaseStep                    | referenceId                                       | char        | char(36)       | NO            |             |
| smUseCaseStep                    | response                                          | text        | text           | NO            |             |
| smUseCaseStep                    | sequence                                          | int         | int            | NO            |             |
| smUseCaseStep                    | state_id                                          | int         | int            | NO            |             |
| smUseCaseStep                    | transition_id                                     | int         | int            | NO            |             |
| smUseCaseStep                    | versionNo                                         | int         | int            | NO            |             |
| smUserAuthentication             | oid                                               | int         | int            | NO            | Primary Key |
| smUserAuthentication             | classoid                                          | int         | int            | NO            |             |
| smUserAuthentication             | initialCredentialStatus                           | varchar     | varchar(10)    | NO            |             |
| smUserAuthentication             | module_id                                         | int         | int            | NO            |             |
| smUserAuthentication             | name                                              | varchar     | varchar(255)   | NO            |             |
| smUserAuthentication             | offlinePrivilege                                  | varchar     | varchar(10)    | NO            |             |
| smUserAuthentication             | policy_id                                         | int         | int            | NO            |             |
| smUserAuthentication             | securityPolicy_id                                 | int         | int            | NO            |             |
| smUserAuthentication             | sessiontype_id                                    | int         | int            | NO            |             |
| smUserAuthentication             | status                                            | varchar     | varchar(255)   | NO            |             |
| smUserAuthentication             | system_id                                         | int         | int            | NO            |             |
| smUserAuthentication             | usertype_id                                       | int         | int            | NO            |             |
| smUserEndpoint                   | oid                                               | int         | int            | NO            | Primary Key |
| smUserEndpoint                   | applicationModel_id                               | int         | int            | NO            |             |
| smUserEndpoint                   | classoid                                          | int         | int            | NO            |             |
| smUserEndpoint                   | description_id                                    | int         | int            | NO            |             |
| smUserEndpoint                   | label_id                                          | int         | int            | NO            |             |
| smUserEndpoint                   | module_id                                         | int         | int            | NO            |             |
| smUserEndpoint                   | name                                              | varchar     | varchar(255)   | NO            |             |
| smUserEndpoint                   | type_id                                           | int         | int            | NO            |             |
| smUserEndpointAccess             | oid                                               | int         | int            | NO            | Primary Key |
| smUserEndpointAccess             | classoid                                          | int         | int            | NO            |             |
| smUserEndpointAccess             | module_id                                         | int         | int            | NO            |             |
| smUserEndpointAccess             | userEndpoint_id                                   | int         | int            | NO            |             |
| smUserEndpointAccess             | userType_id                                       | int         | int            | NO            |             |
| smUserEndpointInstance           | oid                                               | int         | int            | NO            | Primary Key |
| smUserEndpointInstance           | authenticationSystem_id                           | int         | int            | NO            |             |
| smUserEndpointInstance           | classoid                                          | int         | int            | NO            |             |
| smUserEndpointInstance           | endpoint_id                                       | int         | int            | NO            |             |
| smUserEndpointInstance           | module_id                                         | int         | int            | NO            |             |
| smUserEndpointInstance           | parent_id                                         | int         | int            | NO            |             |
| smUserEndpointType               | oid                                               | int         | int            | NO            | Primary Key |
| smUserEndpointType               | classoid                                          | int         | int            | NO            |             |
| smUserEndpointType               | description_id                                    | int         | int            | NO            |             |
| smUserEndpointType               | label_id                                          | int         | int            | NO            |             |
| smUserEndpointType               | module_id                                         | int         | int            | NO            |             |
| smUserEndpointType               | name                                              | varchar     | varchar(255)   | NO            |             |
| smUserEndpointType               | pageType_id                                       | int         | int            | NO            |             |
| smUserType                       | oid                                               | int         | int            | NO            | Primary Key |
| smUserType                       | baseType_id                                       | int         | int            | NO            |             |
| smUserType                       | classoid                                          | int         | int            | NO            |             |
| smUserType                       | defaultRole_id                                    | int         | int            | NO            |             |
| smUserType                       | description_id                                    | int         | int            | NO            |             |
| smUserType                       | label_id                                          | int         | int            | NO            |             |
| smUserType                       | module_id                                         | int         | int            | NO            |             |
| smUserType                       | name                                              | varchar     | varchar(255)   | NO            |             |
| smUserType                       | userClass                                         | varchar     | varchar(255)   | NO            |             |
| smUserTypePermType               | oid                                               | int         | int            | NO            | Primary Key |
| smUserTypePermType               | classoid                                          | int         | int            | NO            |             |
| smUserTypePermType               | description_id                                    | int         | int            | NO            |             |
| smUserTypePermType               | label_id                                          | int         | int            | NO            |             |
| smUserTypePermType               | module_id                                         | int         | int            | NO            |             |
| smUserTypePermType               | name                                              | varchar     | varchar(255)   | NO            |             |
| smUserTypePermType               | permissionType_id                                 | int         | int            | NO            |             |
| smUserTypePermType               | required                                          | varchar     | varchar(10)    | NO            |             |
| smUserTypePermType               | userType_id                                       | int         | int            | NO            |             |
| smUserTypeRight                  | oid                                               | int         | int            | NO            | Primary Key |
| smUserTypeRight                  | child_id                                          | int         | int            | NO            |             |
| smUserTypeRight                  | classoid                                          | int         | int            | NO            |             |
| smUserTypeRight                  | module_id                                         | int         | int            | NO            |             |
| smUserTypeRight                  | parent_id                                         | int         | int            | NO            |             |
| smXMLNamespace                   | oid                                               | int         | int            | NO            | Primary Key |
| smXMLNamespace                   | alias                                             | varchar     | varchar(255)   | NO            |             |
| smXMLNamespace                   | classoid                                          | int         | int            | NO            |             |
| smXMLNamespace                   | module_id                                         | int         | int            | NO            |             |
| smXMLNamespace                   | schema_url                                        | text        | text           | NO            |             |
| smXMLNamespace                   | template_id                                       | int         | int            | NO            |             |
| sysActionCache                   | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysActionCache                   | action_id                                         | int         | int            | NO            | Foreign Key |
| sysActionCache                   | actionKey                                         | varchar     | varchar(255)   | NO            |             |
| sysActionCache                   | classoid                                          | int         | int            | NO            |             |
| sysActionCache                   | executionCount                                    | bigint      | bigint         | NO            |             |
| sysAppServiceStatus              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysAppServiceStatus              | applicationServer_id                              | int         | int            | NO            |             |
| sysAppServiceStatus              | classoid                                          | int         | int            | NO            |             |
| sysAppServiceStatus              | instance_id                                       | int         | int            | NO            |             |
| sysAppServiceStatus              | messages                                          | text        | text           | NO            |             |
| sysAppServiceStatus              | name                                              | varchar     | varchar(255)   | NO            |             |
| sysAppServiceStatus              | object_id                                         | int         | int            | NO            |             |
| sysAppServiceStatus              | service_id                                        | int         | int            | NO            |             |
| sysAppServiceStatus              | startDate                                         | datetime    | datetime       | NO            |             |
| sysAppServiceStatus              | status                                            | varchar     | varchar(255)   | NO            |             |
| sysAppServiceStatus              | stopDate                                          | datetime    | datetime       | NO            |             |
| sysApplicationEvent              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysApplicationEvent              | classoid                                          | int         | int            | NO            |             |
| sysApplicationEvent              | data                                              | text        | text           | NO            |             |
| sysApplicationEvent              | event                                             | varchar     | varchar(255)   | NO            |             |
| sysApplicationEvent              | fromStatus                                        | varchar     | varchar(255)   | NO            |             |
| sysApplicationEvent              | server_id                                         | int         | int            | NO            |             |
| sysApplicationEvent              | serverName                                        | varchar     | varchar(255)   | NO            |             |
| sysApplicationEvent              | timestamp                                         | datetime    | datetime       | NO            |             |
| sysApplicationEvent              | toStatus                                          | varchar     | varchar(255)   | NO            |             |
| sysApplicationEvent              | version_id                                        | int         | int            | NO            |             |
| sysApplicationVersion            | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysApplicationVersion            | application_id                                    | int         | int            | NO            |             |
| sysApplicationVersion            | buildNo                                           | int         | int            | NO            |             |
| sysApplicationVersion            | classoid                                          | int         | int            | NO            |             |
| sysApplicationVersion            | currentStatus                                     | varchar     | varchar(255)   | NO            |             |
| sysApplicationVersion            | desiredStatus                                     | varchar     | varchar(255)   | NO            |             |
| sysApplicationVersion            | modelSchema                                       | varchar     | varchar(255)   | NO            |             |
| sysApplicationVersion            | version                                           | varchar     | varchar(255)   | NO            |             |
| sysArchivedMessage               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysArchivedMessage               | account_id                                        | int         | int            | NO            | Foreign Key |
| sysArchivedMessage               | content_id                                        | int         | int            | NO            | Foreign Key |
| sysArchivedMessage               | endpoint_id                                       | int         | int            | NO            | Foreign Key |
| sysArchivedMessage               | recipient_id                                      | int         | int            | NO            | Foreign Key |
| sysArchivedMessage               | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| sysArchivedMessage               | timestamp                                         | datetime    | datetime       | NO            | Foreign Key |
| sysArchivedMessage               | classoid                                          | int         | int            | NO            |             |
| sysArchivedMessage               | instance_id                                       | int         | int            | NO            |             |
| sysArchivedMessage               | message                                           | text        | text           | NO            |             |
| sysArchivedMessage               | recipientName                                     | varchar     | varchar(255)   | NO            |             |
| sysArchivedMessage               | recipientType_id                                  | int         | int            | NO            |             |
| sysArchivedPoolItem              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysArchivedPoolItem              | action_id                                         | int         | int            | NO            | Foreign Key |
| sysArchivedPoolItem              | itemId                                            | char        | char(36)       | NO            | Foreign Key |
| sysArchivedPoolItem              | pool_id                                           | int         | int            | NO            | Foreign Key |
| sysArchivedPoolItem              | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| sysArchivedPoolItem              | classoid                                          | int         | int            | NO            |             |
| sysArchivedPoolItem              | completedTime                                     | datetime    | datetime       | NO            |             |
| sysArchivedPoolItem              | exception                                         | text        | text           | NO            |             |
| sysArchivedPoolItem              | groupName                                         | varchar     | varchar(255)   | NO            |             |
| sysArchivedPoolItem              | messages                                          | text        | text           | NO            |             |
| sysArchivedPoolItem              | name                                              | varchar     | varchar(255)   | NO            |             |
| sysArchivedPoolItem              | parameters                                        | text        | text           | NO            |             |
| sysArchivedPoolItem              | priority                                          | int         | int            | NO            |             |
| sysArchivedPoolItem              | requestedTime                                     | datetime    | datetime       | NO            |             |
| sysArchivedPoolItem              | startedTime                                       | datetime    | datetime       | NO            |             |
| sysArchivedPoolItem              | user_id                                           | int         | int            | NO            |             |
| sysAttributeConflict             | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysAttributeConflict             | objectConflict_id                                 | int         | int            | NO            | Foreign Key |
| sysAttributeConflict             | action                                            | varchar     | varchar(255)   | NO            |             |
| sysAttributeConflict             | attribute_id                                      | int         | int            | NO            |             |
| sysAttributeConflict             | classoid                                          | int         | int            | NO            |             |
| sysAttributeConflict             | currentDisplay                                    | varchar     | varchar(255)   | NO            |             |
| sysAttributeConflict             | currentValue                                      | text        | text           | NO            |             |
| sysAttributeConflict             | globalAttribute_id                                | int         | int            | NO            |             |
| sysAttributeConflict             | modifiedValue                                     | text        | text           | NO            |             |
| sysAttributeConflict             | name                                              | varchar     | varchar(255)   | NO            |             |
| sysAttributeConflict             | newDisplay                                        | varchar     | varchar(255)   | NO            |             |
| sysAttributeConflict             | newValue                                          | text        | text           | NO            |             |
| sysAttributeConflict             | resolutionMode                                    | varchar     | varchar(255)   | NO            |             |
| sysAttributeConflict             | status                                            | varchar     | varchar(255)   | NO            |             |
| sysCalendar                      | oid                                               | int         | int            | NO            | Primary Key |
| sysCalendar                      | classoid                                          | int         | int            | NO            |             |
| sysCalendar                      | country_id                                        | int         | int            | NO            |             |
| sysCalendar                      | description                                       | varchar     | varchar(255)   | NO            |             |
| sysCalendar                      | endDate                                           | datetime    | datetime       | NO            |             |
| sysCalendar                      | interval_id                                       | int         | int            | NO            |             |
| sysCalendar                      | inverseDays                                       | varchar     | varchar(10)    | NO            |             |
| sysCalendar                      | name                                              | varchar     | varchar(255)   | NO            |             |
| sysCalendar                      | startDate                                         | datetime    | datetime       | NO            |             |
| sysCalendar                      | status                                            | varchar     | varchar(255)   | NO            |             |
| sysCalendarDay                   | oid                                               | int         | int            | NO            | Primary Key |
| sysCalendarDay                   | calendar_id                                       | int         | int            | NO            |             |
| sysCalendarDay                   | classoid                                          | int         | int            | NO            |             |
| sysCalendarDay                   | day                                               | datetime    | datetime       | NO            |             |
| sysCalendarDay                   | description                                       | varchar     | varchar(255)   | NO            |             |
| sysCalendarDay                   | type                                              | varchar     | varchar(255)   | NO            |             |
| sysCalendarOptions               | oid                                               | int         | int            | NO            | Primary Key |
| sysCalendarOptions               | classoid                                          | int         | int            | NO            |             |
| sysCalendarOptions               | firstDayWeek                                      | int         | int            | NO            |             |
| sysCalendarOptions               | firstHourDay                                      | varchar     | varchar(255)   | NO            |             |
| sysCalendarOptions               | firstMonthYear                                    | int         | int            | NO            |             |
| sysCalendarOptions               | name                                              | varchar     | varchar(255)   | NO            |             |
| sysCodeCompilation               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysCodeCompilation               | classoid                                          | int         | int            | NO            |             |
| sysCodeCompilation               | endTime                                           | datetime    | datetime       | NO            |             |
| sysCodeCompilation               | startTime                                         | datetime    | datetime       | NO            |             |
| sysCodeCompilation               | status                                            | varchar     | varchar(255)   | NO            |             |
| sysCodeCompilation               | type                                              | varchar     | varchar(255)   | NO            |             |
| sysCodeCompilation               | user_id                                           | int         | int            | NO            |             |
| sysCompiledCode                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysCompiledCode                  | className                                         | varchar     | varchar(255)   | NO            | Foreign Key |
| sysCompiledCode                  | classoid                                          | int         | int            | NO            |             |
| sysCompiledCode                  | content                                           | mediumtext  | mediumtext     | NO            |             |
| sysCompiledCode                  | generatedCode_id                                  | int         | int            | NO            |             |
| sysCountry                       | oid                                               | int         | int            | NO            | Primary Key |
| sysCountry                       | classoid                                          | int         | int            | NO            |             |
| sysCountry                       | code                                              | varchar     | varchar(255)   | NO            |             |
| sysCountry                       | name                                              | varchar     | varchar(255)   | NO            |             |
| sysCredentials                   | oid                                               | int         | int            | NO            | Primary Key |
| sysCredentials                   | password                                          | varchar     | varchar(255)   | NO            | Foreign Key |
| sysCredentials                   | user_id                                           | int         | int            | NO            | Foreign Key |
| sysCredentials                   | username                                          | varchar     | varchar(255)   | NO            | Foreign Key |
| sysCredentials                   | attempts                                          | int         | int            | NO            |             |
| sysCredentials                   | classoid                                          | int         | int            | NO            |             |
| sysCredentials                   | creationDate                                      | datetime    | datetime       | NO            |             |
| sysCredentials                   | expiration                                        | datetime    | datetime       | NO            |             |
| sysCredentials                   | policy_id                                         | int         | int            | NO            |             |
| sysCredentials                   | salt                                              | char        | char(36)       | NO            |             |
| sysCredentials                   | security_id                                       | int         | int            | NO            |             |
| sysCredentials                   | status                                            | varchar     | varchar(255)   | NO            |             |
| sysCredentials                   | system_id                                         | int         | int            | NO            |             |
| sysCredentials                   | tempPassword                                      | varchar     | varchar(255)   | NO            |             |
| sysCredentialsHistory            | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysCredentialsHistory            | changedby_id                                      | int         | int            | NO            |             |
| sysCredentialsHistory            | classoid                                          | int         | int            | NO            |             |
| sysCredentialsHistory            | credentials_id                                    | int         | int            | NO            |             |
| sysCredentialsHistory            | password                                          | varchar     | varchar(255)   | NO            |             |
| sysCredentialsHistory            | policy_id                                         | int         | int            | NO            |             |
| sysCredentialsHistory            | timestamp                                         | datetime    | datetime       | NO            |             |
| sysCredentialsHistory            | username                                          | varchar     | varchar(255)   | NO            |             |
| sysCurrency                      | oid                                               | int         | int            | NO            | Primary Key |
| sysCurrency                      | classoid                                          | int         | int            | NO            |             |
| sysCurrency                      | code                                              | varchar     | varchar(255)   | NO            |             |
| sysCurrency                      | name                                              | varchar     | varchar(255)   | NO            |             |
| sysCustomAttributeValue          | oid                                               | int         | int            | NO            | Primary Key |
| sysCustomAttributeValue          | attribute_id                                      | int         | int            | NO            |             |
| sysCustomAttributeValue          | classoid                                          | int         | int            | NO            |             |
| sysCustomAttributeValue          | custom_id                                         | int         | int            | NO            |             |
| sysCustomAttributeValue          | object_id                                         | int         | int            | NO            |             |
| sysCustomAttributeValue          | value                                             | varchar     | varchar(255)   | NO            |             |
| sysDevice                        | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysDevice                        | deviceId                                          | varchar     | varchar(255)   | NO            | Foreign Key |
| sysDevice                        | classoid                                          | int         | int            | NO            |             |
| sysDevice                        | description                                       | text        | text           | NO            |             |
| sysDevice                        | deviceModel_id                                    | int         | int            | NO            |             |
| sysDevice                        | macAddress                                        | varchar     | varchar(255)   | NO            |             |
| sysDevice                        | userAgent_id                                      | int         | int            | NO            |             |
| sysDeviceModel                   | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysDeviceModel                   | classoid                                          | int         | int            | NO            |             |
| sysDeviceModel                   | manufacturer                                      | varchar     | varchar(255)   | NO            |             |
| sysDeviceModel                   | name                                              | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticIssue               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysDiagnosticIssue               | issueGroup_id                                     | int         | int            | NO            | Foreign Key |
| sysDiagnosticIssue               | result_id                                         | int         | int            | NO            | Foreign Key |
| sysDiagnosticIssue               | classoid                                          | int         | int            | NO            |             |
| sysDiagnosticIssue               | description                                       | text        | text           | NO            |             |
| sysDiagnosticIssue               | name                                              | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticIssue               | object_id                                         | int         | int            | NO            |             |
| sysDiagnosticIssue               | objectType_id                                     | int         | int            | NO            |             |
| sysDiagnosticIssue               | resolution_id                                     | int         | int            | NO            |             |
| sysDiagnosticIssue               | status                                            | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticIssue               | type_id                                           | int         | int            | NO            |             |
| sysDiagnosticIssueGroup          | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysDiagnosticIssueGroup          | result_id                                         | int         | int            | NO            | Foreign Key |
| sysDiagnosticIssueGroup          | classoid                                          | int         | int            | NO            |             |
| sysDiagnosticIssueGroup          | issueType_id                                      | int         | int            | NO            |             |
| sysDiagnosticIssueGroup          | name                                              | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticIssueParam          | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysDiagnosticIssueParam          | issue_id                                          | int         | int            | NO            | Foreign Key |
| sysDiagnosticIssueParam          | classoid                                          | int         | int            | NO            |             |
| sysDiagnosticIssueParam          | name                                              | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticIssueParam          | type_id                                           | int         | int            | NO            |             |
| sysDiagnosticIssueParam          | value                                             | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticResult              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysDiagnosticResult              | diagnostic_id                                     | int         | int            | NO            | Foreign Key |
| sysDiagnosticResult              | instance_id                                       | int         | int            | NO            | Foreign Key |
| sysDiagnosticResult              | archive                                           | varchar     | varchar(10)    | NO            |             |
| sysDiagnosticResult              | classoid                                          | int         | int            | NO            |             |
| sysDiagnosticResult              | granularity_id                                    | int         | int            | NO            |             |
| sysDiagnosticResult              | messageData                                       | text        | text           | NO            |             |
| sysDiagnosticResult              | name                                              | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticResult              | parent_id                                         | int         | int            | NO            |             |
| sysDiagnosticResult              | serializedData                                    | text        | text           | NO            |             |
| sysDiagnosticResult              | startTime                                         | datetime    | datetime       | NO            |             |
| sysDiagnosticResult              | status                                            | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticResult              | subtype_id                                        | int         | int            | NO            |             |
| sysDiagnosticResult              | threshold_id                                      | int         | int            | NO            |             |
| sysDiagnosticResult              | timestamp                                         | datetime    | datetime       | NO            |             |
| sysDiagnosticResult              | unit_id                                           | int         | int            | NO            |             |
| sysDiagnosticResult              | user_id                                           | int         | int            | NO            |             |
| sysDiagnosticResult              | value                                             | decimal     | decimal(19,2)  | NO            |             |
| sysDiagnosticSubtype             | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysDiagnosticSubtype             | diagnostic_id                                     | int         | int            | NO            | Foreign Key |
| sysDiagnosticSubtype             | classoid                                          | int         | int            | NO            |             |
| sysDiagnosticSubtype             | description                                       | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticSubtype             | name                                              | varchar     | varchar(255)   | NO            |             |
| sysDiagnosticSubtype             | reference_id                                      | int         | int            | NO            |             |
| sysDiagnosticSubtype             | reference_type                                    | int         | int            | NO            |             |
| sysDocument                      | oid                                               | int         | int            | NO            | Primary Key |
| sysDocument                      | doctype_id                                        | int         | int            | NO            | Foreign Key |
| sysDocument                      | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| sysDocument                      | owner_type                                        | int         | int            | NO            | Foreign Key |
| sysDocument                      | classoid                                          | int         | int            | NO            |             |
| sysDocument                      | coverPage_id                                      | int         | int            | NO            |             |
| sysDocument                      | createdBy                                         | int         | int            | NO            |             |
| sysDocument                      | creationDate                                      | datetime    | datetime       | NO            |             |
| sysDocument                      | description_id                                    | int         | int            | NO            |             |
| sysDocument                      | fileName                                          | varchar     | varchar(255)   | NO            |             |
| sysDocument                      | filetype_id                                       | int         | int            | NO            |             |
| sysDocument                      | folder_id                                         | int         | int            | NO            |             |
| sysDocument                      | label_id                                          | int         | int            | NO            |             |
| sysDocument                      | language_id                                       | int         | int            | NO            |             |
| sysDocument                      | owner_id                                          | int         | int            | NO            |             |
| sysDocument                      | parent_id                                         | int         | int            | NO            |             |
| sysDocument                      | referenceId                                       | char        | char(36)       | NO            |             |
| sysDocument                      | reportRelation_id                                 | int         | int            | NO            |             |
| sysDocument                      | repository_id                                     | int         | int            | NO            |             |
| sysDocument                      | status                                            | varchar     | varchar(255)   | NO            |             |
| sysDocument                      | tableOfContents_id                                | int         | int            | NO            |             |
| sysDocument                      | template_id                                       | int         | int            | NO            |             |
| sysDocument                      | type_id                                           | int         | int            | NO            |             |
| sysDocument                      | version                                           | int         | int            | NO            |             |
| sysEvent                         | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysEvent                         | action_id                                         | int         | int            | NO            | Foreign Key |
| sysEvent                         | reference_id                                      | int         | int            | NO            | Foreign Key |
| sysEvent                         | actionEvent_id                                    | int         | int            | NO            |             |
| sysEvent                         | classoid                                          | int         | int            | NO            |             |
| sysEvent                         | eventCode                                         | varchar     | varchar(255)   | NO            |             |
| sysEvent                         | eventData                                         | text        | text           | NO            |             |
| sysEvent                         | partitionNo                                       | int         | int            | NO            |             |
| sysEvent                         | referenceKey                                      | varchar     | varchar(255)   | NO            |             |
| sysEvent                         | referenceType                                     | int         | int            | NO            |             |
| sysEvent                         | timestamp                                         | datetime    | datetime       | NO            |             |
| sysEvent                         | user_id                                           | int         | int            | NO            |             |
| sysGeneratedCode                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGeneratedCode                 | classoid                                          | int         | int            | NO            |             |
| sysGeneratedCode                 | codeTemplate_id                                   | int         | int            | NO            |             |
| sysGeneratedCode                 | message                                           | text        | text           | NO            |             |
| sysGeneratedCode                 | name                                              | varchar     | varchar(255)   | NO            |             |
| sysGeneratedCode                 | objectContext_id                                  | int         | int            | NO            |             |
| sysGeneratedCode                 | sourceCode                                        | mediumtext  | mediumtext     | NO            |             |
| sysGeneratedCode                 | status                                            | varchar     | varchar(255)   | NO            |             |
| sysGeneratedCode                 | timestamp                                         | datetime    | datetime       | NO            |             |
| sysGlobalAttribute               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGlobalAttribute               | attribute_id                                      | int         | int            | NO            |             |
| sysGlobalAttribute               | classoid                                          | int         | int            | NO            |             |
| sysGlobalAttribute               | module_id                                         | int         | int            | NO            |             |
| sysGlobalAttribute               | originalValue                                     | text        | text           | NO            |             |
| sysGlobalKey                     | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGlobalKey                     | currentVersion_id                                 | int         | int            | NO            | Foreign Key |
| sysGlobalKey                     | globalKey                                         | char        | char(36)       | NO            | Foreign Key |
| sysGlobalKey                     | localKey                                          | int         | int            | NO            | Foreign Key |
| sysGlobalKey                     | object_id                                         | int         | int            | NO            | Foreign Key |
| sysGlobalKey                     | originalVersion_id                                | int         | int            | NO            | Foreign Key |
| sysGlobalKey                     | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| sysGlobalKey                     | transactionGroup_id                               | int         | int            | NO            | Foreign Key |
| sysGlobalKey                     | classoid                                          | int         | int            | NO            |             |
| sysGlobalKey                     | deleted                                           | varchar     | varchar(10)    | NO            |             |
| sysGlobalKey                     | keyVersion_id                                     | int         | int            | NO            |             |
| sysGlobalKey                     | name                                              | varchar     | varchar(255)   | NO            |             |
| sysGlobalKey                     | originalVersionNo                                 | int         | int            | NO            |             |
| sysGlobalKey                     | versionNo                                         | int         | int            | NO            |             |
| sysGlobalKeyModule               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGlobalKeyModule               | classoid                                          | int         | int            | NO            |             |
| sysGlobalKeyModule               | globalKey_id                                      | int         | int            | NO            |             |
| sysGlobalKeyModule               | module_id                                         | int         | int            | NO            |             |
| sysGlobalKeyModule               | version_id                                        | int         | int            | NO            |             |
| sysGlobalKeyModule               | versionNo                                         | int         | int            | NO            |             |
| sysGlobalKeyVersion              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGlobalKeyVersion              | globalKey_id                                      | int         | int            | NO            | Foreign Key |
| sysGlobalKeyVersion              | transaction_id                                    | int         | int            | NO            | Foreign Key |
| sysGlobalKeyVersion              | classoid                                          | int         | int            | NO            |             |
| sysGlobalKeyVersion              | module_id                                         | int         | int            | NO            |             |
| sysGlobalKeyVersion              | name                                              | varchar     | varchar(255)   | NO            |             |
| sysGlobalKeyVersion              | operation                                         | varchar     | varchar(255)   | NO            |             |
| sysGlobalKeyVersion              | previous_id                                       | int         | int            | NO            |             |
| sysGlobalKeyVersion              | version_id                                        | int         | int            | NO            |             |
| sysGlobalKeyVersion              | versionNo                                         | int         | int            | NO            |             |
| sysGlobalModule                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGlobalModule                  | classoid                                          | int         | int            | NO            |             |
| sysGlobalModule                  | defaultGroup_id                                   | int         | int            | NO            |             |
| sysGlobalModule                  | globalKey                                         | char        | char(36)       | NO            |             |
| sysGlobalModule                  | lastModified                                      | char        | char(36)       | NO            |             |
| sysGlobalModule                  | module_id                                         | int         | int            | NO            |             |
| sysGlobalModule                  | nextId                                            | int         | int            | NO            |             |
| sysGlobalObjVersion              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGlobalObjVersion              | object_id                                         | int         | int            | NO            | Foreign Key |
| sysGlobalObjVersion              | version_id                                        | int         | int            | NO            | Foreign Key |
| sysGlobalObjVersion              | classoid                                          | int         | int            | NO            |             |
| sysGlobalObjVersion              | globalKey                                         | char        | char(36)       | NO            |             |
| sysGlobalObjVersion              | lastModified                                      | char        | char(36)       | NO            |             |
| sysGlobalObject                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGlobalObject                  | object_id                                         | int         | int            | NO            | Foreign Key |
| sysGlobalObject                  | classoid                                          | int         | int            | NO            |             |
| sysGlobalObject                  | globalKey                                         | char        | char(36)       | NO            |             |
| sysGlobalObject                  | lastModified                                      | char        | char(36)       | NO            |             |
| sysGlobalObject                  | module_id                                         | int         | int            | NO            |             |
| sysGlobalVersion                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysGlobalVersion                 | module_id                                         | int         | int            | NO            | Foreign Key |
| sysGlobalVersion                 | version_id                                        | int         | int            | NO            | Foreign Key |
| sysGlobalVersion                 | classoid                                          | int         | int            | NO            |             |
| sysGlobalVersion                 | globalKey                                         | char        | char(36)       | NO            |             |
| sysGlobalVersion                 | lastModified                                      | char        | char(36)       | NO            |             |
| sysImportedItem                  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysImportedItem                  | externaltoken                                     | varchar     | varchar(255)   | NO            | Foreign Key |
| sysImportedItem                  | importedStamp                                     | datetime    | datetime       | NO            | Foreign Key |
| sysImportedItem                  | timestamp                                         | datetime    | datetime       | NO            | Foreign Key |
| sysImportedItem                  | classoid                                          | int         | int            | NO            |             |
| sysImportedItem                  | config_id                                         | int         | int            | NO            |             |
| sysImportedItem                  | content                                           | mediumtext  | mediumtext     | NO            |             |
| sysImportedItem                  | errors                                            | mediumtext  | mediumtext     | NO            |             |
| sysImportedItem                  | importer_id                                       | int         | int            | NO            |             |
| sysImportedItem                  | interfaceInstance_id                              | int         | int            | NO            |             |
| sysImportedItem                  | modifiedContent                                   | mediumtext  | mediumtext     | NO            |             |
| sysImportedItem                  | partitionNo                                       | int         | int            | NO            |             |
| sysImportedItem                  | response                                          | mediumtext  | mediumtext     | NO            |             |
| sysImportedItem                  | source_id                                         | int         | int            | NO            |             |
| sysImportedItem                  | startTime                                         | datetime    | datetime       | NO            |             |
| sysImportedItem                  | status                                            | varchar     | varchar(255)   | NO            |             |
| sysImportingItem                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysImportingItem                 | startTime                                         | datetime    | datetime       | NO            | Foreign Key |
| sysImportingItem                 | timestamp                                         | datetime    | datetime       | NO            | Foreign Key |
| sysImportingItem                 | classoid                                          | int         | int            | NO            |             |
| sysImportingItem                 | config_id                                         | int         | int            | NO            |             |
| sysImportingItem                 | content                                           | mediumtext  | mediumtext     | NO            |             |
| sysImportingItem                 | endTime                                           | datetime    | datetime       | NO            |             |
| sysImportingItem                 | errors                                            | mediumtext  | mediumtext     | NO            |             |
| sysImportingItem                 | externaltoken                                     | varchar     | varchar(255)   | NO            |             |
| sysImportingItem                 | importer_id                                       | int         | int            | NO            |             |
| sysImportingItem                 | interfaceInstance_id                              | int         | int            | NO            |             |
| sysImportingItem                 | modifiedContent                                   | mediumtext  | mediumtext     | NO            |             |
| sysImportingItem                 | response                                          | mediumtext  | mediumtext     | NO            |             |
| sysImportingItem                 | source_id                                         | int         | int            | NO            |             |
| sysImportingItem                 | status                                            | varchar     | varchar(255)   | NO            |             |
| sysInstalledModule               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysInstalledModule               | applicationVersion_id                             | int         | int            | NO            |             |
| sysInstalledModule               | buildDate                                         | datetime    | datetime       | NO            |             |
| sysInstalledModule               | buildNo                                           | int         | int            | NO            |             |
| sysInstalledModule               | classoid                                          | int         | int            | NO            |             |
| sysInstalledModule               | globalKey                                         | char        | char(36)       | NO            |             |
| sysInstalledModule               | lastModified                                      | char        | char(36)       | NO            |             |
| sysInstalledModule               | name                                              | varchar     | varchar(255)   | NO            |             |
| sysInstalledModule               | version                                           | varchar     | varchar(255)   | NO            |             |
| sysInterfaceArchive              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysInterfaceArchive              | timestamp                                         | datetime    | datetime       | NO            | Foreign Key |
| sysInterfaceArchive              | archivedDate                                      | datetime    | datetime       | NO            |             |
| sysInterfaceArchive              | classoid                                          | int         | int            | NO            |             |
| sysInterfaceArchive              | config_id                                         | int         | int            | NO            |             |
| sysInterfaceArchive              | content                                           | mediumtext  | mediumtext     | NO            |             |
| sysInterfaceArchive              | createdDate                                       | datetime    | datetime       | NO            |             |
| sysInterfaceArchive              | destination_id                                    | int         | int            | NO            |             |
| sysInterfaceArchive              | event_id                                          | int         | int            | NO            |             |
| sysInterfaceArchive              | exporterTrigger_id                                | int         | int            | NO            |             |
| sysInterfaceArchive              | externalToken                                     | varchar     | varchar(255)   | NO            |             |
| sysInterfaceArchive              | interfaceInstance_id                              | int         | int            | NO            |             |
| sysInterfaceArchive              | message                                           | text        | text           | NO            |             |
| sysInterfaceArchive              | partitionNo                                       | int         | int            | NO            |             |
| sysInterfaceArchive              | response                                          | text        | text           | NO            |             |
| sysInterfaceArchive              | status                                            | varchar     | varchar(255)   | NO            |             |
| sysInterfaceArchive              | trigger_id                                        | int         | int            | NO            |             |
| sysInterfaceError                | oid                                               | int         | int            | NO            | Primary Key |
| sysInterfaceError                | classoid                                          | int         | int            | NO            |             |
| sysInterfaceError                | cron_id                                           | int         | int            | NO            |             |
| sysInterfaceError                | endTime                                           | datetime    | datetime       | NO            |             |
| sysInterfaceError                | exception                                         | text        | text           | NO            |             |
| sysInterfaceError                | interface_id                                      | int         | int            | NO            |             |
| sysInterfaceError                | lastRetry                                         | datetime    | datetime       | NO            |             |
| sysInterfaceError                | message                                           | text        | text           | NO            |             |
| sysInterfaceError                | startTime                                         | datetime    | datetime       | NO            |             |
| sysInterfaceError                | status                                            | varchar     | varchar(255)   | NO            |             |
| sysLanguage                      | oid                                               | int         | int            | NO            | Primary Key |
| sysLanguage                      | code                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| sysLanguage                      | active                                            | varchar     | varchar(10)    | NO            |             |
| sysLanguage                      | classoid                                          | int         | int            | NO            |             |
| sysLanguage                      | language                                          | varchar     | varchar(255)   | NO            |             |
| sysLanguage                      | locale                                            | varchar     | varchar(255)   | NO            |             |
| sysLanguage                      | name                                              | varchar     | varchar(255)   | NO            |             |
| sysLocaleConfiguration           | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysLocaleConfiguration           | attribute_id                                      | int         | int            | NO            |             |
| sysLocaleConfiguration           | classoid                                          | int         | int            | NO            |             |
| sysLocaleConfiguration           | language_id                                       | int         | int            | NO            |             |
| sysLocaleConfiguration           | user_id                                           | int         | int            | NO            |             |
| sysLocaleConfiguration           | value                                             | varchar     | varchar(255)   | NO            |             |
| sysLocalizableItem               | oid                                               | int         | int            | NO            | Primary Key |
| sysLocalizableItem               | attribute_id                                      | int         | int            | NO            |             |
| sysLocalizableItem               | classoid                                          | int         | int            | NO            |             |
| sysLocalizableItem               | owner_id                                          | int         | int            | NO            |             |
| sysLocalizableItem               | owner_type                                        | int         | int            | NO            |             |
| sysLocalizableValue              | oid                                               | int         | int            | NO            | Primary Key |
| sysLocalizableValue              | localizable_id                                    | int         | int            | NO            | Foreign Key |
| sysLocalizableValue              | autotranslated                                    | varchar     | varchar(10)    | NO            |             |
| sysLocalizableValue              | classoid                                          | int         | int            | NO            |             |
| sysLocalizableValue              | language                                          | varchar     | varchar(255)   | NO            |             |
| sysLocalizableValue              | message                                           | mediumtext  | mediumtext     | NO            |             |
| sysLockEntry                     | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysLockEntry                     | classoid                                          | int         | int            | NO            |             |
| sysLockEntry                     | lockKey                                           | varchar     | varchar(255)   | NO            |             |
| sysLockEntry                     | name                                              | varchar     | varchar(255)   | NO            |             |
| sysLockEntry                     | server_id                                         | int         | int            | NO            |             |
| sysLockEntry                     | status                                            | varchar     | varchar(255)   | NO            |             |
| sysLockEntry                     | timestamp                                         | datetime    | datetime       | NO            |             |
| sysLockEntry                     | type                                              | varchar     | varchar(255)   | NO            |             |
| sysLockEntry                     | user_id                                           | int         | int            | NO            |             |
| sysMessageContent                | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysMessageContent                | endpoint_id                                       | int         | int            | NO            | Foreign Key |
| sysMessageContent                | message_id                                        | int         | int            | NO            | Foreign Key |
| sysMessageContent                | reference_id                                      | int         | int            | NO            | Foreign Key |
| sysMessageContent                | status                                            | varchar     | varchar(255)   | NO            | Foreign Key |
| sysMessageContent                | attachments                                       | text        | text           | NO            |             |
| sysMessageContent                | classoid                                          | int         | int            | NO            |             |
| sysMessageContent                | content                                           | text        | text           | NO            |             |
| sysMessageContent                | creationDate                                      | datetime    | datetime       | NO            |             |
| sysMessageContent                | format_id                                         | int         | int            | NO            |             |
| sysMessageContent                | referenceType                                     | int         | int            | NO            |             |
| sysMessageContent                | sentDate                                          | datetime    | datetime       | NO            |             |
| sysMessageContent                | title                                             | varchar     | varchar(255)   | NO            |             |
| sysMessageContent                | type_id                                           | int         | int            | NO            |             |
| sysMessageContent                | user_id                                           | int         | int            | NO            |             |
| sysMessageRecipientAccount       | oid                                               | int         | int            | NO            | Primary Key |
| sysMessageRecipientAccount       | recipient_id                                      | int         | int            | NO            | Foreign Key |
| sysMessageRecipientAccount       | accountName                                       | varchar     | varchar(255)   | NO            |             |
| sysMessageRecipientAccount       | classoid                                          | int         | int            | NO            |             |
| sysMessageRecipientAccount       | language_id                                       | int         | int            | NO            |             |
| sysMessageRecipientAccount       | type_id                                           | int         | int            | NO            |             |
| sysMessageSubscriptionRecipient  | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysMessageSubscriptionRecipient  | account_id                                        | int         | int            | NO            |             |
| sysMessageSubscriptionRecipient  | classoid                                          | int         | int            | NO            |             |
| sysMessageSubscriptionRecipient  | recipient_id                                      | int         | int            | NO            |             |
| sysMessageSubscriptionRecipient  | status                                            | varchar     | varchar(255)   | NO            |             |
| sysMessageSubscriptionRecipient  | subscriptionGroup_id                              | int         | int            | NO            |             |
| sysMigrationScriptEvent          | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysMigrationScriptEvent          | classoid                                          | int         | int            | NO            |             |
| sysMigrationScriptEvent          | messages                                          | text        | text           | NO            |             |
| sysMigrationScriptEvent          | migrationScript_id                                | int         | int            | NO            |             |
| sysMigrationScriptEvent          | moduleUpgrade_id                                  | int         | int            | NO            |             |
| sysMigrationScriptEvent          | status                                            | varchar     | varchar(255)   | NO            |             |
| sysMigrationScriptEvent          | timestamp                                         | datetime    | datetime       | NO            |             |
| sysMigrationScriptEvent          | user_id                                           | int         | int            | NO            |             |
| sysModuleUpgrade                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysModuleUpgrade                 | module_id                                         | int         | int            | NO            | Foreign Key |
| sysModuleUpgrade                 | user_id                                           | int         | int            | NO            | Foreign Key |
| sysModuleUpgrade                 | automatic                                         | varchar     | varchar(10)    | NO            |             |
| sysModuleUpgrade                 | classoid                                          | int         | int            | NO            |             |
| sysModuleUpgrade                 | conflictCount                                     | int         | int            | NO            |             |
| sysModuleUpgrade                 | fromBuildNo                                       | int         | int            | NO            |             |
| sysModuleUpgrade                 | fromVersion_id                                    | int         | int            | NO            |             |
| sysModuleUpgrade                 | incremental                                       | varchar     | varchar(10)    | NO            |             |
| sysModuleUpgrade                 | status                                            | varchar     | varchar(255)   | NO            |             |
| sysModuleUpgrade                 | timestamp                                         | datetime    | datetime       | NO            |             |
| sysModuleUpgrade                 | toBuildNo                                         | int         | int            | NO            |             |
| sysModuleUpgrade                 | toVersion_id                                      | int         | int            | NO            |             |
| sysModuleUpgrade                 | unresolvedConflictCount                           | int         | int            | NO            |             |
| sysModuleUpgrade                 | upgradeMode                                       | varchar     | varchar(255)   | NO            |             |
| sysObjectConflict                | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysObjectConflict                | classoid                                          | int         | int            | NO            |             |
| sysObjectConflict                | globalKey_id                                      | int         | int            | NO            |             |
| sysObjectConflict                | name                                              | varchar     | varchar(255)   | NO            |             |
| sysObjectConflict                | newVersion_id                                     | int         | int            | NO            |             |
| sysObjectConflict                | newVersionNo                                      | int         | int            | NO            |             |
| sysObjectConflict                | status                                            | varchar     | varchar(255)   | NO            |             |
| sysObjectConflict                | type                                              | varchar     | varchar(255)   | NO            |             |
| sysObjectConflict                | upgrade_id                                        | int         | int            | NO            |             |
| sysObjectHistory                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysObjectHistory                 | logger_id                                         | int         | int            | NO            | Foreign Key |
| sysObjectHistory                 | object_id                                         | int         | int            | NO            | Foreign Key |
| sysObjectHistory                 | parent_id                                         | int         | int            | NO            | Foreign Key |
| sysObjectHistory                 | timestamp                                         | datetime    | datetime       | NO            | Foreign Key |
| sysObjectHistory                 | user_id                                           | int         | int            | NO            | Foreign Key |
| sysObjectHistory                 | action                                            | varchar     | varchar(255)   | NO            |             |
| sysObjectHistory                 | classoid                                          | int         | int            | NO            |             |
| sysObjectHistory                 | content                                           | text        | text           | NO            |             |
| sysObjectHistory                 | objectKey                                         | int         | int            | NO            |             |
| sysObjectHistory                 | objectName                                        | varchar     | varchar(255)   | NO            |             |
| sysObjectHistory                 | parentKey                                         | int         | int            | NO            |             |
| sysObjectHistory                 | transaction_id                                    | int         | int            | NO            |             |
| sysObjectPermission              | oid                                               | int         | int            | NO            | Primary Key |
| sysObjectPermission              | classoid                                          | int         | int            | NO            |             |
| sysObjectPermission              | externalName                                      | varchar     | varchar(255)   | NO            |             |
| sysObjectPermission              | name                                              | varchar     | varchar(255)   | NO            |             |
| sysObjectPermission              | object_id                                         | int         | int            | NO            |             |
| sysObjectPermission              | type_id                                           | int         | int            | NO            |             |
| sysProcessProfiling              | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysProcessProfiling              | process_id                                        | int         | int            | NO            | Foreign Key |
| sysProcessProfiling              | requestId                                         | varchar     | varchar(255)   | NO            | Foreign Key |
| sysProcessProfiling              | serverStartTime                                   | datetime    | datetime       | NO            | Foreign Key |
| sysProcessProfiling              | session_id                                        | int         | int            | NO            | Foreign Key |
| sysProcessProfiling              | accessPoint_id                                    | int         | int            | NO            |             |
| sysProcessProfiling              | activeDBConnection                                | int         | int            | NO            |             |
| sysProcessProfiling              | classoid                                          | int         | int            | NO            |             |
| sysProcessProfiling              | clientExecutionTime                               | int         | int            | NO            |             |
| sysProcessProfiling              | clientNetworkTime                                 | int         | int            | NO            |             |
| sysProcessProfiling              | clientStartTime                                   | datetime    | datetime       | NO            |             |
| sysProcessProfiling              | firstTransitions                                  | varchar     | varchar(255)   | NO            |             |
| sysProcessProfiling              | fromState_id                                      | int         | int            | NO            |             |
| sysProcessProfiling              | ipAddress                                         | varchar     | varchar(255)   | NO            |             |
| sysProcessProfiling              | location                                          | varchar     | varchar(255)   | NO            |             |
| sysProcessProfiling              | location_id                                       | int         | int            | NO            |             |
| sysProcessProfiling              | parameters                                        | text        | text           | NO            |             |
| sysProcessProfiling              | queryDuplicateCount                               | int         | int            | NO            |             |
| sysProcessProfiling              | queryReadCount                                    | int         | int            | NO            |             |
| sysProcessProfiling              | queryWriteCount                                   | int         | int            | NO            |             |
| sysProcessProfiling              | response                                          | text        | text           | NO            |             |
| sysProcessProfiling              | responseSize                                      | int         | int            | NO            |             |
| sysProcessProfiling              | retryCount                                        | int         | int            | NO            |             |
| sysProcessProfiling              | rssi                                              | int         | int            | NO            |             |
| sysProcessProfiling              | serverExecutionTime                               | int         | int            | NO            |             |
| sysProcessProfiling              | serverProcessTime                                 | int         | int            | NO            |             |
| sysProcessProfiling              | serverUITime                                      | int         | int            | NO            |             |
| sysProcessProfiling              | signalStrength                                    | int         | int            | NO            |             |
| sysProcessProfiling              | speed                                             | int         | int            | NO            |             |
| sysProcessProfiling              | toState_id                                        | int         | int            | NO            |             |
| sysProcessProfiling              | transition_id                                     | int         | int            | NO            |             |
| sysProcessProfiling              | transitionCount                                   | int         | int            | NO            |             |
| sysProcessProfiling              | widget_id                                         | int         | int            | NO            |             |
| sysQuartzJobDetail               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysQuartzJobDetail               | scheduler_id                                      | int         | int            | NO            | Foreign Key |
| sysQuartzJobDetail               | classoid                                          | int         | int            | NO            |             |
| sysQuartzJobDetail               | jobGroup                                          | varchar     | varchar(255)   | NO            |             |
| sysQuartzJobDetail               | jobName                                           | varchar     | varchar(255)   | NO            |             |
| sysQuartzJobDetail               | nonConcurrent                                     | varchar     | varchar(10)    | NO            |             |
| sysQuartzJobDetail               | paused                                            | varchar     | varchar(10)    | NO            |             |
| sysQuartzJobDetail               | requestsRecovery                                  | varchar     | varchar(10)    | NO            |             |
| sysQuartzSchedulerInstance       | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysQuartzSchedulerInstance       | classoid                                          | int         | int            | NO            |             |
| sysQuartzSchedulerInstance       | name                                              | varchar     | varchar(255)   | NO            |             |
| sysQuartzSchedulerInstance       | scheduler_id                                      | int         | int            | NO            |             |
| sysQuartzSchedulerInstance       | server_id                                         | int         | int            | NO            |             |
| sysQuartzTrigger                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysQuartzTrigger                 | classoid                                          | int         | int            | NO            |             |
| sysQuartzTrigger                 | cronExpresion                                     | varchar     | varchar(255)   | NO            |             |
| sysQuartzTrigger                 | endTime                                           | datetime    | datetime       | NO            |             |
| sysQuartzTrigger                 | jobDetail_id                                      | int         | int            | NO            |             |
| sysQuartzTrigger                 | misfireInstruction                                | int         | int            | NO            |             |
| sysQuartzTrigger                 | name                                              | varchar     | varchar(255)   | NO            |             |
| sysQuartzTrigger                 | nextFireTime                                      | datetime    | datetime       | NO            |             |
| sysQuartzTrigger                 | previousFireTime                                  | datetime    | datetime       | NO            |             |
| sysQuartzTrigger                 | priority                                          | int         | int            | NO            |             |
| sysQuartzTrigger                 | startTime                                         | datetime    | datetime       | NO            |             |
| sysQuartzTrigger                 | state                                             | varchar     | varchar(255)   | NO            |             |
| sysQuartzTriggerInstance         | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysQuartzTriggerInstance         | classoid                                          | int         | int            | NO            |             |
| sysQuartzTriggerInstance         | instance_id                                       | int         | int            | NO            |             |
| sysQuartzTriggerInstance         | trigger_id                                        | int         | int            | NO            |             |
| sysQuickLinks                    | oid                                               | int         | int            | NO            | Primary Key |
| sysQuickLinks                    | classoid                                          | int         | int            | NO            |             |
| sysQuickLinks                    | keyvalue                                          | varchar     | varchar(255)   | NO            |             |
| sysQuickLinks                    | name                                              | varchar     | varchar(255)   | NO            |             |
| sysQuickLinks                    | sequence                                          | int         | int            | NO            |             |
| sysQuickLinks                    | user_id                                           | int         | int            | NO            |             |
| sysQuickLinks                    | widget_id                                         | int         | int            | NO            |             |
| sysStateProvince                 | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysStateProvince                 | code                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| sysStateProvince                 | country_id                                        | int         | int            | NO            | Foreign Key |
| sysStateProvince                 | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| sysStateProvince                 | classoid                                          | int         | int            | NO            |             |
| sysTransactionGroupUpgrade       | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysTransactionGroupUpgrade       | moduleUpgrade_id                                  | int         | int            | NO            | Foreign Key |
| sysTransactionGroupUpgrade       | transactionGroup_id                               | int         | int            | NO            | Foreign Key |
| sysTransactionGroupUpgrade       | classoid                                          | int         | int            | NO            |             |
| sysTransactionGroupUpgrade       | conflictCount                                     | int         | int            | NO            |             |
| sysTransactionGroupUpgrade       | status                                            | varchar     | varchar(255)   | NO            |             |
| sysTransactionGroupUpgrade       | unresolvedConflictCount                           | int         | int            | NO            |             |
| sysUIProfiling                   | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysUIProfiling                   | fromPage_id                                       | int         | int            | NO            | Foreign Key |
| sysUIProfiling                   | serverStartTime                                   | datetime    | datetime       | NO            | Foreign Key |
| sysUIProfiling                   | session_id                                        | int         | int            | NO            | Foreign Key |
| sysUIProfiling                   | toPage_id                                         | int         | int            | NO            | Foreign Key |
| sysUIProfiling                   | classoid                                          | int         | int            | NO            |             |
| sysUIProfiling                   | fromWidget_id                                     | int         | int            | NO            |             |
| sysUIProfiling                   | operation_id                                      | int         | int            | NO            |             |
| sysUIProfiling                   | parameters                                        | text        | text           | NO            |             |
| sysUIProfiling                   | queryDuplicateCount                               | int         | int            | NO            |             |
| sysUIProfiling                   | queryReadCount                                    | int         | int            | NO            |             |
| sysUIProfiling                   | queryWriteCount                                   | int         | int            | NO            |             |
| sysUIProfiling                   | serverExecutionTime                               | int         | int            | NO            |             |
| sysUIProfiling                   | toWidget_id                                       | int         | int            | NO            |             |
| sysUserAgent                     | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysUserAgent                     | classoid                                          | int         | int            | NO            |             |
| sysUserAgent                     | name                                              | varchar     | varchar(255)   | NO            |             |
| sysUserPermission                | oid                                               | int         | int            | NO            | Primary Key |
| sysUserPermission                | classoid                                          | int         | int            | NO            |             |
| sysUserPermission                | object_id                                         | int         | int            | NO            |             |
| sysUserPermission                | permission_id                                     | int         | int            | NO            |             |
| sysUserPermission                | user_id                                           | int         | int            | NO            |             |
| sysUserRole                      | oid                                               | int         | int            | NO            | Primary Key |
| sysUserRole                      | user_id                                           | int         | int            | NO            | Foreign Key |
| sysUserRole                      | classoid                                          | int         | int            | NO            |             |
| sysUserRole                      | role_id                                           | int         | int            | NO            |             |
| sysUserSession                   | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysUserSession                   | credentials_id                                    | int         | int            | NO            | Foreign Key |
| sysUserSession                   | sessionKey                                        | varchar     | varchar(255)   | NO            | Foreign Key |
| sysUserSession                   | sessionStart                                      | datetime    | datetime       | NO            | Foreign Key |
| sysUserSession                   | assumedIdentity_id                                | int         | int            | NO            |             |
| sysUserSession                   | classoid                                          | int         | int            | NO            |             |
| sysUserSession                   | device_id                                         | int         | int            | NO            |             |
| sysUserSession                   | endpoint_id                                       | int         | int            | NO            |             |
| sysUserSession                   | language                                          | varchar     | varchar(255)   | NO            |             |
| sysUserSession                   | lastActivity                                      | datetime    | datetime       | NO            |             |
| sysUserSession                   | lastServer                                        | varchar     | varchar(255)   | NO            |             |
| sysUserSession                   | network_id                                        | int         | int            | NO            |             |
| sysUserSession                   | parameters                                        | text        | text           | NO            |             |
| sysUserSession                   | sessionEnd                                        | datetime    | datetime       | NO            |             |
| sysUserSession                   | source                                            | varchar     | varchar(255)   | NO            |             |
| sysUserSession                   | status                                            | varchar     | varchar(255)   | NO            |             |
| sysUserSession                   | system_id                                         | int         | int            | NO            |             |
| sysUserSession                   | type_id                                           | int         | int            | NO            |             |
| sysUserSession                   | userAgent_id                                      | int         | int            | NO            |             |
| sysUserSession                   | userEndpoint_id                                   | int         | int            | NO            |             |
| sysUserSession                   | username                                          | varchar     | varchar(255)   | NO            |             |
| sysUserTransaction               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysUserTransaction               | session_id                                        | int         | int            | NO            | Foreign Key |
| sysUserTransaction               | classoid                                          | int         | int            | NO            |             |
| sysUserTransaction               | timestamp                                         | datetime    | datetime       | NO            |             |
| sysUserTransaction               | transactionId                                     | char        | char(36)       | NO            |             |
| sysUserTransaction               | user_id                                           | int         | int            | NO            |             |
| sysUserTransactionGroup          | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysUserTransactionGroup          | transactionGroup_id                               | int         | int            | NO            | Foreign Key |
| sysUserTransactionGroup          | classoid                                          | int         | int            | NO            |             |
| sysUserTransactionGroup          | closedDate                                        | datetime    | datetime       | NO            |             |
| sysUserTransactionGroup          | openedDate                                        | datetime    | datetime       | NO            |             |
| sysUserTransactionGroup          | status                                            | varchar     | varchar(255)   | NO            |             |
| sysUserTransactionGroup          | user_id                                           | int         | int            | NO            |             |
| sysUserTransactionGroup          | userSession_id                                    | int         | int            | NO            |             |
| sysWorkflowSession               | oid                                               | bigint      | bigint         | NO            | Primary Key |
| sysWorkflowSession               | sessionKey                                        | varchar     | varchar(255)   | NO            | Foreign Key |
| sysWorkflowSession               | classoid                                          | int         | int            | NO            |             |
| sysWorkflowSession               | data                                              | mediumtext  | mediumtext     | NO            |             |
| sysWorkflowSession               | lastActivity                                      | datetime    | datetime       | NO            |             |
| sysWorkflowSession               | lastProfiling_id                                  | int         | int            | NO            |             |
| sysWorkflowSession               | lastRequestId                                     | varchar     | varchar(255)   | NO            |             |
| sysWorkflowSession               | process_id                                        | int         | int            | NO            |             |
| sysWorkflowSession               | state_id                                          | int         | int            | NO            |             |
| sysWorkflowSession               | status                                            | varchar     | varchar(255)   | NO            |             |
| sysWorkflowSession               | userSession_id                                    | int         | int            | NO            |             |
| testObject                       | oid                                               | bigint      | bigint         | NO            | Primary Key |
| testObject                       | name                                              | varchar     | varchar(255)   | NO            | Foreign Key |
| testObject                       | parent_id                                         | int         | int            | NO            | Foreign Key |
| testObject                       | classoid                                          | int         | int            | NO            |             |
| testObject                       | sequence                                          | int         | int            | NO            |             |
| testObject                       | testBigDecimal                                    | decimal     | decimal(19,2)  | NO            |             |
| testObject                       | testBoolean                                       | varchar     | varchar(10)    | NO            |             |
| testObject                       | testDate                                          | datetime    | datetime       | NO            |             |
| testObject                       | testInteger                                       | int         | int            | NO            |             |
| testObject                       | testLocalizedString_id                            | int         | int            | NO            |             |
| testObject                       | testString                                        | varchar     | varchar(255)   | NO            |             |
| testObject                       | testStringEnum                                    | varchar     | varchar(255)   | NO            |             |
| testObject                       | testText                                          | text        | text           | NO            |             |
| testObject                       | testTotalValue                                    | decimal     | decimal(19,2)  | NO            |             |
| testObject                       | testUUID                                          | char        | char(36)       | NO            |             |
| testObject                       | testValue                                         | decimal     | decimal(19,2)  | NO            |             |
| users                            | oid                                               | int         | int            | NO            | Primary Key |
| users                            | userName                                          | varchar     | varchar(255)   | NO            | Foreign Key |
| users                            | classoid                                          | int         | int            | NO            |             |
| users                            | firstName                                         | varchar     | varchar(255)   | NO            |             |
| users                            | language_id                                       | int         | int            | NO            |             |
| users                            | lastName                                          | varchar     | varchar(255)   | NO            |             |
| users                            | locale                                            | varchar     | varchar(255)   | NO            |             |
| users                            | status                                            | varchar     | varchar(255)   | NO            |             |
| users                            | timeZone                                          | varchar     | varchar(255)   | NO            |             |
| users                            | type_id                                           | int         | int            | NO            |             |
| users                            | userGroup_id                                      | int         | int            | NO            |             |

---

## 7. Summary of Top Tables Structure

Shows a summary of column types and keys for each large table

### Query:
```sql
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
```

### Results:
| TABLE_NAME              |   total_columns |   primary_keys |   foreign_keys |   nullable_columns | data_types                            |
|:------------------------|----------------:|---------------:|---------------:|-------------------:|:--------------------------------------|
| scMaterial              |              64 |              1 |             18 |                  0 | bigint,datetime,decimal,int,varchar   |
| scMovement              |              48 |              1 |             20 |                  0 | bigint,datetime,decimal,int,varchar   |
| sysProcessProfiling     |              33 |              1 |              4 |                  0 | bigint,datetime,int,text,varchar      |
| scMIAdjustment          |              26 |              1 |              6 |                  0 | bigint,datetime,decimal,int,varchar   |
| scLineAdjustment        |              22 |              1 |              3 |                  0 | bigint,int,varchar                    |
| scOrderAdjustment       |              19 |              1 |              2 |                  0 | bigint,datetime,int,varchar           |
| scGeneratedMREQ         |              18 |              1 |              3 |                  0 | bigint,decimal,int,mediumtext,varchar |
| sysEvent                |              12 |              1 |              2 |                  0 | bigint,datetime,int,text,varchar      |
| scMIAdjustmentDimension |               9 |              1 |              2 |                  0 | bigint,decimal,int                    |
| oidToTable              |               3 |              1 |              2 |                  0 | int                                   |

---

