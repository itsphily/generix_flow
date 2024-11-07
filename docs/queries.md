# Database Analysis and Structure

Analysis performed on: 2024-11-06 16:36:43


## 0. Available Tables

Lists all tables in the database with their actual names


---


## 1. Database Size and Table Count

Overview of database size, total tables, and tables with data

The database 'agropur_prod' has a total size of 247.37 GB and contains 777 tables, of which 516.0 contain data.

---


## 2. Top 10 Largest Tables

Identifies the largest tables by data size

The largest tables in the database are:

- scGeneratedMREQ: 72.73 GB data, 2.78 GB indexes, containing 16668583 rows
- scMovement: 13.51 GB data, 31.43 GB indexes, containing 55454691 rows
- scMIAdjustment: 11.74 GB data, 10.39 GB indexes, containing 76114843 rows
- sysImportedItem: 16.73 GB data, 0.28 GB indexes, containing 2720933 rows
- sysProcessProfiling: 8.56 GB data, 6.19 GB indexes, containing 44153523 rows
- sysInterfaceArchive: 12.62 GB data, 0.01 GB indexes, containing 660867 rows
- scLineAdjustment: 6.27 GB data, 2.78 GB indexes, containing 36046571 rows
- scMaterial: 3.57 GB data, 4.09 GB indexes, containing 9633411 rows
- scMIAdjustmentDimension: 4.37 GB data, 3.21 GB indexes, containing 64015150 rows
- scPKLI: 2.05 GB data, 3.4 GB indexes, containing 7004251 rows

---


## 3. Tables with Most Records

Shows tables with the highest number of rows

Tables with the highest number of records:

- scMIAdjustment: 76114843 rows (11.74 GB)
- scMIAdjustmentDimension: 64015150 rows (4.37 GB)
- scMovement: 55454691 rows (13.51 GB)
- oidToTable: 48054858 rows (1.47 GB)
- sysProcessProfiling: 44153523 rows (8.56 GB)
- scLineAdjustment: 36046571 rows (6.27 GB)
- sysEvent: 20021938 rows (1.67 GB)
- scGeneratedMREQ: 16668583 rows (72.73 GB)
- scOrderAdjustment: 13272123 rows (1.59 GB)
- scMaterial: 9633411 rows (3.57 GB)

---


## 4. Recent Database Activity

Shows tables with recent updates

Recent table updates:

- users was updated at 2024-11-02 12:38:07, contains 654 rows (0.0 GB)
- sysWorkflowSession was updated at 2024-11-02 12:38:06, contains 36 rows (0.0 GB)
- testObject was updated at 2024-11-02 12:38:06, contains 12 rows (0.0 GB)
- sysWIFIAccessPoint was updated at 2024-11-02 12:38:06, contains 0 rows (0.0 GB)
- sysUserSession was updated at 2024-11-02 12:38:06, contains 226223 rows (0.04 GB)
- sysUserTransaction was updated at 2024-11-02 12:38:06, contains 1101 rows (0.0 GB)
- sysUserRole was updated at 2024-11-02 12:37:44, contains 856 rows (0.0 GB)
- sysUserPermission was updated at 2024-11-02 12:37:44, contains 2895 rows (0.0 GB)
- sysUserAgent was updated at 2024-11-02 12:37:43, contains 649 rows (0.0 GB)
- sysUIProfiling was updated at 2024-11-02 12:37:43, contains 5455454 rows (1.17 GB)

---


## 5. Table Engine Distribution

Shows distribution of storage engines used in the database

Storage engine distribution:

- InnoDB: 777 tables, total size 247.37 GB

---


## 6. Column Details for All Active Tables

Lists all columns and their data types for all tables containing data

Table structure details:


### billGLAccount
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- code: varchar(255) - not nullable
- description: text - not nullable

### event
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable (Foreign Key)
- eventCode: varchar(255) - not nullable (Foreign Key)
- mioid: int - not nullable (Foreign Key)
- refoid: int - not nullable (Foreign Key)
- siteoid: int - not nullable (Foreign Key)
- tooid: int - not nullable (Foreign Key)
- adjustedQty: bigint - not nullable
- comments: text - not nullable
- definition_id: int - not nullable
- eventDate: datetime - not nullable
- eventType: varchar(255) - not nullable
- fromoid: int - not nullable
- location: varchar(255) - not nullable
- qty: bigint - not nullable
- stamp: datetime - not nullable
- useroid: int - not nullable

### ints
- i: int - not nullable (Primary Key)

### objectid
- entityName: varchar(255) - not nullable (Foreign Key)
- next: int - not nullable
- range_start: int - not nullable
- range_stop: int - not nullable

### oidToTable
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable (Foreign Key)
- table_id: int - not nullable (Foreign Key)

### scABCClass
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable
- site_id: int - not nullable

### scABCConfiguration
- oid: int - not nullable (Primary Key)
- abcClass_id: int - not nullable
- classoid: int - not nullable
- countingJob_id: int - not nullable
- frequency: int - not nullable
- generationMode: varchar(255) - not nullable
- owner_id: int - not nullable
- priority: varchar(255) - not nullable
- route_id: int - not nullable
- schedule_id: int - not nullable
- site_id: int - not nullable

### scAddress
- oid: bigint - not nullable (Primary Key)
- address1: varchar(255) - not nullable
- address2: varchar(255) - not nullable
- address3: varchar(255) - not nullable
- address4: varchar(255) - not nullable
- addresstype: varchar(255) - not nullable
- city: varchar(255) - not nullable
- classoid: int - not nullable
- country: varchar(255) - not nullable
- country_id: int - not nullable
- latitude: varchar(255) - not nullable
- longitude: varchar(255) - not nullable
- postalCode: varchar(255) - not nullable
- province: varchar(255) - not nullable
- site_id: int - not nullable
- stateProvince_id: int - not nullable

### scAgropurContainerSSCC
- oid: bigint - not nullable (Primary Key)
- container_id: int - not nullable (Foreign Key)
- deliveryNo: varchar(255) - not nullable (Foreign Key)
- pklh_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- creationDate: datetime - not nullable
- generatedSSCC_id: int - not nullable
- gs1LabelFormat: varchar(255) - not nullable
- inactiveDate: datetime - not nullable
- materialmaster_id: int - not nullable
- mmdimension_id: int - not nullable
- sequence: int - not nullable
- sscc: varchar(255) - not nullable

### scAgropurHandlingMaterialLoad
- oid: bigint - not nullable (Primary Key)
- load_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable

### scAgropurSSCC
- oid: bigint - not nullable (Primary Key)
- companyPrefix: varchar(255) - not nullable (Foreign Key)
- organization: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- inactiveDate: datetime - not nullable
- serial: int - not nullable
- status: varchar(255) - not nullable

### scAisle
- oid: int - not nullable (Primary Key)
- allocateInventory: varchar(10) - not nullable
- classoid: int - not nullable
- name: varchar(255) - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable
- velocity: varchar(255) - not nullable

### scAllocateInvPolicy
- oid: int - not nullable (Primary Key)
- allocationUOIMode: varchar(255) - not nullable
- backorderMode: varchar(255) - not nullable
- bopolicy_id: int - not nullable
- boReservMode: varchar(255) - not nullable
- bozone_id: int - not nullable
- classoid: int - not nullable
- description: text - not nullable
- expiryValidationDate: varchar(255) - not nullable
- forwardpick_id: int - not nullable
- inventoryPriority: varchar(255) - not nullable
- mergePKLI: varchar(255) - not nullable
- name: varchar(255) - not nullable
- pklilocsetting: varchar(255) - not nullable
- priority: int - not nullable
- priorizationMode: varchar(255) - not nullable
- replenishableZone_id: int - not nullable
- reservationMode: varchar(255) - not nullable
- site_id: int - not nullable
- siteConfiguration_id: int - not nullable
- unallocationMode: varchar(255) - not nullable

### scAllocationJob
- oid: int - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- showAllocationPlan: varchar(10) - not nullable
- siteConfiguration_id: int - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable

### scAllocationJobFillrate
- oid: bigint - not nullable (Primary Key)
- allocationJob_id: int - not nullable
- classoid: int - not nullable
- fillrateType_id: int - not nullable
- sequence: int - not nullable

### scAssembly
- oid: int - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- name: varchar(255) - not nullable
- status: varchar(255) - not nullable
- uoi_id: int - not nullable

### scBayConfiguration
- oid: int - not nullable (Primary Key)
- bay_id: int - not nullable
- classoid: int - not nullable
- printingWorkCenter_id: int - not nullable
- receivingJob_id: int - not nullable

### scCalendarPeriod_Agropur
- oid: bigint - not nullable (Primary Key)
- calendar_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- endDate: datetime - not nullable
- name: varchar(255) - not nullable
- startDate: datetime - not nullable
- type: varchar(255) - not nullable

### scCarrierRelation
- oid: int - not nullable (Primary Key)
- customer_id: int - not nullable (Foreign Key)
- bolreport_id: int - not nullable
- carrier_id: int - not nullable
- carrierAccountNo: varchar(255) - not nullable
- classoid: int - not nullable
- masterBOLreport_id: int - not nullable
- serviceLevel_id: int - not nullable
- shipmentType_id: int - not nullable

### scCheckListInstanceComment
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- comment: text - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- owner_id: int - not nullable
- ownerType: varchar(255) - not nullable
- publicComment: varchar(10) - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable

### scChecklistDataType
- oid: int - not nullable (Primary Key)
- checklistType_id: int - not nullable
- classoid: int - not nullable
- column_id: int - not nullable
- name: varchar(255) - not nullable
- query_id: int - not nullable
- scriptText: text - not nullable
- type_id: int - not nullable
- valueList_id: int - not nullable

### scChecklistInstance
- oid: bigint - not nullable (Primary Key)
- checklistMaster_id: int - not nullable (Foreign Key)
- reference_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- locked: varchar(10) - not nullable
- materialMaster_id: int - not nullable
- owner_id: int - not nullable
- referenceName: varchar(255) - not nullable
- referenceNo: varchar(255) - not nullable
- revision_id: int - not nullable
- site_id: int - not nullable
- source: varchar(255) - not nullable
- status: varchar(255) - not nullable
- unlockStamp: datetime - not nullable
- unlockUser_id: int - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable

### scChecklistInstanceSourceDetail
- oid: bigint - not nullable (Primary Key)
- checklistInstance_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- customer_id: int - not nullable
- dimension_id: int - not nullable
- materialMaster_id: int - not nullable
- source: varchar(255) - not nullable
- vendor_id: int - not nullable

### scChecklistInstanceStep
- oid: bigint - not nullable (Primary Key)
- checklistInstance_id: int - not nullable (Foreign Key)
- stepMaster_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- lastResult_id: int - not nullable
- sequence: int - not nullable
- status: varchar(255) - not nullable

### scChecklistMaster
- oid: int - not nullable (Primary Key)
- activeRevision_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- origin_id: int - not nullable
- referenceNo: varchar(255) - not nullable
- revision: varchar(255) - not nullable
- status: varchar(255) - not nullable
- type_id: int - not nullable

### scChecklistMasterAction
- oid: int - not nullable (Primary Key)
- step_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- instanceStatus: varchar(255) - not nullable
- label_id: int - not nullable
- referenceNo: varchar(255) - not nullable

### scChecklistMasterRevision
- oid: int - not nullable (Primary Key)
- checklistMaster_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- origin_id: int - not nullable
- revision: varchar(255) - not nullable
- status: varchar(255) - not nullable

### scChecklistMasterStep
- oid: int - not nullable (Primary Key)
- billingEventType_id: int - not nullable
- checklistMaster_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- expectedResult: varchar(255) - not nullable
- label_id: int - not nullable
- origin_id: int - not nullable
- referenceNo: varchar(255) - not nullable
- required: varchar(10) - not nullable
- resultType_id: int - not nullable
- sequence: int - not nullable
- status: varchar(255) - not nullable

### scChecklistStepResult
- oid: bigint - not nullable (Primary Key)
- reference_id: int - not nullable (Foreign Key)
- step_id: int - not nullable (Foreign Key)
- action_id: int - not nullable
- classoid: int - not nullable
- comment: text - not nullable
- completedDate: datetime - not nullable
- result: varchar(255) - not nullable
- status: varchar(255) - not nullable
- user_id: int - not nullable

### scChecklistType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- mode: varchar(255) - not nullable
- name: varchar(255) - not nullable
- referenceType_id: int - not nullable
- type: varchar(255) - not nullable

### scComment
- oid: bigint - not nullable (Primary Key)
- reference_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- comment: text - not nullable
- timestamp: datetime - not nullable
- type: varchar(255) - not nullable
- user_id: int - not nullable

### scConfigurationItem
- oid: int - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- enforcePosition: varchar(10) - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- quantity: int - not nullable
- sequence: int - not nullable
- status: varchar(255) - not nullable
- subAssembly_id: int - not nullable
- uoi_id: int - not nullable

### scConsolidationJob
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- containerConsolidationMode: varchar(255) - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- site_id: int - not nullable
- siteConfiguration_id: int - not nullable
- status: varchar(255) - not nullable

### scContainer
- oid: int - not nullable (Primary Key)
- container_id: int - not nullable (Foreign Key)
- currentLOAD_id: int - not nullable (Foreign Key)
- currentPKLH_id: int - not nullable (Foreign Key)
- location_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- serialNo: varchar(255) - not nullable (Foreign Key)
- sSCC: varchar(255) - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- topContainer_id: int - not nullable (Foreign Key)
- trackingNo: varchar(255) - not nullable (Foreign Key)
- type_id: int - not nullable (Foreign Key)
- capacity: decimal(19,2) - not nullable
- capacityUsed: decimal(19,2) - not nullable
- classoid: int - not nullable
- containerSequence: varchar(255) - not nullable
- currentMOVE_id: int - not nullable
- currentSHLP_id: int - not nullable
- currentSOLH_id: int - not nullable
- depth: decimal(19,2) - not nullable
- dimensionUOM_id: int - not nullable
- height: decimal(19,2) - not nullable
- items: int - not nullable
- loadSequence: int - not nullable
- manualWeight: varchar(10) - not nullable
- maxWeight: decimal(19,2) - not nullable
- mobileEquipment_id: int - not nullable
- partitionNo: int - not nullable
- physicalSequence: int - not nullable
- pickCOPosition: varchar(255) - not nullable
- pickedSequence: int - not nullable
- pickingContainer_id: int - not nullable
- shipmentRequest_id: int - not nullable
- shippingLabelPrinted: varchar(10) - not nullable
- shipTo_id: int - not nullable
- shipToZone_id: int - not nullable
- site_id: int - not nullable
- supplier_id: int - not nullable
- tmsInfo_id: int - not nullable
- totalValue: decimal(19,2) - not nullable
- transportEquipment_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable
- width: decimal(19,2) - not nullable
- zone_id: int - not nullable

### scCountingJob
- oid: int - not nullable (Primary Key)
- allowRecountUniqueItemInSameSession: varchar(10) - not nullable
- allowSameCounter: varchar(255) - not nullable
- classoid: int - not nullable
- countAllLPOneCount: varchar(10) - not nullable
- countAllLPOneCountMode: varchar(255) - not nullable
- countMethod: varchar(255) - not nullable
- countMode: varchar(255) - not nullable
- countTolerance: varchar(255) - not nullable
- description: text - not nullable
- displayItemInfoOnBatchLPNCount: varchar(10) - not nullable
- inconsistentJob_id: int - not nullable
- inconsistentStrategy: varchar(255) - not nullable
- maxConsecutiveCount: varchar(255) - not nullable
- maxConsecutiveCountBatch: int - not nullable
- name: varchar(255) - not nullable
- newItemCondition_id: int - not nullable
- newItemOwner_id: int - not nullable
- reason_id: int - not nullable
- recoundNewItem: varchar(10) - not nullable
- recountNotCounted: varchar(10) - not nullable
- sendToReconcile: varchar(10) - not nullable
- serialNumberDiscrepancyAllowed: varchar(10) - not nullable
- site_id: int - not nullable
- siteConfiguration_id: int - not nullable

### scCustomerRelation
- oid: int - not nullable (Primary Key)
- customer_id: int - not nullable (Foreign Key)
- supplier_id: int - not nullable (Foreign Key)
- allocationInvPolicy_id: int - not nullable
- billingCustomer_id: int - not nullable
- billingLocation_id: int - not nullable
- billTo_id: int - not nullable
- billToAddress_id: int - not nullable
- billToContact_id: int - not nullable
- blocked: varchar(255) - not nullable
- checklistInbound: int - not nullable
- checklistInboundByItem: int - not nullable
- checklistInboundByLOTNO: int - not nullable
- checklistInboundByReceivingDocument: int - not nullable
- classoid: int - not nullable
- customerNo: varchar(255) - not nullable
- defaultSOLIPriority: varchar(255) - not nullable
- packingSlip_id: int - not nullable
- productionReceivingLabel_id: int - not nullable
- productionReceivingLabelQty: int - not nullable
- shipTo_id: int - not nullable
- shipToAddress_id: int - not nullable
- shipToContact_id: int - not nullable
- shipVia_id: int - not nullable
- shipViaAddress_id: int - not nullable
- shipViaContact_id: int - not nullable

### scCycleCount
- oid: int - not nullable (Primary Key)
- calendar_id: int - not nullable
- classoid: int - not nullable
- countedItems: int - not nullable
- countingJob_id: int - not nullable
- countingMode: varchar(255) - not nullable
- currentCycle: int - not nullable
- currentLocation_id: int - not nullable
- endLocation_id: int - not nullable
- frequency: int - not nullable
- locationType: varchar(255) - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- priority: varchar(255) - not nullable
- remainingDays: int - not nullable
- route_id: int - not nullable
- schedule_id: int - not nullable
- scheduledItems: int - not nullable
- site_id: int - not nullable
- startLocation_id: int - not nullable
- status: varchar(255) - not nullable
- totalDays: int - not nullable
- totalItems: int - not nullable

### scDeliveryJob
- oid: int - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- siteConfiguration_id: int - not nullable
- status: varchar(255) - not nullable

### scExpiryDateJobLog
- oid: bigint - not nullable (Primary Key)
- expiryDateJob_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description: varchar(255) - not nullable
- endDate: datetime - not nullable
- startDate: datetime - not nullable
- user_id: int - not nullable

### scFillrateType
- oid: int - not nullable (Primary Key)
- baseType: varchar(255) - not nullable
- classoid: int - not nullable
- description: varchar(255) - not nullable
- name: varchar(255) - not nullable

### scGTIN
- oid: int - not nullable (Primary Key)
- gtin: varchar(255) - not nullable (Foreign Key)
- uoiconfig_id: int - not nullable (Foreign Key)
- classoid: int - not nullable

### scGeneratedItem
- oid: bigint - not nullable (Primary Key)
- generation_id: int - not nullable (Foreign Key)
- allocatedQty: bigint - not nullable
- availableQty: bigint - not nullable
- classoid: int - not nullable
- materialMaster_id: int - not nullable
- partitionNo: int - not nullable
- requestedQty: bigint - not nullable
- totalQty: bigint - not nullable
- uoi_id: int - not nullable

### scGeneratedMREQ
- oid: bigint - not nullable (Primary Key)
- generatedOrder_id: int - not nullable (Foreign Key)
- item_id: int - not nullable (Foreign Key)
- mreq_id: int - not nullable (Foreign Key)
- allocatedQty: bigint - not nullable
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- fillrateType_id: int - not nullable
- fulfilledValue: decimal(19,2) - not nullable
- locations: mediumtext - not nullable
- partitionNo: int - not nullable
- policy_id: int - not nullable
- reason: varchar(255) - not nullable
- requiredQty: bigint - not nullable
- sequence: int - not nullable
- status: varchar(255) - not nullable
- totalValue: decimal(19,2) - not nullable
- uoi_id: int - not nullable

### scGeneratedOrder
- oid: bigint - not nullable (Primary Key)
- generation_id: int - not nullable (Foreign Key)
- shipmentRequest_id: int - not nullable (Foreign Key)
- solh_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- fillrateType_id: int - not nullable
- fulfilledValue: decimal(19,2) - not nullable
- partitionNo: int - not nullable
- reason: varchar(255) - not nullable
- status: varchar(255) - not nullable
- totalValue: decimal(19,2) - not nullable

### scGeneration
- oid: int - not nullable (Primary Key)
- generationTime: datetime - not nullable (Foreign Key)
- allocatedLines: int - not nullable
- allocationJob_id: int - not nullable
- assemblyMode: varchar(255) - not nullable
- cancelledLines: int - not nullable
- classoid: int - not nullable
- completedTime: datetime - not nullable
- executionTime: int - not nullable
- ignoredLines: int - not nullable
- message: text - not nullable
- name: varchar(255) - not nullable
- partiallyAllocatedLines: int - not nullable
- partitionNo: int - not nullable
- policy_id: int - not nullable
- preposition_id: int - not nullable
- prepositionZone_id: int - not nullable
- requestedTime: datetime - not nullable
- simulation: varchar(10) - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable
- totalItems: int - not nullable
- totalLines: int - not nullable
- type: varchar(255) - not nullable
- user_id: int - not nullable
- wave_id: int - not nullable

### scHandlingMaterialOrderContainer
- oid: bigint - not nullable (Primary Key)
- container_id: int - not nullable (Foreign Key)
- solh_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- handlingMaterial_id: int - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable

### scInternalRoute
- oid: int - not nullable (Primary Key)
- aislepattern: varchar(255) - not nullable
- classoid: int - not nullable
- description: varchar(255) - not nullable
- levelpattern: varchar(255) - not nullable
- name: varchar(255) - not nullable
- rackpattern: varchar(255) - not nullable
- siteoid: int - not nullable
- zoneoid: int - not nullable

### scInvAdjustmentReason
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- condition_id: int - not nullable
- costcenter_id: int - not nullable
- description_id: int - not nullable
- glAccount_id: int - not nullable
- hostValue: varchar(255) - not nullable
- label_id: int - not nullable
- name: varchar(255) - not nullable

### scInventoryCountSession
- oid: bigint - not nullable (Primary Key)
- abcClass_id: int - not nullable
- activeCount: int - not nullable
- aisle_id: int - not nullable
- cancelledCount: int - not nullable
- classoid: int - not nullable
- comment: text - not nullable
- completedCount: int - not nullable
- completedDate: datetime - not nullable
- countingJob_id: int - not nullable
- countingMode: varchar(255) - not nullable
- creationDate: datetime - not nullable
- cycleCount_id: int - not nullable
- location_id: int - not nullable
- locationItemCount_id: int - not nullable
- locationType: varchar(255) - not nullable
- materialMaster_id: int - not nullable
- name: varchar(255) - not nullable
- owner_id: int - not nullable
- pkli_id: int - not nullable
- priority: int - not nullable
- productClass_id: int - not nullable
- requiredDate: datetime - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable
- totalCount: int - not nullable
- type: varchar(255) - not nullable
- user_id: int - not nullable
- zone_id: int - not nullable

### scInventoryLocation
- oid: int - not nullable (Primary Key)
- aisle_id: int - not nullable (Foreign Key)
- level_id: int - not nullable (Foreign Key)
- materialAssignment: varchar(255) - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- rack_id: int - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- type_id: int - not nullable (Foreign Key)
- zone_id: int - not nullable (Foreign Key)
- allocateInventory: varchar(10) - not nullable
- checkDigit: varchar(255) - not nullable
- classoid: int - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- enableAgingReport: varchar(10) - not nullable
- lastLocation_id: int - not nullable
- lastMovement_id: int - not nullable
- lightId: varchar(255) - not nullable
- nbLPInTheLocation: int - not nullable
- nextLocation_id: int - not nullable
- position: varchar(255) - not nullable
- sequence: int - not nullable
- TrackingMode: varchar(255) - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable
- user_id: int - not nullable
- velocity: varchar(255) - not nullable

### scInventoryLocationType
- oid: int - not nullable (Primary Key)
- type: varchar(255) - not nullable (Foreign Key)
- agropurRestrictStagingBay: varchar(10) - not nullable
- agropurStagingBay: varchar(10) - not nullable
- askReasonCode: varchar(10) - not nullable
- assignmentType: varchar(255) - not nullable
- baseMaxVolume: decimal(19,2) - not nullable
- baseMaxWeight: decimal(19,2) - not nullable
- capacity: varchar(255) - not nullable
- classoid: int - not nullable
- description: text - not nullable
- dimensionUOM_id: int - not nullable
- dropAction: varchar(255) - not nullable
- dropBay: varchar(10) - not nullable
- exteriorDepth: decimal(19,2) - not nullable
- exteriorHeight: decimal(19,2) - not nullable
- exteriorWidth: decimal(19,2) - not nullable
- forwardPickBay: varchar(10) - not nullable
- interiorDepth: decimal(19,2) - not nullable
- interiorHeight: decimal(19,2) - not nullable
- interiorWidth: decimal(19,2) - not nullable
- maxNumberOfLP: int - not nullable
- maxVolume: decimal(19,2) - not nullable
- maxWeight: decimal(19,2) - not nullable
- name: varchar(255) - not nullable
- period: decimal(19,2) - not nullable
- productionBay: varchar(10) - not nullable
- qaBay: varchar(10) - not nullable
- receivingBay: varchar(10) - not nullable
- shippingBay: varchar(10) - not nullable
- stagingBay: varchar(10) - not nullable
- status: varchar(255) - not nullable
- weightUOM_id: int - not nullable

### scInventorySnapshot
- oid: bigint - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- session_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- condition_id: int - not nullable
- consumedQty: bigint - not nullable
- costCenter_id: int - not nullable
- location_id: int - not nullable
- lotNo_id: int - not nullable
- outputtedQty: bigint - not nullable
- owner_id: int - not nullable
- pickedQty: bigint - not nullable
- processedQty: bigint - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- sequenceLevel: varchar(255) - not nullable
- serialNo_id: int - not nullable
- snapshotLevel: varchar(255) - not nullable
- uoi_id: int - not nullable
- zone_id: int - not nullable

### scJobConstraint
- oid: bigint - not nullable (Primary Key)
- job_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- maxValue: decimal(19,2) - not nullable
- sequence: int - not nullable
- type: varchar(255) - not nullable

### scJobDestination
- oid: int - not nullable (Primary Key)
- job_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- location_id: int - not nullable
- site_id: int - not nullable
- type: varchar(255) - not nullable
- zone_id: int - not nullable

### scJobSplitter
- oid: bigint - not nullable (Primary Key)
- job_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- sequence: int - not nullable
- type: varchar(255) - not nullable

### scJobZone
- oid: int - not nullable (Primary Key)
- job_id: int - not nullable (Foreign Key)
- allocationMode: varchar(255) - not nullable
- breakUOI: varchar(255) - not nullable
- classoid: int - not nullable
- disableFutureReplenishments: varchar(10) - not nullable
- forceAllocateConfiguredUOI: varchar(10) - not nullable
- forwardPick_id: int - not nullable
- locationPriorizationMode: varchar(255) - not nullable
- maxPickPercentage: varchar(255) - not nullable
- minReplenishmentPercentage: varchar(255) - not nullable
- name: varchar(255) - not nullable
- overCapacityMode: varchar(255) - not nullable
- pickPredecessor_id: int - not nullable
- priority: int - not nullable
- replenishmentJob_id: int - not nullable
- replenishmentMode: varchar(255) - not nullable
- route_id: int - not nullable
- validateCapacity: varchar(10) - not nullable
- zone_id: int - not nullable

### scLOAD
- oid: int - not nullable (Primary Key)
- location_id: int - not nullable (Foreign Key)
- plannedDoor_id: int - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- capacity: decimal(19,2) - not nullable
- capacityUsed: decimal(19,2) - not nullable
- classoid: int - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- deliveryDate: datetime - not nullable
- description: varchar(255) - not nullable
- dimensionUOM_id: int - not nullable
- displayOnTV: varchar(10) - not nullable
- equipment_id: int - not nullable
- isAgropur_Staged: varchar(10) - not nullable
- lifeCycle: varchar(255) - not nullable
- loadingJob_id: int - not nullable
- maxWeight: decimal(19,2) - not nullable
- plannedArrival: datetime - not nullable
- plannedDeparture: datetime - not nullable
- priority: varchar(255) - not nullable
- proBill: varchar(255) - not nullable
- queue_id: int - not nullable
- referenceNo: varchar(255) - not nullable
- requiredDate: datetime - not nullable
- route_id: int - not nullable
- routeName: varchar(255) - not nullable
- seal: varchar(255) - not nullable
- sendShipmentDetailToOracle: varchar(10) - not nullable
- shippedDate: datetime - not nullable
- type_id: int - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scLevel
- oid: int - not nullable (Primary Key)
- aisle_id: int - not nullable (Foreign Key)
- rack_id: int - not nullable (Foreign Key)
- allocateInventory: varchar(10) - not nullable
- classoid: int - not nullable
- lightId: varchar(255) - not nullable
- name: varchar(255) - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable
- velocity: varchar(255) - not nullable

### scLineAdjustment
- oid: bigint - not nullable (Primary Key)
- line_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- reference_id: int - not nullable (Foreign Key)
- allocatedQty: bigint - not nullable
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- consumedQty: bigint - not nullable
- loadedQty: bigint - not nullable
- outstandingQty: bigint - not nullable
- packedQty: bigint - not nullable
- partitionNo: int - not nullable
- pickedQty: bigint - not nullable
- prepositionQty: bigint - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- releasedQty: bigint - not nullable
- shippedQty: bigint - not nullable
- stagedQty: bigint - not nullable
- status: varchar(255) - not nullable
- toReceiveQty: bigint - not nullable
- uoi_id: int - not nullable

### scLoadType
- oid: int - not nullable (Primary Key)
- canBeLockedByChecklist: varchar(255) - not nullable
- capacity: decimal(19,2) - not nullable
- classoid: int - not nullable
- creationMode: varchar(255) - not nullable
- depth: decimal(19,2) - not nullable
- description: text - not nullable
- dimensionUOM_id: int - not nullable
- forceSealNoInput: varchar(255) - not nullable
- height: decimal(19,2) - not nullable
- inboundChecklist_id: int - not nullable
- initialStatus: varchar(255) - not nullable
- loadingSequenceOrderAlgorithm: varchar(255) - not nullable
- loadingSequenceOrderMode: varchar(255) - not nullable
- maxWeight: decimal(19,2) - not nullable
- name: varchar(255) - not nullable
- preLoadingChecklist_id: int - not nullable
- shipmentType_id: int - not nullable
- weightUOM_id: int - not nullable
- width: decimal(19,2) - not nullable

### scLoadingJob
- oid: int - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- allowContainerLoadingOnToLoadList: varchar(10) - not nullable
- allowMultipleItemLoading: varchar(10) - not nullable
- askEquipmentOperating: varchar(10) - not nullable
- canBeLockedByChecklist: varchar(255) - not nullable
- classoid: int - not nullable
- description: text - not nullable
- forceSealNoInput: varchar(255) - not nullable
- itemCapacityDefault: int - not nullable
- itemCapacityReachMode: varchar(255) - not nullable
- itemCapacityStartMoveNotReachMode: varchar(255) - not nullable
- itemVerificationThreshold: int - not nullable
- loadingSequenceOrderAlgorithm: varchar(255) - not nullable
- loadingSequenceOrderMode: varchar(255) - not nullable
- name: varchar(255) - not nullable
- preLoadingChecklist_id: int - not nullable
- restrictionMode: varchar(255) - not nullable
- shipmentRestriction: varchar(255) - not nullable
- showOnlyAssigned: varchar(10) - not nullable
- siteConfiguration_id: int - not nullable
- status: varchar(255) - not nullable

### scLocationRoute
- oid: bigint - not nullable (Primary Key)
- location_id: int - not nullable (Foreign Key)
- route_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- sequence: int - not nullable

### scMIAdjustment
- oid: bigint - not nullable (Primary Key)
- eventDate: datetime - not nullable (Foreign Key)
- location_id: int - not nullable (Foreign Key)
- material_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- movement_id: int - not nullable (Foreign Key)
- type: varchar(255) - not nullable (Foreign Key)
- adjustedQty: bigint - not nullable
- adjustedWeight: decimal(19,2) - not nullable
- classoid: int - not nullable
- condition_id: int - not nullable
- costCenter_id: int - not nullable
- externalOID: varchar(255) - not nullable
- owner_id: int - not nullable
- partitionNo: int - not nullable
- reason_id: int - not nullable
- reference_id: int - not nullable
- site_id: int - not nullable
- stampDate: datetime - not nullable
- status: varchar(255) - not nullable
- totalQty: bigint - not nullable
- totalWeight: decimal(19,2) - not nullable
- uoi_id: int - not nullable
- user_id: int - not nullable
- weightUOM_id: int - not nullable
- zone_id: int - not nullable

### scMIAdjustmentDimension
- oid: bigint - not nullable (Primary Key)
- adjustment_id: int - not nullable (Foreign Key)
- dimension_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- partitionNo: int - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scMICondition
- oid: int - not nullable (Primary Key)
- baseCondition: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- name: varchar(255) - not nullable

### scMIDimension
- oid: bigint - not nullable (Primary Key)
- dimension_id: int - not nullable (Foreign Key)
- material_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- dimensionUOM_id: int - not nullable
- partitionNo: int - not nullable
- quantity: bigint - not nullable
- soliDimension_id: int - not nullable
- status: varchar(255) - not nullable
- uoi_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable
- wosDimension_id: int - not nullable

### scMIHistory
- oid: bigint - not nullable (Primary Key)
- material_id: int - not nullable (Foreign Key)
- pkli_id: int - not nullable (Foreign Key)
- shli_id: int - not nullable (Foreign Key)
- wos_id: int - not nullable (Foreign Key)
- activeDate: datetime - not nullable
- classoid: int - not nullable
- inactiveDate: datetime - not nullable
- load_id: int - not nullable
- partitionNo: int - not nullable
- previous_id: int - not nullable
- rcli_id: int - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable

### scMMABCCycleCount
- oid: bigint - not nullable (Primary Key)
- cycleCount_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- cancelledLocations: int - not nullable
- classoid: int - not nullable
- countedLocations: int - not nullable
- createdCycle: int - not nullable
- createdDate: datetime - not nullable
- itemCount: int - not nullable
- lastCountedDate: datetime - not nullable
- lastCycle: int - not nullable
- lastSession_id: int - not nullable
- remainingCount: int - not nullable
- scheduledLocations: int - not nullable

### scMMCustAttribute
- oid: int - not nullable (Primary Key)
- relation_id: int - not nullable (Foreign Key)
- checklistInboundByItem: int - not nullable
- checklistInboundByLOTNO: int - not nullable
- classoid: int - not nullable
- customerName: varchar(255) - not nullable
- customerPartNo: varchar(255) - not nullable
- expiryDateTolerance: varchar(255) - not nullable
- expiryDateToleranceMode: varchar(255) - not nullable
- matmaster_id: int - not nullable
- maxqty: int - not nullable
- minqty: int - not nullable

### scMMDimension
- oid: int - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- value: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- country_id: int - not nullable
- expiryDate: datetime - not nullable
- lotNumber_id: int - not nullable
- manufacturer_id: int - not nullable
- productionDate: datetime - not nullable
- reference_id: int - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scMMDimensionLocation
- oid: bigint - not nullable (Primary Key)
- mmDimension_id: int - not nullable (Foreign Key)
- mmLocation_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- dimensionUOM_id: int - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scMMLocation
- oid: bigint - not nullable (Primary Key)
- location_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- abcClass_id: int - not nullable
- baseVolume: decimal(19,2) - not nullable
- baseWeight: decimal(19,2) - not nullable
- classoid: int - not nullable
- condition_id: int - not nullable
- dimensionUOM_id: int - not nullable
- displayPartNo: varchar(255) - not nullable
- maximumQty: bigint - not nullable
- owner_id: int - not nullable
- pickedQty: bigint - not nullable
- quantity: bigint - not nullable
- replenishmentQty: bigint - not nullable
- replenishThresholdQty: bigint - not nullable
- reservedMoveQty: bigint - not nullable
- reservedPickQty: bigint - not nullable
- site_id: int - not nullable
- uoi_id: int - not nullable
- uoiConfigLocation_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scMMLocationLog
- oid: bigint - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- condition_id: int - not nullable
- location_id: int - not nullable
- owner_id: int - not nullable
- pickedQty: varchar(10) - not nullable
- quantity: varchar(10) - not nullable
- replenishmentQty: varchar(10) - not nullable
- reservedMoveQty: varchar(10) - not nullable
- reservedPickQty: varchar(10) - not nullable
- timestamp: datetime - not nullable
- uoiConfigLocation: varchar(10) - not nullable

### scMMSiteAttributes
- oid: int - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- abcClass_id: int - not nullable
- allowMixAttributes: varchar(10) - not nullable
- allowMixExpiryDate: varchar(10) - not nullable
- allowMixItems: varchar(10) - not nullable
- allowMixLotNo: varchar(10) - not nullable
- allowMixMode: varchar(255) - not nullable
- allowMixOwners: varchar(10) - not nullable
- allowReserve: varchar(10) - not nullable
- catchWeightMode: varchar(255) - not nullable
- checklistInboundByItem: int - not nullable
- checklistInboundByLOTNO: int - not nullable
- classoid: int - not nullable
- conditionChangeReasonList_id: int - not nullable
- conditionReasonRequired: varchar(255) - not nullable
- confLocMovingRangeOverlapValidationMode: varchar(255) - not nullable
- consumptionTolerance: varchar(255) - not nullable
- consumptionToleranceMode: varchar(255) - not nullable
- cooReceiving: varchar(255) - not nullable
- cooTracking: varchar(255) - not nullable
- customerExpiryDateTolerance: varchar(255) - not nullable
- customerExpiryDateToleranceMode: varchar(255) - not nullable
- deliverySequence: int - not nullable
- description: varchar(255) - not nullable
- expiryDateDelay: int - not nullable
- expiryDateProduction: varchar(255) - not nullable
- expiryDateReceiving: varchar(255) - not nullable
- expiryDateTracking: varchar(255) - not nullable
- externalBarcodeTracking: varchar(10) - not nullable
- gs1LabelFormat: varchar(255) - not nullable
- handlingMaterialQtyAutomaticAdjustReason_id: int - not nullable
- ingredientUOI_id: int - not nullable
- inventoryUOI_id: int - not nullable
- lotNoFormat_id: int - not nullable
- lotNoProduction: varchar(255) - not nullable
- lotNoReceiving: varchar(255) - not nullable
- lotNoTracking: varchar(255) - not nullable
- manufacturerReceiving: varchar(255) - not nullable
- manufacturerTracking: varchar(255) - not nullable
- manufacturingUOI_id: int - not nullable
- maxqty: int - not nullable
- minqty: int - not nullable
- mmInfoLabelSite: int - not nullable
- name: varchar(255) - not nullable
- overPickTolerance: varchar(255) - not nullable
- overReceivingTolerance: varchar(255) - not nullable
- overrideShippableMode: varchar(255) - not nullable
- owner_id: int - not nullable
- packlabel_id: int - not nullable
- pickingPriority: varchar(255) - not nullable
- pickingPriorityEnforcement: varchar(255) - not nullable
- pickingPriorityValidation: varchar(255) - not nullable
- pickingSequence: int - not nullable
- picklabel_id: int - not nullable
- printSingleShippingInfoLabelPerLine: varchar(10) - not nullable
- productionDateReceiving: varchar(255) - not nullable
- putawayAllowedCondition: varchar(255) - not nullable
- putawayFromReceiving: varchar(10) - not nullable
- putawayRestrainConfiguredZones: varchar(10) - not nullable
- quantityReasonRequired: varchar(255) - not nullable
- receivingUOI_id: int - not nullable
- receivingWeightDimensionUpdateDelay: int - not nullable
- receivingWeightDimensionUpdateMode: varchar(255) - not nullable
- reclabel_id: int - not nullable
- sampleQAFrequency: varchar(255) - not nullable
- sampleQAMode: varchar(255) - not nullable
- sampleQAQty: varchar(255) - not nullable
- scrapReasonList_id: int - not nullable
- serialNoFormat_id: int - not nullable
- serialNoTracking: varchar(255) - not nullable
- shiplabel_id: int - not nullable
- shippableLimit: varchar(255) - not nullable
- shippingInfoLabel_id: int - not nullable
- shippingInfoLabelQty: varchar(255) - not nullable
- shippingLabelQty: varchar(255) - not nullable
- shippingUOI_id: int - not nullable
- shortPickTolerance: varchar(255) - not nullable
- site_id: int - not nullable
- siteConfiguration_id: int - not nullable
- sitePartNo: varchar(255) - not nullable
- stackingMode: varchar(255) - not nullable
- temperatureCategory_id: int - not nullable
- uniqueAttributeByExternalBarcode: varchar(10) - not nullable
- vendorExpiryDateTolerance: varchar(255) - not nullable
- vendorExpiryDateToleranceMode: varchar(255) - not nullable
- womh_id: int - not nullable

### scMMStatistic
- oid: int - not nullable (Primary Key)
- mm_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- name: varchar(255) - not nullable
- site_id: int - not nullable
- value: varchar(255) - not nullable

### scMOVE
- oid: int - not nullable (Primary Key)
- fromLocation_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- condition_id: int - not nullable
- currentLocation_id: int - not nullable
- displayPartNo: varchar(255) - not nullable
- from_id: int - not nullable
- fromContainer_id: int - not nullable
- fromZone_id: int - not nullable
- generatedItem_id: int - not nullable
- inProgressQty: bigint - not nullable
- item_id: int - not nullable
- lastLockedTime: datetime - not nullable
- lastUser_id: int - not nullable
- lockedUntil: datetime - not nullable
- moveAction: varchar(255) - not nullable
- movedQty: bigint - not nullable
- movingJob_id: int - not nullable
- owner_id: int - not nullable
- priority: varchar(255) - not nullable
- quantity: bigint - not nullable
- queue_id: int - not nullable
- referenceNo: varchar(255) - not nullable
- replenReservedBarcode_id: int - not nullable
- requiredDate: datetime - not nullable
- to_id: int - not nullable
- toContainer_id: int - not nullable
- toLocation_id: int - not nullable
- toZone_id: int - not nullable
- type: varchar(255) - not nullable
- uoi_id: int - not nullable

### scMOVEDimension
- oid: bigint - not nullable (Primary Key)
- move_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- dimension_id: int - not nullable
- mode: varchar(255) - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable

### scMREQToSHLI
- oid: int - not nullable (Primary Key)
- mreq_id: int - not nullable (Foreign Key)
- shli_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- toReceiveQty: bigint - not nullable
- uoi_id: int - not nullable

### scMSHLH
- oid: int - not nullable (Primary Key)
- shipfrom_id: int - not nullable (Foreign Key)
- shipto_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- type_id: int - not nullable (Foreign Key)
- bolNumber: varchar(255) - not nullable
- carrier_id: int - not nullable
- classoid: int - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- deliveryArrival: datetime - not nullable
- deliveryDate: datetime - not nullable
- deliveryDeparture: datetime - not nullable
- deliverySequence: int - not nullable
- equipment_id: int - not nullable
- equipmentNo: varchar(255) - not nullable
- equipmentType_id: int - not nullable
- load_id: int - not nullable
- location_id: int - not nullable
- owner_id: int - not nullable
- referenceNo: varchar(255) - not nullable
- sealNo: varchar(255) - not nullable
- shippedDate: datetime - not nullable
- shippingTerms_id: int - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable

### scManufacturingJob
- oid: int - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- allowModifyDependencies: varchar(10) - not nullable
- allowOverProduction: varchar(10) - not nullable
- classoid: int - not nullable
- consumptionMethod: varchar(255) - not nullable
- consumptionTolerance: varchar(255) - not nullable
- consumptionToleranceMode: varchar(255) - not nullable
- defaultBatchSize: varchar(255) - not nullable
- description: text - not nullable
- expiryDateMode: varchar(255) - not nullable
- name: varchar(255) - not nullable
- outputCompletionCondition_id: int - not nullable
- outputCreationCondition_id: int - not nullable
- qtyConfirmationMethod: varchar(255) - not nullable
- qtyOutputMode: varchar(255) - not nullable
- receivingLabel_id: int - not nullable
- sequencingMethod: varchar(255) - not nullable
- siteConfiguration_id: int - not nullable
- status: varchar(255) - not nullable

### scMaterial
- oid: int - not nullable (Primary Key)
- agropurMaterialSupplier_id: int - not nullable (Foreign Key)
- asset_id: int - not nullable (Foreign Key)
- container_id: int - not nullable (Foreign Key)
- currentLOAD_id: int - not nullable (Foreign Key)
- currentPKLI_id: int - not nullable (Foreign Key)
- currentSHLI_id: int - not nullable (Foreign Key)
- expiryDate: datetime - not nullable (Foreign Key)
- externalOID: varchar(255) - not nullable (Foreign Key)
- label_id: int - not nullable (Foreign Key)
- location_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- origin_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- topAsset_id: int - not nullable (Foreign Key)
- topContainer_id: int - not nullable (Foreign Key)
- transportEquipment_id: int - not nullable (Foreign Key)
- type: varchar(255) - not nullable (Foreign Key)
- abcClass_id: int - not nullable
- agropurLotNo: varchar(255) - not nullable
- agropurLotNoCalculated: varchar(10) - not nullable
- classoid: int - not nullable
- condition: varchar(255) - not nullable
- conditionReason_id: int - not nullable
- costCenter_id: int - not nullable
- creationDate: datetime - not nullable
- currentMOVE_id: int - not nullable
- currentPKLH_id: int - not nullable
- currentRCLI_id: int - not nullable
- currentSKLI_id: int - not nullable
- currentUKLI_id: int - not nullable
- currentWOS_id: int - not nullable
- depth: decimal(19,2) - not nullable
- dimensionType: varchar(255) - not nullable
- dimensionUOM_id: int - not nullable
- displayPartNo: varchar(255) - not nullable
- height: decimal(19,2) - not nullable
- history_id: int - not nullable
- inventoryUOI_id: int - not nullable
- lastMovedDate: datetime - not nullable
- manualWeight: varchar(10) - not nullable
- materialCondition_id: int - not nullable
- mobileEquipment_id: int - not nullable
- output_id: int - not nullable
- owner_id: int - not nullable
- packingContainer_id: int - not nullable
- partitionNo: int - not nullable
- position: varchar(255) - not nullable
- previous_id: int - not nullable
- productionDate: datetime - not nullable
- putawayDate: datetime - not nullable
- quantity: bigint - not nullable
- receptionDate: datetime - not nullable
- reservedQty: bigint - not nullable
- site_id: int - not nullable
- unitCost: decimal(19,2) - not nullable
- unitPrice: decimal(19,2) - not nullable
- uoi_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable
- width: decimal(19,2) - not nullable
- zone_id: int - not nullable

### scMaterialBarcode
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable (Foreign Key)
- material_id: int - not nullable (Foreign Key)
- country_id: int - not nullable
- dimension_id: int - not nullable
- dimensionUOM_id: int - not nullable
- expiryDate: datetime - not nullable
- gtin_id: int - not nullable
- lotNo: varchar(255) - not nullable
- partitionNo: int - not nullable
- productionDate: datetime - not nullable
- quantity: bigint - not nullable
- report_id: int - not nullable
- status: varchar(255) - not nullable
- uoi_id: int - not nullable
- value: varchar(255) - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scMaterialMaster
- oid: int - not nullable (Primary Key)
- baseUOI_id: int - not nullable (Foreign Key)
- mmProductClass_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- partNo: varchar(255) - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- agrFormat: varchar(255) - not nullable
- argFormatUOM: varchar(255) - not nullable
- category2_id: int - not nullable
- category3_id: int - not nullable
- category_id: int - not nullable
- classoid: int - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- description: varchar(255) - not nullable
- description_id: int - not nullable
- hazmat: int - not nullable
- itemTemplate_id: int - not nullable
- maxNumberOfLicencePlatesStacked: int - not nullable
- name_id: int - not nullable
- natureSubClass: varchar(255) - not nullable
- nmfc: int - not nullable
- nmfcClass: int - not nullable
- owner_id: int - not nullable
- precisionlength: int - not nullable
- purchasingPrice: decimal(19,2) - not nullable
- shipInCase: varchar(10) - not nullable
- shippingDescription: varchar(255) - not nullable
- supplier: varchar(255) - not nullable
- type: varchar(255) - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable

### scMobileEquipment
- oid: int - not nullable (Primary Key)
- parent_id: int - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- capacity: decimal(19,2) - not nullable
- capacityUsed: decimal(19,2) - not nullable
- classoid: int - not nullable
- currentPKLH_id: int - not nullable
- dimensionUOM_id: int - not nullable
- items: int - not nullable
- job_id: int - not nullable
- location_id: int - not nullable
- maxWeight: decimal(19,2) - not nullable
- mobileEquipment_id: int - not nullable
- name: varchar(255) - not nullable
- status: varchar(255) - not nullable
- transportEquipment_id: int - not nullable
- type_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable
- zone_id: int - not nullable

### scMobileEquipmentType
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- agropurType: varchar(255) - not nullable
- capacity: decimal(19,2) - not nullable
- classoid: int - not nullable
- description: text - not nullable
- dimensionUOM_id: int - not nullable
- interiorDepth: decimal(19,2) - not nullable
- interiorHeight: decimal(19,2) - not nullable
- interiorWidth: decimal(19,2) - not nullable
- lpnCapacity: int - not nullable
- maxWeight: decimal(19,2) - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scMovement
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable (Foreign Key)
- eventDate: datetime - not nullable (Foreign Key)
- fromContainer_id: int - not nullable (Foreign Key)
- fromLocation_id: int - not nullable (Foreign Key)
- fromParent_id: int - not nullable (Foreign Key)
- fromSite_id: int - not nullable (Foreign Key)
- fromTransportEquipment_id: int - not nullable (Foreign Key)
- fromZone_id: int - not nullable (Foreign Key)
- item_id: int - not nullable (Foreign Key)
- itemMaster_id: int - not nullable (Foreign Key)
- reference_id: int - not nullable (Foreign Key)
- sourceItem_id: int - not nullable (Foreign Key)
- toContainer_id: int - not nullable (Foreign Key)
- toLocation_id: int - not nullable (Foreign Key)
- toParent_id: int - not nullable (Foreign Key)
- toSite_id: int - not nullable (Foreign Key)
- toTransportEquipment_id: int - not nullable (Foreign Key)
- toZone_id: int - not nullable (Foreign Key)
- type: varchar(255) - not nullable (Foreign Key)
- user_id: int - not nullable (Foreign Key)
- comment_id: int - not nullable
- dimensionUOM_id: int - not nullable
- fromCondition_id: int - not nullable
- fromCostCenter_id: int - not nullable
- fromMaterial_id: int - not nullable
- fromMobileEquipment_id: int - not nullable
- fromOwner_id: int - not nullable
- fromStatus: varchar(255) - not nullable
- fromTopContainer_id: int - not nullable
- parent_id: int - not nullable
- partitionNo: int - not nullable
- previous_id: int - not nullable
- quantity: bigint - not nullable
- reason_id: int - not nullable
- referenceName: varchar(255) - not nullable
- stampDate: datetime - not nullable
- toCondition_id: int - not nullable
- toCostCenter_id: int - not nullable
- toMaterial_id: int - not nullable
- toMobileEquipment_id: int - not nullable
- toOwner_id: int - not nullable
- toStatus: varchar(255) - not nullable
- toTopContainer_id: int - not nullable
- uoiconfig_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scMovingJob
- oid: int - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- allowLPNMove: varchar(10) - not nullable
- askMobileEquipmentOperating: varchar(10) - not nullable
- assumeQuantity: varchar(10) - not nullable
- classoid: int - not nullable
- description: text - not nullable
- lockingDuration: int - not nullable
- lpnCapacityDefault: int - not nullable
- lpnCapacityReachMode: varchar(255) - not nullable
- lpnCapacityStartMoveNotReachMode: varchar(255) - not nullable
- name: varchar(255) - not nullable
- returnToLocationAfterMove: varchar(10) - not nullable
- route_id: int - not nullable
- shortMode: varchar(255) - not nullable
- siteConfiguration_id: int - not nullable

### scOrder
- oid: int - not nullable (Primary Key)
- orderNo: varchar(255) - not nullable (Foreign Key)
- orderType_id: int - not nullable (Foreign Key)
- referenceNo: varchar(255) - not nullable (Foreign Key)
- requester_id: int - not nullable (Foreign Key)
- requiredDate: datetime - not nullable (Foreign Key)
- shippedDate: datetime - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- updateDate: datetime - not nullable (Foreign Key)
- workOrder_id: int - not nullable (Foreign Key)
- backOrder: varchar(255) - not nullable
- billTo_id: int - not nullable
- billToAddress_id: int - not nullable
- billToContact_id: int - not nullable
- billToCostCenter_id: int - not nullable
- billToName: varchar(255) - not nullable
- broker_id: int - not nullable
- cancelReason: int - not nullable
- classoid: int - not nullable
- consolidationGroup: varchar(255) - not nullable
- contractNo: varchar(255) - not nullable
- createUser_id: int - not nullable
- creationDate: datetime - not nullable
- cusotmerPO: varchar(255) - not nullable
- deliveryNo: varchar(255) - not nullable
- description: text - not nullable
- fillrateType_id: int - not nullable
- lastAdjustment_id: int - not nullable
- leadingStatus: varchar(255) - not nullable
- lifecycle: varchar(255) - not nullable
- loadingSequence: int - not nullable
- loadNumber: varchar(255) - not nullable
- loadSequence: int - not nullable
- maxShipmentQuantity: int - not nullable
- minimumFillrate: int - not nullable
- nbContainer: int - not nullable
- orderClass: varchar(255) - not nullable
- orderPrice: decimal(19,2) - not nullable
- originalOrderNo: varchar(255) - not nullable
- originalPO: int - not nullable
- owner_id: int - not nullable
- partitionNo: int - not nullable
- pickCOPosition: varchar(255) - not nullable
- pickTicketNo: varchar(255) - not nullable
- priority: varchar(255) - not nullable
- receivedDate: datetime - not nullable
- requesterContact_id: int - not nullable
- requesterDepartment_id: int - not nullable
- route: varchar(255) - not nullable
- sealNumber: varchar(255) - not nullable
- sendCancelQtiesToOracle: varchar(10) - not nullable
- sequenceERPConfirmation: int - not nullable
- shipmentCount: int - not nullable
- shippingDetails_id: int - not nullable
- supplier_id: int - not nullable
- trailer: varchar(255) - not nullable
- trailingStatus: varchar(255) - not nullable
- updateUser_id: int - not nullable
- workOrderNo: varchar(255) - not nullable

### scOrderAdjustment
- oid: bigint - not nullable (Primary Key)
- order_id: int - not nullable (Foreign Key)
- reference_id: int - not nullable (Foreign Key)
- allocatedValue: int - not nullable
- cancelledValue: int - not nullable
- classoid: int - not nullable
- eventDate: datetime - not nullable
- fillRateType_id: int - not nullable
- leadingStatus: varchar(255) - not nullable
- orderedValue: int - not nullable
- outstandingValue: int - not nullable
- packedValue: int - not nullable
- partitionNo: int - not nullable
- pickedValue: int - not nullable
- shippedValue: int - not nullable
- status: varchar(255) - not nullable
- trailingStatus: varchar(255) - not nullable
- type: varchar(255) - not nullable
- user_id: int - not nullable

### scOrderInstruction
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- instruction: text - not nullable
- mreq_id: int - not nullable
- partitionNo: int - not nullable
- solh_id: int - not nullable
- type: varchar(255) - not nullable

### scOrderLine
- oid: int - not nullable (Primary Key)
- currentLoad_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- pickTicketNo: varchar(255) - not nullable (Foreign Key)
- referenceNo: varchar(255) - not nullable (Foreign Key)
- requiredDate: datetime - not nullable (Foreign Key)
- shipmentRequest_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- wave_id: int - not nullable (Foreign Key)
- wos_id: int - not nullable (Foreign Key)
- allocatedQty: bigint - not nullable
- allocationInvPolicy_id: int - not nullable
- backOrder: varchar(255) - not nullable
- backorderQty: bigint - not nullable
- billToCostCenter_id: int - not nullable
- blockPartialShipment: varchar(255) - not nullable
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- condition_id: int - not nullable
- consolidationGroup: varchar(255) - not nullable
- consumedQty: bigint - not nullable
- costcenter_id: int - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- currency: varchar(255) - not nullable
- description: text - not nullable
- displayPartNo: varchar(255) - not nullable
- fillrateType_id: int - not nullable
- generatedMREQ_id: int - not nullable
- ignoreOrderFillrate: varchar(10) - not nullable
- leadingStatus: varchar(255) - not nullable
- lineOutstandingToCancelReason: int - not nullable
- loadedQty: bigint - not nullable
- minimumFillrate: int - not nullable
- outstandingQty: bigint - not nullable
- overrideShippable: varchar(255) - not nullable
- owner_id: int - not nullable
- packedQty: bigint - not nullable
- partitionNo: int - not nullable
- pickCOPosition: varchar(255) - not nullable
- pickedQty: bigint - not nullable
- prepositionQty: bigint - not nullable
- priority: varchar(255) - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- receivingUOI_id: int - not nullable
- releasedQty: bigint - not nullable
- sequence: varchar(255) - not nullable
- shippedDate: datetime - not nullable
- shippedQty: bigint - not nullable
- shipTo_id: int - not nullable
- shipToContact_id: int - not nullable
- shipToDepartment_id: int - not nullable
- shipToDoor_id: int - not nullable
- shipToLocation_id: int - not nullable
- stagedQty: bigint - not nullable
- supplier_id: int - not nullable
- supplierLocation_id: int - not nullable
- supplierZone_id: int - not nullable
- toReceiveQty: bigint - not nullable
- trailingStatus: varchar(255) - not nullable
- unitPrice: decimal(19,2) - not nullable
- uoi_id: int - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable

### scOrderLineDimension
- oid: bigint - not nullable (Primary Key)
- soli_id: int - not nullable (Foreign Key)
- backOrderQty: bigint - not nullable
- classoid: int - not nullable
- dimension_id: int - not nullable
- mode: varchar(255) - not nullable
- partitionNo: int - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable

### scOrderLineLog
- oid: int - not nullable (Primary Key)
- orderLine_id: int - not nullable (Foreign Key)
- eventDate: datetime - not nullable
- orderLineData: varchar(10000) - not nullable

### scOrderType
- oid: int - not nullable (Primary Key)
- agropur_AllowDeliverFromContainerDeliveryWhenLoad: varchar(10) - not nullable
- allowContainerDelivery: varchar(10) - not nullable
- allowUpdateCarrier: varchar(10) - not nullable
- allowUpdateLoad: varchar(10) - not nullable
- autoReleaseQty: varchar(10) - not nullable
- canBeLockedByChecklist: varchar(255) - not nullable
- cancelReasonList: int - not nullable
- cancelReasonRequired: varchar(10) - not nullable
- classoid: int - not nullable
- condition_id: int - not nullable
- defaultSOLIPriority: varchar(255) - not nullable
- deliverRestriction: varchar(255) - not nullable
- deliveryNoAssignment: varchar(255) - not nullable
- description: varchar(255) - not nullable
- enableTEUsageStatusWhenReceiptCompleted: varchar(255) - not nullable
- fillrateType_id: int - not nullable
- InboundCompletionAction: varchar(255) - not nullable
- initialStatus: varchar(255) - not nullable
- lifeCycle: varchar(255) - not nullable
- lineOutstandingToCancelReasonList: int - not nullable
- lineOutstandingToCancelReasonRequired: varchar(10) - not nullable
- maxShipPKLIStatusRequired: varchar(255) - not nullable
- name: varchar(255) - not nullable
- orderClass: varchar(255) - not nullable
- orderCompletion: varchar(255) - not nullable
- orderCreation: varchar(255) - not nullable
- outboundCancellation: varchar(255) - not nullable
- outboundModification: varchar(255) - not nullable
- owner: varchar(255) - not nullable
- preReceivingChecklist_id: int - not nullable
- reason_id: int - not nullable
- receiptClosureAction: varchar(255) - not nullable
- shipAction: varchar(255) - not nullable
- shipmentCreation: varchar(255) - not nullable
- shipmentType_id: int - not nullable
- shortPickAction: varchar(255) - not nullable
- status: varchar(255) - not nullable
- teUsageStatusWhenReceiptCompleted: varchar(255) - not nullable
- thresholdToEnableClosing: varchar(255) - not nullable
- zeroPickAction: varchar(255) - not nullable

### scPKLH
- oid: int - not nullable (Primary Key)
- parent_id: int - not nullable (Foreign Key)
- pickingJob_id: int - not nullable (Foreign Key)
- requiredDate: datetime - not nullable (Foreign Key)
- shipmentRequest_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- assignedDate: datetime - not nullable
- balancingMethodUsed: varchar(255) - not nullable
- classoid: int - not nullable
- consolidation_pklh_id: int - not nullable
- containerType_id: int - not nullable
- dimensionUOM_id: int - not nullable
- firstLocation_id: int - not nullable
- firstZone_id: int - not nullable
- lastPickStamp: datetime - not nullable
- load_id: int - not nullable
- loadSequence: int - not nullable
- partitionNo: int - not nullable
- plannedEnd: datetime - not nullable
- plannedStart: datetime - not nullable
- printedDate: datetime - not nullable
- priority: varchar(255) - not nullable
- queue_id: int - not nullable
- referenceNo: varchar(255) - not nullable
- site_id: int - not nullable
- sortedByLayer: varchar(10) - not nullable
- splitOrderedPickLines: varchar(10) - not nullable
- subType: varchar(255) - not nullable
- user_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable
- zone_id: int - not nullable

### scPKLI
- oid: int - not nullable (Primary Key)
- generatedMREQ_id: int - not nullable (Foreign Key)
- load_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- mreq_id: int - not nullable (Foreign Key)
- pickedDate: datetime - not nullable (Foreign Key)
- pklh_id: int - not nullable (Foreign Key)
- referenceNo: varchar(255) - not nullable (Foreign Key)
- requiredDate: datetime - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- supplierLocation_id: int - not nullable (Foreign Key)
- backorder: varchar(255) - not nullable
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- condition_id: int - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- currentContainer_id: int - not nullable
- dimensionUOM_id: int - not nullable
- expiryDate: datetime - not nullable
- invalidPickPriority: varchar(10) - not nullable
- loadSequence: int - not nullable
- location_id: int - not nullable
- mreqToLoad_id: int - not nullable
- owner_id: int - not nullable
- packedQty: bigint - not nullable
- palletLayer: varchar(255) - not nullable
- parent_id: int - not nullable
- partitionNo: int - not nullable
- pickAction: varchar(255) - not nullable
- pickCOPosition: varchar(255) - not nullable
- pickedByUser_id: int - not nullable
- pickedQty: bigint - not nullable
- pickingLayer: int - not nullable
- priority: varchar(255) - not nullable
- quantity: bigint - not nullable
- rcli_id: int - not nullable
- replenishmentCount: int - not nullable
- requester_id: int - not nullable
- sequence: int - not nullable
- shipTo_id: int - not nullable
- site_id: int - not nullable
- splitPickLine: varchar(10) - not nullable
- subType: varchar(255) - not nullable
- supplier_id: int - not nullable
- supplierZone_id: int - not nullable
- toPickQuantity: bigint - not nullable
- uoi_id: int - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable
- zone_id: int - not nullable

### scPKLIDimension
- oid: bigint - not nullable (Primary Key)
- pkli_id: int - not nullable (Foreign Key)
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- dimension_id: int - not nullable
- mode: varchar(255) - not nullable
- partitionNo: int - not nullable
- pickedQty: bigint - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable

### scPackingJob
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- site_id: int - not nullable
- siteConfiguration_id: int - not nullable

### scPickingJob
- oid: int - not nullable (Primary Key)
- route_id: int - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- askMobileEquipmentOperating: varchar(10) - not nullable
- assemblyLevel: varchar(255) - not nullable
- assemblyStartLocation: varchar(255) - not nullable
- assyOverflowStrategy: varchar(255) - not nullable
- autoDropLocation_id: int - not nullable
- blockPicklistScanByUnassignedUsers: varchar(10) - not nullable
- bulkClusterCapacity: int - not nullable
- classoid: int - not nullable
- clustersize: int - not nullable
- confMethod: varchar(255) - not nullable
- coPosAssignMode: varchar(255) - not nullable
- defaultContainer_id: int - not nullable
- defaultCountingJob_id: int - not nullable
- description: text - not nullable
- dropSuggestionSource: varchar(255) - not nullable
- groupingZone: int - not nullable
- groupMethod: varchar(255) - not nullable
- includebo: varchar(255) - not nullable
- includePending: varchar(10) - not nullable
- labelFormat: varchar(255) - not nullable
- labelGroupBy: varchar(255) - not nullable
- maxItems: int - not nullable
- maxlines: int - not nullable
- maxLocations: int - not nullable
- maxorders: int - not nullable
- name: varchar(255) - not nullable
- notifyPKLHComplete: varchar(10) - not nullable
- notifyZoneChange: varchar(10) - not nullable
- orderlineqty: varchar(255) - not nullable
- orderType: varchar(255) - not nullable
- overPickTolerance: varchar(255) - not nullable
- overweightPercent: int - not nullable
- overweightStrategy: varchar(10) - not nullable
- packreport_id: int - not nullable
- palletLevelingAssemblyMinLayerThreshold: decimal(19,2) - not nullable
- palletLevelingLayerOnPallet: int - not nullable
- palletLevelingLinkedPickingJob: int - not nullable
- palletLevelingMaxLayerOnPallet: int - not nullable
- palletLevelingMinLayerOnPallet: int - not nullable
- palletLevelingOverloadThreshold: decimal(19,2) - not nullable
- palletLevelingRangeFullPallet: varchar(255) - not nullable
- palletLevelingSharedPalletCultureSpace: int - not nullable
- pickingLabel_id: int - not nullable
- pickingPriorityValidation: varchar(255) - not nullable
- pickListBalancingMethod: varchar(255) - not nullable
- pickmethod: varchar(255) - not nullable
- pickmode: varchar(255) - not nullable
- pickRfListMode: varchar(255) - not nullable
- pklhCapacityReachMode: varchar(255) - not nullable
- printLabelAtPicking: varchar(10) - not nullable
- productConfirmationMethod: varchar(255) - not nullable
- qtyConfMethod: varchar(255) - not nullable
- reverseConsolidationMode: varchar(255) - not nullable
- sequence: int - not nullable
- shippingInfoLabel_id: int - not nullable
- shippingInfoLabelQty: varchar(255) - not nullable
- shippingLabel_id: int - not nullable
- shippingLabelQty: varchar(255) - not nullable
- shortPickAction: varchar(255) - not nullable
- shortPickCountMode: varchar(255) - not nullable
- shortPickTolerance: varchar(255) - not nullable
- showInstructions: varchar(255) - not nullable
- siteConfiguration_id: int - not nullable
- skipZoneList: varchar(255) - not nullable
- sortedByLayer: varchar(10) - not nullable
- sortorder: varchar(255) - not nullable
- sortOrderList: varchar(255) - not nullable
- splitcarriers: varchar(10) - not nullable
- splitConsGroup: varchar(10) - not nullable
- splitdestination: varchar(255) - not nullable
- splitfamily: varchar(10) - not nullable
- splitShipment: varchar(10) - not nullable
- splitShipVia: varchar(10) - not nullable
- splitVolWeight: varchar(255) - not nullable
- userRequiredToReleaseOnAssembly: varchar(10) - not nullable
- voicePicking: varchar(255) - not nullable
- volCapacity: decimal(19,2) - not nullable
- warnBaseUOI: varchar(10) - not nullable
- weightbase: int - not nullable
- weightCapacity: decimal(19,2) - not nullable
- workcenter_id: int - not nullable

### scPrinter
- oid: int - not nullable (Primary Key)
- backup_id: int - not nullable
- classoid: int - not nullable
- name: varchar(255) - not nullable
- path: varchar(255) - not nullable
- printerFormat_id: int - not nullable
- printService_id: int - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable
- type_id: int - not nullable
- voiceLabel_id: int - not nullable

### scProductCategory
- oid: int - not nullable (Primary Key)
- code: varchar(255) - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- description: varchar(255) - not nullable
- mmPosition: varchar(255) - not nullable

### scProductCategoryItem
- oid: int - not nullable (Primary Key)
- category_id: int - not nullable
- classoid: int - not nullable
- code: varchar(255) - not nullable
- name: varchar(255) - not nullable

### scProductClass
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- code: varchar(255) - not nullable
- glaccount_id: int - not nullable
- glcode: varchar(255) - not nullable
- name: varchar(255) - not nullable
- shipdesc: varchar(255) - not nullable

### scPutawayJob
- oid: int - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- allowAllConditions: varchar(10) - not nullable
- allowPutawayOverride: varchar(10) - not nullable
- automaticTaskCreation: varchar(255) - not nullable
- binTypeSequenceRequired: varchar(10) - not nullable
- classoid: int - not nullable
- constraintLocationMode: varchar(255) - not nullable
- description: text - not nullable
- maxAddSuggestions: varchar(255) - not nullable
- maxInitialSuggestions: varchar(255) - not nullable
- movingJob_id: int - not nullable
- name: varchar(255) - not nullable
- pickingPriority: varchar(255) - not nullable
- pickingPriorityEnforcement: varchar(255) - not nullable
- putawayOverrideReasonMode: varchar(255) - not nullable
- siteConfiguration_id: int - not nullable
- suggestionMode: varchar(255) - not nullable
- uoiMode: varchar(255) - not nullable

### scPutawayOverrideEvent
- oid: bigint - not nullable (Primary Key)
- reason_id: int - not nullable (Foreign Key)
- timestamp: datetime - not nullable (Foreign Key)
- user_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- location_id: int - not nullable
- materialMaster_id: int - not nullable
- movement_id: int - not nullable
- suggestedLocation_id: int - not nullable

### scPutawayOverrideEventReason
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- description: varchar(255) - not nullable
- label: varchar(255) - not nullable
- name: varchar(255) - not nullable

### scPutawaySuggestion
- oid: bigint - not nullable (Primary Key)
- putawayJob_id: int - not nullable (Foreign Key)
- allocateInventory: varchar(10) - not nullable
- classoid: int - not nullable
- enableConfLocMovingQtyRange: varchar(10) - not nullable
- locationType: varchar(255) - not nullable
- maxPriority: varchar(255) - not nullable
- maxSuggestions: int - not nullable
- minPercentage: int - not nullable
- minPriority: varchar(255) - not nullable
- name: varchar(255) - not nullable
- nearSuggestion_id: int - not nullable
- sequence: int - not nullable
- sortBy: varchar(255) - not nullable
- sortMode: varchar(255) - not nullable

### scRCLH
- oid: int - not nullable (Primary Key)
- document_id: int - not nullable (Foreign Key)
- referenceNo: varchar(255) - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- supplier_id: int - not nullable (Foreign Key)
- bolNumber: varchar(255) - not nullable
- classoid: int - not nullable
- completedDate: datetime - not nullable
- documentNo: varchar(255) - not nullable
- location_id: int - not nullable
- owner_id: int - not nullable
- pickTicketNo: varchar(255) - not nullable
- priority: varchar(255) - not nullable
- receiptDate: datetime - not nullable
- receivingJob_id: int - not nullable
- reopenedDate: datetime - not nullable
- shippedDate: datetime - not nullable
- type: varchar(255) - not nullable
- unforecasted: varchar(10) - not nullable
- user_id: int - not nullable

### scRCLI
- oid: int - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- mreq_id: int - not nullable (Foreign Key)
- rclh_id: int - not nullable (Foreign Key)
- receivedDate: datetime - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- costCenter_id: int - not nullable
- deliverTo_id: int - not nullable
- description: varchar(255) - not nullable
- isQASample: varchar(10) - not nullable
- location_id: int - not nullable
- material_id: int - not nullable
- parentRCLI_id: int - not nullable
- priority: varchar(255) - not nullable
- putawayJob_id: int - not nullable
- quantity: bigint - not nullable
- receivedQuantity: bigint - not nullable
- referenceNo: varchar(255) - not nullable
- supplier_id: int - not nullable
- uoi_id: int - not nullable
- user_id: int - not nullable

### scRCLIDimension
- oid: bigint - not nullable (Primary Key)
- dimension_id: int - not nullable (Foreign Key)
- rcli_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable

### scRack
- oid: int - not nullable (Primary Key)
- aisle_id: int - not nullable (Foreign Key)
- allocateInventory: varchar(255) - not nullable
- classoid: int - not nullable
- lightId: varchar(255) - not nullable
- name: varchar(255) - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable
- velocity: varchar(255) - not nullable

### scReasonList
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- name: varchar(255) - not nullable

### scReasonListItem
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- list_id: int - not nullable
- reason_id: int - not nullable
- sequence: int - not nullable

### scReceivingJob
- oid: int - not nullable (Primary Key)
- allowMixConditionsInContainer: varchar(255) - not nullable
- allowMultipleQtyReceiving: varchar(10) - not nullable
- allowMultipleScanReceiving: varchar(10) - not nullable
- allowOverReceiving: varchar(255) - not nullable
- allowReceivingWhenMissingHandlingMaterials: varchar(10) - not nullable
- allowReopeningRCLH: varchar(10) - not nullable
- askBOLNumberReceiving: varchar(255) - not nullable
- askCommentReceiving: varchar(10) - not nullable
- askCostCenterUnforcastedReceiving: varchar(10) - not nullable
- askDepartmentUnforcastedReceiving: varchar(10) - not nullable
- askDestinationUnforcastedReceiving: varchar(10) - not nullable
- askDocumentNoUnforcatedReceiving: varchar(10) - not nullable
- askMultiScanCyclesReceiving: varchar(10) - not nullable
- askOriginUnforcastedReceiving: varchar(10) - not nullable
- askZoneForNewCOReceiving: varchar(10) - not nullable
- canBeLockedByChecklist: varchar(255) - not nullable
- classoid: int - not nullable
- conditionChangeReasonList_id: int - not nullable
- consolidateReceiving: varchar(10) - not nullable
- defaultItemOwner: varchar(255) - not nullable
- defaultMaterialConditionReceiving_id: int - not nullable
- description: text - not nullable
- enableTEUsageStatusWhenReceiptCompleted: varchar(255) - not nullable
- handlingMaterialPutawayBay_id: int - not nullable
- inboundLineSortOrder: varchar(255) - not nullable
- inboundShowPartNumber: varchar(255) - not nullable
- materialLabelRequiredOnReceiving: varchar(10) - not nullable
- maximumQuantityReceiving: varchar(255) - not nullable
- missingDepthWarning: varchar(10) - not nullable
- missingDimensionCondition_id: int - not nullable
- missingHeightWarning: varchar(10) - not nullable
- missingWeightWarning: varchar(10) - not nullable
- missingWidthWarning: varchar(10) - not nullable
- name: varchar(255) - not nullable
- noAllocatableInventoryWarning: varchar(10) - not nullable
- preReceivingChecklist_id: int - not nullable
- printExternalBarcodeOnReceiving: varchar(10) - not nullable
- printingWorkCenter_id: int - not nullable
- qaMaterialConditionReceiving_id: int - not nullable
- receiptClosureAction: varchar(255) - not nullable
- receivingLabel_id: int - not nullable
- receivingLocationEnforcement: varchar(255) - not nullable
- receivingMode: varchar(255) - not nullable
- receivingMultipleDocument: varchar(10) - not nullable
- receivingMultipleShipment: varchar(10) - not nullable
- receivingPrintMaterialLabel: varchar(255) - not nullable
- recGroupReceivingLines: varchar(10) - not nullable
- sampleQAQuantityMode: varchar(255) - not nullable
- showRelatedOrderOnReceiving: varchar(10) - not nullable
- site_id: int - not nullable
- siteConfiguration_id: int - not nullable
- specificNoScanReceivingConsolidationMode: varchar(255) - not nullable
- teUsageStatusWhenReceiptCompleted: varchar(255) - not nullable
- thresholdToEnableClosing: varchar(255) - not nullable
- xdockMode_Opportunities: varchar(255) - not nullable
- xdockMode_SOBind: varchar(255) - not nullable

### scReplenishmentJob
- oid: int - not nullable (Primary Key)
- allowFromFixedPick: varchar(10) - not nullable
- classoid: int - not nullable
- description: text - not nullable
- dropAction: varchar(255) - not nullable
- lpnQtyRoundingMode: varchar(255) - not nullable
- mergeQuantity: varchar(10) - not nullable
- mergeReplenishments: varchar(10) - not nullable
- movingJob_id: int - not nullable
- name: varchar(255) - not nullable
- qtyPriorityMode: varchar(255) - not nullable
- site_id: int - not nullable
- siteConfiguration_id: int - not nullable

### scSHLH
- oid: int - not nullable (Primary Key)
- orderNo: varchar(255) - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- shippedDate: datetime - not nullable (Foreign Key)
- billTo_id: int - not nullable
- classoid: int - not nullable
- customerOrderNo: varchar(255) - not nullable
- deliveryDate: datetime - not nullable
- lastAdjustment_id: int - not nullable
- owner_id: int - not nullable
- partitionNo: int - not nullable
- reference_id: int - not nullable
- referenceNo: varchar(255) - not nullable
- requester_id: int - not nullable
- requiredDate: datetime - not nullable
- shipFrom_id: int - not nullable
- shipmentRequest_id: int - not nullable
- shippingServiceLevel_id: int - not nullable
- shipTo_id: int - not nullable
- shipToAddress_id: int - not nullable
- status: varchar(255) - not nullable
- type_id: int - not nullable

### scSHLI
- oid: int - not nullable (Primary Key)
- masterShipment_id: int - not nullable (Foreign Key)
- pack_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- cancelledDate: varchar(255) - not nullable
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- deliveryDate: datetime - not nullable
- dimensionUOM_id: int - not nullable
- externalOID: varchar(255) - not nullable
- materialMaster_id: int - not nullable
- orderLine_id: int - not nullable
- owner_id: int - not nullable
- partitionNo: int - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- referenceNo: varchar(255) - not nullable
- requiredDate: datetime - not nullable
- sequence: varchar(255) - not nullable
- shippedDate: datetime - not nullable
- shipTo_id: int - not nullable
- shipToDepartment_id: int - not nullable
- status: varchar(255) - not nullable
- supplier_id: int - not nullable
- toReceiveQty: bigint - not nullable
- uoi_id: int - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scSHLIDimension
- oid: bigint - not nullable (Primary Key)
- dimension_id: int - not nullable (Foreign Key)
- shli_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- partitionNo: int - not nullable
- quantity: bigint - not nullable
- uoi_id: int - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scSHLP
- oid: int - not nullable (Primary Key)
- container_id: int - not nullable (Foreign Key)
- masterShipment_id: int - not nullable (Foreign Key)
- pack_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- cancelledDate: varchar(255) - not nullable
- classoid: int - not nullable
- containerType_id: int - not nullable
- deliveryDate: datetime - not nullable
- dimensionUOM_id: int - not nullable
- partitionNo: int - not nullable
- sequence: int - not nullable
- sscc: varchar(255) - not nullable
- status: varchar(255) - not nullable
- trackingNo: varchar(255) - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scSKLH
- oid: int - not nullable (Primary Key)
- cycleCount_id: int - not nullable (Foreign Key)
- location_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- session_id: int - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- aisle_id: int - not nullable
- classoid: int - not nullable
- completedDate: datetime - not nullable
- countingMode: varchar(255) - not nullable
- inconsistentAction: varchar(255) - not nullable
- inconsistentSKLH: int - not nullable
- inconsistentSKLI_id: int - not nullable
- owner_id: int - not nullable
- priority: int - not nullable
- referenceNo: varchar(255) - not nullable
- startDate: datetime - not nullable
- verificationDate: datetime - not nullable
- verifiedByUser_id: int - not nullable
- zone_id: int - not nullable

### scSKLHCount
- oid: bigint - not nullable (Primary Key)
- sklh_id: int - not nullable (Foreign Key)
- batchCountType: varchar(255) - not nullable
- classoid: int - not nullable
- completedDate: datetime - not nullable
- countedQtyItem: bigint - not nullable
- countedQtyLPN: int - not nullable
- countNo: int - not nullable
- expectedQtyItem: bigint - not nullable
- expectedQtyLPN: int - not nullable
- materialMaster_id: int - not nullable
- previousCount: int - not nullable
- status: varchar(255) - not nullable
- uoiConfig_id: int - not nullable
- user_id: int - not nullable

### scSKLI
- oid: int - not nullable (Primary Key)
- lastCount_id: int - not nullable (Foreign Key)
- materialMaster_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- skli_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- abcClass_id: int - not nullable
- adjustedQty: bigint - not nullable
- adjustedWeight: decimal(19,2) - not nullable
- classoid: int - not nullable
- condition_id: int - not nullable
- container_id: int - not nullable
- countAllLPOneCount: varchar(10) - not nullable
- countingJob_id: int - not nullable
- dimension_id: int - not nullable
- displayPartNo: varchar(255) - not nullable
- inconsistentAction: varchar(255) - not nullable
- inconsistentReason: varchar(255) - not nullable
- inconsistentRelatedSKLI_id: int - not nullable
- label_id: int - not nullable
- owner_id: int - not nullable
- serialMoved: varchar(10) - not nullable
- site_id: int - not nullable
- totalCount: int - not nullable
- uoi_id: int - not nullable
- verificationDate: datetime - not nullable
- verifiedByUser_id: int - not nullable
- weightUOM: int - not nullable

### scSKLICount
- oid: bigint - not nullable (Primary Key)
- skli_id: int - not nullable (Foreign Key)
- adjustedWeight: decimal(19,2) - not nullable
- adjustment: bigint - not nullable
- classoid: int - not nullable
- completedDate: datetime - not nullable
- countedQty: bigint - not nullable
- countedWeight: decimal(19,2) - not nullable
- countNo: int - not nullable
- expectedQty: bigint - not nullable
- expectedWeight: decimal(19,2) - not nullable
- previousCount_id: int - not nullable
- status: varchar(255) - not nullable
- uoi_id: int - not nullable
- user_id: int - not nullable
- weightUOM: int - not nullable

### scSOLHReason
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- name: varchar(255) - not nullable

### scSOLHReasonList
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- name: varchar(255) - not nullable

### scShipmentRequest
- oid: int - not nullable (Primary Key)
- carrier_id: int - not nullable (Foreign Key)
- deliverByDate: datetime - not nullable (Foreign Key)
- deliveryNo: varchar(255) - not nullable (Foreign Key)
- load_id: int - not nullable (Foreign Key)
- reference_id: int - not nullable (Foreign Key)
- shipTo_id: int - not nullable (Foreign Key)
- wave_id: int - not nullable (Foreign Key)
- allocationInvPolicy_id: int - not nullable
- bolreport_id: int - not nullable
- broker_id: int - not nullable
- callDeliveryAppointment: varchar(10) - not nullable
- cancelByDate: datetime - not nullable
- carrierBillAccount: varchar(255) - not nullable
- carrierDeliveryOption: varchar(255) - not nullable
- carrierShippingInsurance: varchar(255) - not nullable
- classoid: int - not nullable
- codAmount: decimal(19,2) - not nullable
- creationDate: datetime - not nullable
- freightTerms_id: int - not nullable
- ignoreAddressValidation: varchar(10) - not nullable
- insideDelivery: varchar(10) - not nullable
- liftGate: varchar(10) - not nullable
- loadingDock: varchar(10) - not nullable
- name: varchar(255) - not nullable
- packingSlip_id: int - not nullable
- partitionNo: int - not nullable
- pickByDate: datetime - not nullable
- plannedShippingCost: decimal(19,2) - not nullable
- referenceNo: varchar(255) - not nullable
- releaseDate: datetime - not nullable
- requestDate: datetime - not nullable
- requester_id: int - not nullable
- route_id: int - not nullable
- routingGuide: varchar(10) - not nullable
- serviceLevel_id: int - not nullable
- shipByDate: datetime - not nullable
- shipFrom_id: int - not nullable
- shipFromAddress_id: int - not nullable
- shipFromContact_id: int - not nullable
- shipFromName: varchar(255) - not nullable
- shipFromPhoneNo: varchar(255) - not nullable
- shippingIssurance: varchar(255) - not nullable
- shipToAddress_id: int - not nullable
- shipToContact_id: int - not nullable
- shipToLocation_id: int - not nullable
- shipToName: varchar(255) - not nullable
- shipToPhoneNo: varchar(255) - not nullable
- shipToZone_id: int - not nullable
- shipVia_id: int - not nullable
- shipViaAddress_id: int - not nullable
- shipViaContact_id: int - not nullable
- shipViaName: varchar(255) - not nullable
- status: varchar(255) - not nullable
- thirdPartyFreight_id: int - not nullable
- type_id: int - not nullable
- workCenter_id: int - not nullable
- workCenterType_id: int - not nullable

### scShipmentType
- oid: int - not nullable (Primary Key)
- canBeLockedByChecklist: varchar(255) - not nullable
- classoid: int - not nullable
- creationMode: varchar(255) - not nullable
- description: varchar(255) - not nullable
- enableTEUsageStatusWhenReceiptCompleted: varchar(255) - not nullable
- name: varchar(255) - not nullable
- preReceivingChecklist_id: int - not nullable
- receiptClosureAction: varchar(255) - not nullable
- status: varchar(255) - not nullable
- teUsageStatusWhenReceiptCompleted: varchar(255) - not nullable

### scShippingJob
- oid: int - not nullable (Primary Key)
- bolQty: int - not nullable
- classoid: int - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- packingSlip_id: int - not nullable
- packingSlipQty: int - not nullable
- site_id: int - not nullable
- siteConfiguration_id: int - not nullable
- weightCapture: varchar(255) - not nullable

### scShippingServiceLevel
- oid: int - not nullable (Primary Key)
- carrier_id: int - not nullable
- classoid: int - not nullable
- code: varchar(255) - not nullable
- name: varchar(255) - not nullable
- overrideShippableRule: varchar(255) - not nullable
- tmsCode: varchar(255) - not nullable
- Type: varchar(255) - not nullable

### scSite
- oid: int - not nullable (Primary Key)
- accountNo: varchar(255) - not nullable (Foreign Key)
- gln: varchar(255) - not nullable (Foreign Key)
- language_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- primaryContact_id: int - not nullable (Foreign Key)
- siteType_id: int - not nullable (Foreign Key)
- address_id: int - not nullable
- asn_Dept: varchar(255) - not nullable
- asn_Store: varchar(255) - not nullable
- asnEnable: varchar(10) - not nullable
- asnNbPalletLAbel: int - not nullable
- banner: varchar(255) - not nullable
- bannerGroup: varchar(255) - not nullable
- carrierType: varchar(255) - not nullable
- classoid: int - not nullable
- createStamp: datetime - not nullable
- createUser_id: int - not nullable
- currency_id: int - not nullable
- departmentNo: varchar(255) - not nullable
- displayName: varchar(255) - not nullable
- dunsNo: varchar(255) - not nullable
- email: varchar(255) - not nullable
- externalType: varchar(255) - not nullable
- family: varchar(255) - not nullable
- faxNo: varchar(255) - not nullable
- freightCode: varchar(255) - not nullable
- geoZone: varchar(255) - not nullable
- gs1_Company_Prefix: varchar(255) - not nullable
- overrideShippableRule: varchar(255) - not nullable
- parent_id: int - not nullable
- phoneNo: varchar(255) - not nullable
- scac: varchar(255) - not nullable
- status: varchar(255) - not nullable
- storeNo: varchar(255) - not nullable
- storeNumber: varchar(255) - not nullable
- taxIdentificationNo: varchar(255) - not nullable
- updateStamp: datetime - not nullable
- updateUser_id: int - not nullable
- webSite: varchar(255) - not nullable

### scSiteConfiguration
- oid: int - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- accountNo: varchar(255) - not nullable
- allocationInvPolicy_id: int - not nullable
- allocationJob_id: int - not nullable
- allowNumericLocationAlias: varchar(10) - not nullable
- bigDecimalTolerance: varchar(255) - not nullable
- calendarOptions_id: int - not nullable
- classoid: int - not nullable
- consolidationJob_id: int - not nullable
- countingJob_id: int - not nullable
- deliveryJob_id: int - not nullable
- dimensionUOM_id: int - not nullable
- isContainerTracking: varchar(10) - not nullable
- itemConfiguration_id: int - not nullable
- loadingJob_id: int - not nullable
- manufacturingJob_id: int - not nullable
- maxGenericCOLabelToPrint: varchar(255) - not nullable
- maxGenericMILabelToPrint: varchar(255) - not nullable
- movingJob_id: int - not nullable
- name: varchar(255) - not nullable
- orderLineSequenceMode: varchar(255) - not nullable
- packingJob_id: int - not nullable
- parent_id: int - not nullable
- pickingJob_id: int - not nullable
- putawayJob_id: int - not nullable
- receivingJob_id: int - not nullable
- replenishmentJob_id: int - not nullable
- shippingJob_id: int - not nullable
- temperatureUOM_id: int - not nullable
- unloadingJob_id: int - not nullable
- weightUOM_id: int - not nullable
- zoneSequencing: varchar(255) - not nullable

### scSiteOrderType
- oid: bigint - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- defaultSOLIPriority: varchar(255) - not nullable
- orderType_id: int - not nullable
- policy_id: int - not nullable
- receivingJob_id: int - not nullable
- wavingJob_id: int - not nullable

### scSiteType
- oid: int - not nullable (Primary Key)
- billingCustomer: varchar(10) - not nullable
- billingLocation: varchar(10) - not nullable
- broker: varchar(255) - not nullable
- classoid: int - not nullable
- customer: varchar(255) - not nullable
- description: text - not nullable
- displayName: varchar(255) - not nullable
- hasUsers: varchar(10) - not nullable
- internal: varchar(255) - not nullable
- name: varchar(255) - not nullable
- owner: varchar(10) - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable
- vendor: varchar(255) - not nullable

### scSiteWorkOrderType
- oid: bigint - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- workOrderType_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- manufacturingJob_id: int - not nullable

### scSnapshotConfiguration
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: text - not nullable
- locationType: varchar(255) - not nullable
- name: varchar(255) - not nullable
- owner_id: int - not nullable
- schedule_id: int - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable

### scSnapshotLevel
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- configuration_id: int - not nullable
- sequence: int - not nullable
- type: varchar(255) - not nullable

### scSnapshotSchedule
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: text - not nullable
- frequency_id: int - not nullable
- name: varchar(255) - not nullable
- scheduler_id: int - not nullable
- status: varchar(255) - not nullable

### scSnapshotSession
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- completedDate: datetime - not nullable
- configuration_id: int - not nullable
- creationDate: datetime - not nullable
- itemCount: int - not nullable
- status: varchar(255) - not nullable
- user_id: int - not nullable

### scStandbyLPN
- oid: int - not nullable (Primary Key)
- lpn: varchar(255) - not nullable (Foreign Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- containerCode: varchar(255) - not nullable
- creationTime: datetime - not nullable
- expiryDate: datetime - not nullable
- filler: varchar(255) - not nullable
- lotNo: varchar(255) - not nullable
- materialMaster_id: int - not nullable
- palletNo: varchar(255) - not nullable
- productionDate: datetime - not nullable
- productionRun: varchar(255) - not nullable
- productionSite_id: int - not nullable
- quantity: bigint - not nullable
- receptionDate: datetime - not nullable
- uoi_id: int - not nullable
- weight: decimal(19,2) - not nullable

### scStandbyLPNToSOLI
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- quantity: bigint - not nullable
- soli: int - not nullable
- standbylpn_id: int - not nullable
- uoi_id: int - not nullable

### scStockCountSchedule
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: text - not nullable
- frequency_id: int - not nullable
- name: varchar(255) - not nullable
- scheduler_id: int - not nullable
- status: varchar(255) - not nullable

### scSubAssembly
- oid: int - not nullable (Primary Key)
- assembly_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- item_id: int - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable

### scTransportEquipment
- oid: int - not nullable (Primary Key)
- load_id: int - not nullable (Foreign Key)
- location_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- type_id: int - not nullable (Foreign Key)
- capacity: decimal(19,2) - not nullable
- capacityUsed: decimal(19,2) - not nullable
- classoid: int - not nullable
- currentPKLH_id: int - not nullable
- dimensionUOM_id: int - not nullable
- items: int - not nullable
- lastUsageComment: text - not nullable
- lastUsageDate: datetime - not nullable
- lastUsageMovement_id: int - not nullable
- licenseNo: varchar(255) - not nullable
- maxWeight: decimal(19,2) - not nullable
- parent_id: int - not nullable
- status: varchar(255) - not nullable
- transportEquipment_id: int - not nullable
- usageStatus: varchar(255) - not nullable
- volume: decimal(19,2) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable
- zone_id: int - not nullable

### scTransportEquipmentType
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- capacity: decimal(19,2) - not nullable
- classoid: int - not nullable
- description: text - not nullable
- dimensionUOM_id: int - not nullable
- interiorDepth: decimal(19,2) - not nullable
- interiorHeight: decimal(19,2) - not nullable
- interiorWidth: decimal(19,2) - not nullable
- maxPallets: int - not nullable
- maxWeight: decimal(19,2) - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable

### scUKLI
- oid: int - not nullable (Primary Key)
- mi_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- createdDate: datetime - not nullable
- initialQty: bigint - not nullable
- location_id: int - not nullable
- pkli_id: int - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable
- unpickedDate: datetime - not nullable
- unpickedQty: bigint - not nullable
- uoi_id: int - not nullable
- user_id: int - not nullable

### scUOI
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: text - not nullable
- description_id: int - not nullable
- name: varchar(255) - not nullable
- name_id: int - not nullable
- uom_id: int - not nullable

### scUOIConfig
- oid: int - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- depth: decimal(19,2) - not nullable
- description: varchar(255) - not nullable
- dimensionUOM_id: int - not nullable
- displayName: varchar(255) - not nullable
- handlingMaterial_id: int - not nullable
- height: decimal(19,2) - not nullable
- inactiveDate: varchar(255) - not nullable
- lastUpdated: datetime - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- pickingLayer: int - not nullable
- pickrule: varchar(255) - not nullable
- quantity: bigint - not nullable
- referenceNo: varchar(255) - not nullable
- status: varchar(255) - not nullable
- uoi_id: int - not nullable
- volume: decimal(19,2) - not nullable
- volumetryBinding: varchar(255) - not nullable
- weight: decimal(19,2) - not nullable
- weightUOM_id: int - not nullable
- width: decimal(19,2) - not nullable

### scUOIConfigLocation
- oid: int - not nullable (Primary Key)
- uoiconfig_id: int - not nullable (Foreign Key)
- active: varchar(10) - not nullable
- agropur_movingMaxQty: bigint - not nullable
- agropur_movingMinQty: bigint - not nullable
- allowreslot: varchar(10) - not nullable
- binType_id: int - not nullable
- classoid: int - not nullable
- condition_id: int - not nullable
- inPriority: int - not nullable
- itemTemplateUOIConfigLocation_id: int - not nullable
- lastReplenCount: datetime - not nullable
- location_id: int - not nullable
- manuallyChanged: varchar(10) - not nullable
- maxLocationInZone: int - not nullable
- maxNbDay: int - not nullable
- maxNumberOfLicencePlates: int - not nullable
- maxPickQty: bigint - not nullable
- movingMaxQty: decimal(19,2) - not nullable
- movingMinQty: decimal(19,2) - not nullable
- outPriority: int - not nullable
- owner_id: int - not nullable
- replenCountFrequency: varchar(255) - not nullable
- repQty: bigint - not nullable
- repTresholdQty: bigint - not nullable
- site_id: int - not nullable
- type: varchar(255) - not nullable
- zone_id: int - not nullable

### scUOM
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: varchar(255) - not nullable
- name: varchar(255) - not nullable
- type: varchar(255) - not nullable

### scUnloadingJob
- oid: int - not nullable (Primary Key)
- site_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- siteConfiguration_id: int - not nullable
- status: varchar(255) - not nullable
- unloadingChecklist_id: int - not nullable
- unloadingCondition_id: int - not nullable

### scUserSite
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- site_id: int - not nullable
- user_id: int - not nullable

### scVendorRelation
- oid: int - not nullable (Primary Key)
- receiver_id: int - not nullable (Foreign Key)
- vendor_id: int - not nullable (Foreign Key)
- checklistInbound: int - not nullable
- checklistInboundByItem: int - not nullable
- checklistInboundByLOTNO: int - not nullable
- checklistInboundByReceivingDocument: int - not nullable
- classoid: int - not nullable
- name: varchar(255) - not nullable
- vendorNo: varchar(255) - not nullable

### scWMAsset
- oid: bigint - not nullable (Primary Key)
- map_id: int - not nullable (Foreign Key)
- absPositionX: decimal(19,2) - not nullable
- absPositionY: decimal(19,2) - not nullable
- absPositionZ: decimal(19,2) - not nullable
- absRotationX: decimal(19,2) - not nullable
- absRotationY: decimal(19,2) - not nullable
- absRotationZ: decimal(19,2) - not nullable
- assetClass: varchar(255) - not nullable
- assetKey: char(36) - not nullable
- centerPositionX: decimal(19,2) - not nullable
- centerPositionY: decimal(19,2) - not nullable
- centerPositionZ: decimal(19,2) - not nullable
- classoid: int - not nullable
- color_id: int - not nullable
- depth: decimal(19,2) - not nullable
- floor_id: int - not nullable
- height: decimal(19,2) - not nullable
- name: varchar(255) - not nullable
- parameters: text - not nullable
- parent_id: int - not nullable
- reference_id: int - not nullable
- relPositionX: decimal(19,2) - not nullable
- relPositionY: decimal(19,2) - not nullable
- relPositionZ: decimal(19,2) - not nullable
- rotationX: decimal(19,2) - not nullable
- rotationY: decimal(19,2) - not nullable
- rotationZ: decimal(19,2) - not nullable
- thickness: decimal(19,2) - not nullable
- type_id: int - not nullable
- velocity: int - not nullable
- width: decimal(19,2) - not nullable

### scWMAssetType
- oid: bigint - not nullable (Primary Key)
- assetClass: varchar(255) - not nullable
- assetId: varchar(255) - not nullable
- classoid: int - not nullable
- color_id: int - not nullable
- depth: decimal(19,2) - not nullable
- height: decimal(19,2) - not nullable
- name: varchar(255) - not nullable
- width: decimal(19,2) - not nullable

### scWOH
- oid: int - not nullable (Primary Key)
- actionRequired: text - not nullable
- assembly_id: int - not nullable
- billToCostCenter_id: int - not nullable
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- description: text - not nullable
- duration: int - not nullable
- earliest: datetime - not nullable
- lastAdjustment_id: int - not nullable
- leadingStatus: varchar(255) - not nullable
- materialMaster_id: int - not nullable
- orderClass: varchar(255) - not nullable
- owner_id: int - not nullable
- parent_id: int - not nullable
- percentComplete: varchar(255) - not nullable
- pickTicketNo: varchar(255) - not nullable
- plannedEnd: datetime - not nullable
- plannedStart: datetime - not nullable
- priority: varchar(255) - not nullable
- productionQty: bigint - not nullable
- productionRoute_id: int - not nullable
- productionType: varchar(255) - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- referenceNo: varchar(255) - not nullable
- requester_id: int - not nullable
- requiredDate: datetime - not nullable
- seqChildren: varchar(255) - not nullable
- shippedDate: datetime - not nullable
- shipTo_id: int - not nullable
- slack: int - not nullable
- status: varchar(255) - not nullable
- supplier_id: int - not nullable
- toReceiveQty: bigint - not nullable
- trailingStatus: varchar(255) - not nullable
- type_id: int - not nullable
- unitPrice: varchar(255) - not nullable
- uoi_id: int - not nullable
- womh_id: int - not nullable
- workCenter_id: int - not nullable

### scWOHAdjustment
- oid: bigint - not nullable (Primary Key)
- woh_id: int - not nullable (Foreign Key)
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- eventDate: datetime - not nullable
- leadingStatus: varchar(255) - not nullable
- productionQty: bigint - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- status: varchar(255) - not nullable
- toReceiveQty: bigint - not nullable
- trailingStatus: varchar(255) - not nullable
- type: varchar(255) - not nullable
- uoi_id: int - not nullable
- user_id: int - not nullable

### scWOS
- oid: int - not nullable (Primary Key)
- materialMaster_id: int - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- woh_id: int - not nullable (Foreign Key)
- woms_id: int - not nullable (Foreign Key)
- actionRequired: text - not nullable
- backOrder: varchar(255) - not nullable
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- configurationItem_id: int - not nullable
- dependency: varchar(255) - not nullable
- description: text - not nullable
- duration: int - not nullable
- earliest: datetime - not nullable
- executionDate: datetime - not nullable
- leadingStatus: varchar(255) - not nullable
- manufacturingJob_id: int - not nullable
- outstandingQty: bigint - not nullable
- owner_id: int - not nullable
- percentComplete: varchar(255) - not nullable
- pickTicketNo: varchar(255) - not nullable
- plannedEnd: datetime - not nullable
- plannedStart: datetime - not nullable
- priority: varchar(255) - not nullable
- productionQty: bigint - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- referenceNo: varchar(255) - not nullable
- requester_id: int - not nullable
- requiredDate: datetime - not nullable
- seqChildren: varchar(255) - not nullable
- sequence: varchar(255) - not nullable
- shippedDate: datetime - not nullable
- shipTo_id: int - not nullable
- shipToDepartment_id: int - not nullable
- slack: int - not nullable
- status: varchar(255) - not nullable
- supplier_id: int - not nullable
- toReceiveQty: bigint - not nullable
- trailingStatus: varchar(255) - not nullable
- unitPrice: decimal(19,2) - not nullable
- uoi_id: int - not nullable
- workCenter_id: int - not nullable
- workCenterType_id: int - not nullable

### scWOSAdjustment
- oid: bigint - not nullable (Primary Key)
- parent_id: int - not nullable (Foreign Key)
- wos_id: int - not nullable (Foreign Key)
- cancelledQty: bigint - not nullable
- classoid: int - not nullable
- leadingStatus: varchar(255) - not nullable
- outstandingQty: bigint - not nullable
- productionQty: bigint - not nullable
- quantity: bigint - not nullable
- receivedQty: bigint - not nullable
- status: varchar(255) - not nullable
- toReceiveQty: bigint - not nullable
- trailingStatus: varchar(255) - not nullable
- uoi_id: int - not nullable

### scWorkCenter
- oid: int - not nullable (Primary Key)
- type_id: int - not nullable (Foreign Key)
- zone_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- name: varchar(255) - not nullable
- outBay_id: int - not nullable
- productionBay_id: int - not nullable
- scale_id: int - not nullable
- site_id: int - not nullable
- status: varchar(255) - not nullable

### scWorkCenterPrinter
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- printer_id: int - not nullable
- printerFormat_id: int - not nullable
- printerType_id: int - not nullable
- workCenter_id: int - not nullable

### scWorkCenterType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable

### scWorkOrderType
- oid: int - not nullable (Primary Key)
- cancellationStatus: varchar(255) - not nullable
- classoid: int - not nullable
- consumptionMode: varchar(255) - not nullable
- consumptionPriority: varchar(255) - not nullable
- description: text - not nullable
- inbayValidationMode: varchar(255) - not nullable
- initialStatus: varchar(255) - not nullable
- modificationStatus: varchar(255) - not nullable
- name: varchar(255) - not nullable
- orderClass: varchar(255) - not nullable
- orderCompletion: varchar(255) - not nullable
- orderCreation: varchar(255) - not nullable
- outputProcess: varchar(255) - not nullable
- owner: varchar(255) - not nullable
- productionType: varchar(255) - not nullable
- routeType_id: int - not nullable
- status: varchar(255) - not nullable
- transferCreation: varchar(255) - not nullable
- transferType_id: int - not nullable
- workCenterType_id: int - not nullable

### scWorkcenterLoc
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- location_id: int - not nullable
- type: varchar(255) - not nullable
- workcenter_id: int - not nullable

### scZLocation
- oid: int - not nullable (Primary Key)
- zlocation: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- object_id: int - not nullable
- site_id: int - not nullable

### scZone
- oid: int - not nullable (Primary Key)
- costCenter_id: int - not nullable (Foreign Key)
- gln: varchar(255) - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- site_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- allowMixAttributes: varchar(10) - not nullable
- allowMixExpiryDate: varchar(10) - not nullable
- allowMixItems: varchar(10) - not nullable
- allowMixLotNo: varchar(10) - not nullable
- allowMixMode: varchar(255) - not nullable
- allowMixOwners: varchar(10) - not nullable
- classoid: int - not nullable
- description: varchar(255) - not nullable
- enableAgingReport: varchar(10) - not nullable
- replenishmentJob_id: int - not nullable
- type_id: int - not nullable

### scZoneRelation
- oid: bigint - not nullable (Primary Key)
- child_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- parent_id: int - not nullable
- relationType: varchar(255) - not nullable
- sequence: int - not nullable

### smAPIService
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smAPIServiceInstance
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- instance_id: int - not nullable
- module_id: int - not nullable
- system_id: int - not nullable
- systemAccount_id: int - not nullable
- systemInstance_id: int - not nullable

### smAPIServiceInterface
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- exporter_id: int - not nullable
- interfaceExporter_id: int - not nullable
- module_id: int - not nullable
- scriptText: text - not nullable
- scriptType: varchar(255) - not nullable
- service_id: int - not nullable
- system_id: int - not nullable

### smAPIServiceParameter
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- direction: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- required: varchar(10) - not nullable
- service_id: int - not nullable
- type_id: int - not nullable

### smAPIServiceSystem
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- system_id: int - not nullable
- type_id: int - not nullable

### smAPIServiceType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smActionEvent
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- active: varchar(10) - not nullable
- classoid: int - not nullable
- code: varchar(255) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- message_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- reference_id: int - not nullable
- sequence: int - not nullable
- type_id: int - not nullable

### smActionEventType
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- classoid: int - not nullable
- code: varchar(255) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- message_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- reference_id: int - not nullable

### smActionExecutionPool
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- pool_id: int - not nullable
- priority: int - not nullable

### smActionInterceptor
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable (Foreign Key)
- active: varchar(10) - not nullable
- asyncMode: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- reference_id: int - not nullable
- referenceType_id: int - not nullable
- sequence: int - not nullable

### smActionScript
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- classoid: int - not nullable
- content: mediumtext - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- language_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- scriptContext_id: int - not nullable
- status: varchar(255) - not nullable

### smActionValidator
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable (Foreign Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable

### smAllowedLookupCategory
- oid: int - not nullable (Primary Key)
- category_id: int - not nullable
- classoid: int - not nullable
- context_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- status: varchar(255) - not nullable

### smAllowedLookupItem
- oid: int - not nullable (Primary Key)
- category_id: int - not nullable
- classoid: int - not nullable
- item_id: int - not nullable
- module_id: int - not nullable
- sequence: int - not nullable
- status: varchar(255) - not nullable

### smAppProfileEndpoint
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- module_id: int - not nullable
- type_id: int - not nullable
- userEndpoint_id: int - not nullable

### smAppProfileEndpointType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultEndpoint_id: int - not nullable
- endpointType_id: int - not nullable
- module_id: int - not nullable
- profile_id: int - not nullable

### smAppService
- oid: int - not nullable (Primary Key)
- autoStart: varchar(10) - not nullable
- canPause: varchar(10) - not nullable
- canRestart: varchar(10) - not nullable
- canStop: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- sequence: int - not nullable
- type: varchar(255) - not nullable
- type_id: int - not nullable

### smAppServiceMode
- oid: int - not nullable (Primary Key)
- applicationMode_id: int - not nullable
- classoid: int - not nullable
- limited: varchar(10) - not nullable
- module_id: int - not nullable
- operationMode_id: int - not nullable
- sequence: int - not nullable
- service_id: int - not nullable

### smApplication
- oid: int - not nullable (Primary Key)
- authenticationSystem_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- notes_id: int - not nullable

### smApplicationInstance
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- application_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- instanceModule_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- profile_id: int - not nullable
- serverGroup_id: int - not nullable
- status: varchar(255) - not nullable

### smApplicationMode
- oid: int - not nullable (Primary Key)
- applicationModel_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- operationMode_id: int - not nullable

### smApplicationProfile
- oid: int - not nullable (Primary Key)
- application_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smApplicationServerGroup
- oid: int - not nullable (Primary Key)
- applicationModel_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smArchivingStrategy
- oid: int - not nullable (Primary Key)
- archiveGroup_id: int - not nullable
- classoid: int - not nullable
- dataGroup_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smArchivingStrategyObject
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- strategy_id: int - not nullable

### smAttribute
- oid: int - not nullable (Primary Key)
- column_id: int - not nullable (Foreign Key)
- object_id: int - not nullable (Foreign Key)
- type_id: int - not nullable (Foreign Key)
- chainAttribute_id: int - not nullable
- classoid: int - not nullable
- configurable: varchar(255) - not nullable
- defaultvalue: varchar(255) - not nullable
- description_id: int - not nullable
- dynamic_id: int - not nullable
- eventLogging: varchar(255) - not nullable
- importtype: varchar(255) - not nullable
- insertable: varchar(10) - not nullable
- label_id: int - not nullable
- massUpdatable: varchar(10) - not nullable
- mode: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- notes_id: int - not nullable
- readonly: varchar(10) - not nullable
- related_id: int - not nullable
- relationType: varchar(255) - not nullable
- required: varchar(10) - not nullable
- restrictedValue: varchar(10) - not nullable
- scriptText: text - not nullable
- tagName: varchar(255) - not nullable
- typeColumn_id: int - not nullable
- updatable: varchar(10) - not nullable

### smAttributeOptions
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- value: varchar(255) - not nullable

### smAuthSystemInstance
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- instance_id: int - not nullable
- module_id: int - not nullable
- system_id: int - not nullable

### smAuthenticationSystem
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- domainNames: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- policy_id: int - not nullable
- security_id: int - not nullable
- sessiontype_id: int - not nullable
- type_id: int - not nullable

### smAuthenticationType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- mode: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smBObjectInterface
- oid: int - not nullable (Primary Key)
- object_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- interface_id: int - not nullable
- module_id: int - not nullable

### smBatchAction
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- parameter_id: int - not nullable
- type: varchar(255) - not nullable

### smBatchActionParam
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- attribute_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- parameter_id: int - not nullable

### smBatchAttribute
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- column_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- type_id: int - not nullable

### smBatchConfiguration
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smBatchObject
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- query_id: int - not nullable

### smBusinessObject
- oid: int - not nullable (Primary Key)
- module_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- table_id: int - not nullable (Foreign Key)
- abstractClass: varchar(10) - not nullable
- classoid: int - not nullable
- deletable: varchar(10) - not nullable
- description_id: int - not nullable
- displayAttribute_id: int - not nullable
- displaydesc_id: int - not nullable
- displayField: varchar(255) - not nullable
- importable: varchar(255) - not nullable
- label_id: int - not nullable
- notes_id: int - not nullable
- query_id: int - not nullable

### smCache
- oid: int - not nullable (Primary Key)
- type_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- configuration_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- loadingMode: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable

### smCacheConfiguration
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- strategy_id: int - not nullable
- type_id: int - not nullable

### smCacheItem
- oid: int - not nullable (Primary Key)
- cache_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- loadingMode: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smCacheableType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- strategy_id: int - not nullable
- type_id: int - not nullable

### smCachingStrategy
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- configuration_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smCachingStrategyInstance
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- configuration_id: int - not nullable
- instance_id: int - not nullable
- module_id: int - not nullable
- strategy_id: int - not nullable

### smCategory
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- help_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- protectionMode: varchar(255) - not nullable
- referenceId: char(36) - not nullable
- subtype_id: int - not nullable
- type: varchar(255) - not nullable
- type_id: int - not nullable
- versionNo: int - not nullable

### smChainObject
- oid: int - not nullable (Primary Key)
- chain_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- param_id: int - not nullable
- virtual: varchar(10) - not nullable

### smCodeTemplate
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- filename: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- template: text - not nullable

### smCodeTemplateObject
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- codeTemplate_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- parent_id: int - not nullable

### smColor
- oid: int - not nullable (Primary Key)
- baseColor: varchar(255) - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- code: varchar(255) - not nullable
- module_id: int - not nullable
- shade: varchar(255) - not nullable

### smColumnTemplate
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable
- tableType_id: int - not nullable
- type_id: int - not nullable
- visible: varchar(10) - not nullable

### smColumnType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smComProtocol
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type: varchar(255) - not nullable

### smConfiguredSystem
- oid: int - not nullable (Primary Key)
- applicationModel_id: int - not nullable
- classoid: int - not nullable
- description: text - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- system_id: int - not nullable

### smContext
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable

### smContextAction
- oid: int - not nullable (Primary Key)
- context_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- contextObject_id: int - not nullable
- createObjectRequest: varchar(10) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- language_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- objectDescription_id: int - not nullable
- objectLabel_id: int - not nullable
- objectLabelMode: varchar(255) - not nullable
- objectName: varchar(255) - not nullable
- result_id: int - not nullable
- scriptContextAction_id: int - not nullable
- service_id: int - not nullable

### smContextActionParam
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- derivationScript: text - not nullable
- description_id: int - not nullable
- direction: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- required: varchar(10) - not nullable
- scriptAccess: varchar(255) - not nullable
- scriptName: varchar(255) - not nullable
- type_id: int - not nullable

### smContextClass
- oid: int - not nullable (Primary Key)
- class_id: int - not nullable
- classoid: int - not nullable
- context_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- paramAttribute_id: int - not nullable
- paramClass_id: int - not nullable

### smContextError
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- classoid: int - not nullable
- context_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smCron
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- frequency: varchar(255) - not nullable
- frequency_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- reference_id: int - not nullable
- scheduler_id: int - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable

### smCronFrequency
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- frequency: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smCronScheduler
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- delayedStart: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- mode: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- priority: varchar(255) - not nullable
- threadCount: int - not nullable
- type: varchar(255) - not nullable

### smCurrentModule
- oid: bigint - not nullable (Primary Key)
- buildDate: datetime - not nullable
- buildNo: int - not nullable
- classoid: int - not nullable
- lastModified: char(36) - not nullable
- module_id: int - not nullable
- moduleVersion_id: int - not nullable
- name: varchar(255) - not nullable
- status: varchar(255) - not nullable
- timestamp: varchar(255) - not nullable
- version: varchar(255) - not nullable

### smCustomAttribute
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- datasource_id: int - not nullable
- defaultValue: varchar(255) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- type_id: int - not nullable

### smCustomAttributeValue
- oid: int - not nullable (Primary Key)
- object_id: int - not nullable (Foreign Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- custom_id: int - not nullable
- module_id: int - not nullable
- value: text - not nullable

### smCustomizedObject
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- customizationCount: int - not nullable
- description_id: int - not nullable
- feature_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- source_id: int - not nullable
- status: varchar(255) - not nullable
- type_id: int - not nullable

### smDataGroup
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- datastore_id: int - not nullable
- defaultGroup: varchar(10) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- location_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smDataGroupLocation
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- dataGroup_id: int - not nullable
- datastoreConf_id: int - not nullable
- location_id: int - not nullable
- module_id: int - not nullable
- partition_id: int - not nullable

### smDataGroupType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDataMask
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- format: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smDataMaskType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDataMaskTypeParam
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- dataMaskType_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smDataPartition
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- dataGroup_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- partitionNo: int - not nullable
- type_id: int - not nullable

### smDataPartitionType
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable

### smDataTypeColumn
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- columntype_id: int - not nullable
- datatype_id: int - not nullable
- module_id: int - not nullable

### smDatastore
- oid: int - not nullable (Primary Key)
- applicationModel_id: int - not nullable
- classoid: int - not nullable
- defaultAPI_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smDatastoreAPI
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- datastore_id: int - not nullable
- module_id: int - not nullable
- persistenceAPI_id: int - not nullable

### smDatastoreConf
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- datastore_id: int - not nullable
- datastoreAPI_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- storageEngine_id: int - not nullable

### smDatastoreInstance
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- datastore_id: int - not nullable
- datastoreConf_id: int - not nullable
- instance_id: int - not nullable
- module_id: int - not nullable

### smDatastoreLocation
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- datastoreConf_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDatastorePartitionType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- datastoreConf_id: int - not nullable
- module_id: int - not nullable
- partitionType_id: int - not nullable

### smDatePreset
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- parent_id: int - not nullable
- relativeDate_id: int - not nullable
- sequence: int - not nullable

### smDeviceModel
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- protocol_id: int - not nullable
- type_id: int - not nullable

### smDeviceProtocol
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDiagnostic
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- unit_id: int - not nullable

### smDiagnosticGranularity
- oid: int - not nullable (Primary Key)
- diagnostic_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable

### smDiagnosticInstance
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- diagnostic_id: int - not nullable
- diagnosticGroup_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- overrideThreshold: varchar(10) - not nullable

### smDiagnosticInstanceCron
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- cron_id: int - not nullable
- instance_id: int - not nullable
- module_id: int - not nullable
- sequence: int - not nullable

### smDiagnosticIssueType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultResolution_id: int - not nullable
- description_id: int - not nullable
- diagnostic_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- resolutionMode: varchar(255) - not nullable

### smDiagnosticIssueTypeParam
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- issueType_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smDiagnosticResolution
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- issueType_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDiagnosticThreshold
- oid: int - not nullable (Primary Key)
- archiveResult: varchar(10) - not nullable
- classoid: int - not nullable
- diagnostic_id: int - not nullable
- instance_id: int - not nullable
- maximumValue: decimal(19,2) - not nullable
- message_id: int - not nullable
- messageLevel_id: int - not nullable
- minimumValue: decimal(19,2) - not nullable
- module_id: int - not nullable

### smDiagnosticUnit
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- symbol: varchar(255) - not nullable

### smDictionary
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDictionaryItem
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- dictionary_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDocSectionType
- oid: int - not nullable (Primary Key)
- bottomleft_id: int - not nullable
- bottomright_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- language_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- orientation: varchar(255) - not nullable
- topleft_id: int - not nullable
- topright_id: int - not nullable

### smDocStylesheet
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- document_id: int - not nullable
- format_id: int - not nullable
- module_id: int - not nullable
- stylesheet: text - not nullable

### smDocTemplateType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- coverPage_id: int - not nullable
- description_id: int - not nullable
- folder_id: int - not nullable
- format_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- repository_id: int - not nullable
- tableOfContents_id: int - not nullable

### smDocument
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultAttribute_id: int - not nullable
- description_id: int - not nullable
- fileName: varchar(255) - not nullable
- filetype_id: int - not nullable
- folder_id: int - not nullable
- label_id: int - not nullable
- language: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- owner_id: int - not nullable
- parent_id: int - not nullable
- referenceId: char(36) - not nullable
- repository_id: int - not nullable
- status: varchar(255) - not nullable
- title_id: int - not nullable
- type_id: int - not nullable
- version: int - not nullable

### smDocumentAttribute
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultValue: varchar(255) - not nullable
- description_id: int - not nullable
- document_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- section_id: int - not nullable
- type_id: int - not nullable

### smDocumentDef
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- delimiter: varchar(255) - not nullable
- description_id: int - not nullable
- docName: varchar(255) - not nullable
- docSchema: text - not nullable
- enclosure: varchar(255) - not nullable
- encoding: varchar(255) - not nullable
- example: text - not nullable
- headerType: varchar(255) - not nullable
- label_id: int - not nullable
- lineSeparator: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- namespace_id: int - not nullable
- notes_id: int - not nullable
- owner_id: int - not nullable
- query_id: int - not nullable
- reference_id: int - not nullable
- status: varchar(255) - not nullable
- strictMode: varchar(255) - not nullable
- type_id: int - not nullable

### smDocumentDefChild
- oid: int - not nullable (Primary Key)
- document_id: int - not nullable (Foreign Key)
- appField: varchar(255) - not nullable
- classoid: int - not nullable
- column_id: int - not nullable
- defaultValue: varchar(255) - not nullable
- description_id: int - not nullable
- exampleValue: varchar(255) - not nullable
- hostField: varchar(255) - not nullable
- label_id: int - not nullable
- maxOccurrence: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- namespace_id: int - not nullable
- noderef_id: int - not nullable
- notes_id: int - not nullable
- parent_id: int - not nullable
- path: text - not nullable
- reference_id: int - not nullable
- required: varchar(10) - not nullable
- sequence: int - not nullable
- type: varchar(255) - not nullable
- visible: varchar(10) - not nullable

### smDocumentDefChildRel
- oid: int - not nullable (Primary Key)
- child_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- value: text - not nullable

### smDocumentDefRel
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- document_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- type: varchar(255) - not nullable
- version: varchar(255) - not nullable

### smDocumentDefType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- format: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type: varchar(255) - not nullable

### smDocumentFormat
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- filetype_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDocumentLanguage
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smDocumentSection
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- docref_id: int - not nullable
- document_id: int - not nullable
- hidden: varchar(10) - not nullable
- label_id: int - not nullable
- language_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- notes_id: int - not nullable
- numberingMode: varchar(255) - not nullable
- orientation: varchar(255) - not nullable
- pageBreak: varchar(255) - not nullable
- parent_id: int - not nullable
- readOnly: varchar(10) - not nullable
- section: varchar(255) - not nullable
- sectionref_id: int - not nullable
- sequence: int - not nullable
- type_id: int - not nullable

### smDocumentVarType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultValue_id: int - not nullable
- description_id: int - not nullable
- document_id: int - not nullable
- format_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smEmailSettings
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- encryption: varchar(255) - not nullable
- hostName: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- port: int - not nullable

### smEndpointTypeRecipientType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- endpointType_id: int - not nullable
- module_id: int - not nullable
- recipientType_id: int - not nullable

### smEnumerationGroupItem
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- enumerationGroup_id: int - not nullable
- item_id: int - not nullable
- module_id: int - not nullable

### smEnumerationValue
- oid: int - not nullable (Primary Key)
- enumeration_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable
- value: varchar(255) - not nullable

### smExecutionPool
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- cancellation: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- interruptible: varchar(10) - not nullable
- label_id: int - not nullable
- maxItems: int - not nullable
- maxItemsPerGroup: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- scheduler_id: int - not nullable
- strategy_id: int - not nullable
- type_id: int - not nullable

### smExecutionPoolType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smExecutionPoolTypeAction
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- type_id: int - not nullable

### smExportField
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- trigger_id: int - not nullable
- type_id: int - not nullable

### smExportTrigger
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- defaultdoc_id: int - not nullable
- definition_id: int - not nullable
- description_id: int - not nullable
- document_id: int - not nullable
- example: text - not nullable
- importable: varchar(10) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- notes_id: int - not nullable
- object_id: int - not nullable
- query: text - not nullable
- queryType: varchar(255) - not nullable
- response_id: int - not nullable
- type_id: int - not nullable

### smExporterDestination
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- creationMode: varchar(255) - not nullable
- defaultResponse: varchar(255) - not nullable
- destination_id: int - not nullable
- exporter_id: int - not nullable
- exporterIndex: int - not nullable
- interface_id: int - not nullable
- module_id: int - not nullable
- msgLogging: varchar(255) - not nullable
- name: varchar(255) - not nullable
- system_id: int - not nullable

### smExporterTrigger
- oid: int - not nullable (Primary Key)
- actionEvent_id: int - not nullable (Foreign Key)
- exporter_id: int - not nullable (Foreign Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- reference_id: int - not nullable
- sequence: int - not nullable

### smExternalSystem
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- template: varchar(10) - not nullable
- template_id: int - not nullable
- type_id: int - not nullable

### smFeatureTactic
- oid: int - not nullable (Primary Key)
- feature_id: int - not nullable (Foreign Key)
- tactic_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- referenceId: char(36) - not nullable
- sequence: int - not nullable
- useCase_id: int - not nullable
- versionNo: int - not nullable

### smFeatureType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- referenceId: char(36) - not nullable
- versionNo: int - not nullable

### smFileDocType
- oid: int - not nullable (Primary Key)
- authentication: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- folder_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- repository_id: int - not nullable

### smFileDocTypeRelation
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- creationMode: varchar(255) - not nullable
- description_id: int - not nullable
- folder_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- repository_id: int - not nullable
- type_id: int - not nullable

### smFileType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- extension: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smHelpDocument
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- fileType_id: int - not nullable
- folder_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- owner_id: int - not nullable
- report_id: int - not nullable
- reportRelation_id: int - not nullable
- repository_id: int - not nullable
- template_id: int - not nullable

### smHelpTopic
- oid: int - not nullable (Primary Key)
- document_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- docref_id: int - not nullable
- hidden: varchar(10) - not nullable
- keywords: varchar(255) - not nullable
- label_id: int - not nullable
- language_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- notes_id: int - not nullable
- numberingMode: varchar(255) - not nullable
- orientation: varchar(255) - not nullable
- pageBreak: varchar(255) - not nullable
- section: varchar(255) - not nullable
- sequence: int - not nullable
- type_id: int - not nullable

### smImporter
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- defaultdoc_id: int - not nullable
- description_id: int - not nullable
- document_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- notes_id: int - not nullable
- object_id: int - not nullable
- status: text - not nullable
- type: varchar(255) - not nullable
- type_id: int - not nullable

### smImporterRel
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- document_id: int - not nullable
- importer_id: int - not nullable
- module_id: int - not nullable
- sequence: int - not nullable
- template_id: int - not nullable

### smImporterSource
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- config_id: int - not nullable
- exporter_id: int - not nullable
- importer_id: int - not nullable
- importerIndex: int - not nullable
- interface_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- system_id: int - not nullable

### smIndex
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- object_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description: text - not nullable
- module_id: int - not nullable
- uniqueIdx: varchar(10) - not nullable
- validation: varchar(255) - not nullable

### smIndexAttribute
- oid: int - not nullable (Primary Key)
- index_id: int - not nullable (Foreign Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- indexPosition: int - not nullable
- label_id: int - not nullable
- methodName: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- optional: varchar(10) - not nullable
- type_id: int - not nullable

### smInterfaceInstance
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- interface_id: int - not nullable
- module_id: int - not nullable
- system_id: int - not nullable

### smInterfaceTrigger
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- interface_id: int - not nullable
- module_id: int - not nullable
- notes_id: int - not nullable
- status: varchar(255) - not nullable
- trigger_id: int - not nullable

### smKPI
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- filters: text - not nullable
- icon: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- script: text - not nullable
- sequence: int - not nullable

### smKeyGenerator
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smLicense
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- licenseKey: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smLicenseObject
- oid: int - not nullable (Primary Key)
- access: varchar(255) - not nullable
- classoid: int - not nullable
- license_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- parent_id: int - not nullable

### smLocaleAttribute
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type: varchar(255) - not nullable

### smLocalizableItem
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable (Foreign Key)
- owner_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- module_id: int - not nullable
- readonly: varchar(10) - not nullable

### smLocalizableValue
- oid: int - not nullable (Primary Key)
- localizable_id: int - not nullable (Foreign Key)
- autotranslated: varchar(10) - not nullable
- classoid: int - not nullable
- language: varchar(255) - not nullable
- message: mediumtext - not nullable
- module_id: int - not nullable

### smLogger
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- user_id: int - not nullable

### smLookupCategory
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable

### smLookupCategoryRel
- oid: int - not nullable (Primary Key)
- child_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- parent_id: int - not nullable

### smLookupContext
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smLookupContextParam
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- context_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smLookupItem
- oid: int - not nullable (Primary Key)
- category_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- status: varchar(255) - not nullable

### smMessage
- oid: int - not nullable (Primary Key)
- messageGroup_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- code: int - not nullable
- description_id: int - not nullable
- error_id: int - not nullable
- hasParameters: varchar(10) - not nullable
- label_id: int - not nullable
- level_id: int - not nullable
- message_id: int - not nullable
- module_id: int - not nullable
- msgType: varchar(255) - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- title_id: int - not nullable
- type_id: int - not nullable

### smMessageCategory
- oid: int - not nullable (Primary Key)
- asyncMode: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- format_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smMessageCategoryRecipientType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- messageCategory_id: int - not nullable
- module_id: int - not nullable
- recipientType_id: int - not nullable

### smMessageEndpoint
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultEndpoint: varchar(10) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- persistence: varchar(255) - not nullable
- type_id: int - not nullable

### smMessageEndpointInstance
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- endpoint_id: int - not nullable
- instance_id: int - not nullable
- module_id: int - not nullable

### smMessageEndpointSubscription
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- endpoint_id: int - not nullable
- module_id: int - not nullable
- subscriptionGroup_id: int - not nullable

### smMessageEndpointType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smMessageFormat
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- message_id: int - not nullable
- module_id: int - not nullable
- type_id: int - not nullable

### smMessageFormatType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- filetype_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smMessageGroup
- oid: int - not nullable (Primary Key)
- category_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- owner_id: int - not nullable
- type_id: int - not nullable

### smMessageLevel
- oid: int - not nullable (Primary Key)
- action: varchar(255) - not nullable
- category_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- priority: int - not nullable

### smMessageParam
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultValue: varchar(255) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- message_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- required: varchar(10) - not nullable
- sequence: int - not nullable
- type_id: int - not nullable

### smMessageRecipientAccount
- oid: int - not nullable (Primary Key)
- accountName: varchar(255) - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- recipient_id: int - not nullable
- type_id: int - not nullable

### smMessageRecipientType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable

### smMessageSubscription
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- message_id: int - not nullable
- messageGroup_id: int - not nullable
- module_id: int - not nullable
- subscriptionGroup_id: int - not nullable

### smMessageSubscriptionGroup
- oid: int - not nullable (Primary Key)
- category_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- level_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- recipient_id: int - not nullable
- recipientType_id: int - not nullable

### smMessageSubscriptionRecipient
- oid: int - not nullable (Primary Key)
- account_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- subscriptionGroup_id: int - not nullable

### smMessageType
- oid: int - not nullable (Primary Key)
- category: varchar(255) - not nullable
- category_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- priority: int - not nullable

### smMigrationScript
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- required: varchar(10) - not nullable
- scriptText: text - not nullable
- scriptType: varchar(255) - not nullable
- sequence: int - not nullable
- triggerName: varchar(255) - not nullable
- version_id: int - not nullable

### smMimeType
- oid: int - not nullable (Primary Key)
- baseType: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- subType: varchar(255) - not nullable

### smModule
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- lastImported: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- package: varchar(255) - not nullable
- range_start: int - not nullable
- range_stop: int - not nullable
- readonly: varchar(10) - not nullable
- runtime: varchar(10) - not nullable
- type: varchar(255) - not nullable
- version_id: int - not nullable

### smModuleDependency
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- module_id: int - not nullable
- parent_id: int - not nullable

### smModuleLibrary
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: text - not nullable
- license: varchar(255) - not nullable
- licenseURL: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- organization: varchar(255) - not nullable
- parent_id: int - not nullable
- revision: varchar(255) - not nullable

### smModuleRecordableGroup
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- recordableGroup_id: int - not nullable

### smModuleVersion
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- module_id: int - not nullable
- sequence: int - not nullable
- version: varchar(255) - not nullable

### smObjectAPIServiceType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- type_id: int - not nullable

### smObjectCategory
- oid: int - not nullable (Primary Key)
- category_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable

### smObjectContext
- oid: int - not nullable (Primary Key)
- contextClass_id: int - not nullable (Foreign Key)
- object_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- context_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smObjectContextAction
- oid: int - not nullable (Primary Key)
- context_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- action_id: int - not nullable
- className: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- executionMode: varchar(255) - not nullable
- executionPool_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- script_id: int - not nullable

### smObjectGroup
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable

### smObjectGroupItem
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- item_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- objectGroup_id: int - not nullable
- sequence: int - not nullable

### smObjectLogger
- oid: int - not nullable (Primary Key)
- object_id: int - not nullable (Foreign Key)
- objectGroup_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smObjectParameter
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- direction: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- objectContext_id: int - not nullable
- sequence: int - not nullable
- type_id: int - not nullable

### smOperationMode
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smParameter
- oid: int - not nullable (Primary Key)
- service_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- defaultValue: varchar(255) - not nullable
- description_id: int - not nullable
- displayOrder: int - not nullable
- label_id: int - not nullable
- methodName: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- required: varchar(10) - not nullable
- type_id: int - not nullable

### smPasswordPolicy
- oid: int - not nullable (Primary Key)
- changeInitialPassword: varchar(10) - not nullable
- classoid: int - not nullable
- daysBeforeExpiry: int - not nullable
- description_id: int - not nullable
- encoding: varchar(255) - not nullable
- generationMode: varchar(255) - not nullable
- hashingAlgorithm: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- status: varchar(255) - not nullable
- type_id: int - not nullable

### smPasswordPolicyType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smPermissionType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- objectGroup_id: int - not nullable

### smPersistedColumn
- oid: int - not nullable (Primary Key)
- table_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- dbType: varchar(255) - not nullable
- description: text - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable
- template_id: int - not nullable
- type_id: int - not nullable

### smPersistedIndex
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description: varchar(255) - not nullable
- idxFillFactor: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- table_id: int - not nullable
- uniqueIndex: varchar(10) - not nullable

### smPersistedIndexCol
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- column_id: int - not nullable
- columnOrder: int - not nullable
- index_id: int - not nullable
- module_id: int - not nullable

### smPersistedTable
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- type_id: int - not nullable (Foreign Key)
- archivable: varchar(10) - not nullable
- classoid: int - not nullable
- dataGroup_id: int - not nullable
- datastore_id: int - not nullable
- description: text - not nullable
- incrementNo: int - not nullable
- module_id: int - not nullable
- partitionType_id: int - not nullable
- version_id: int - not nullable

### smPlatformLanguage
- classoid: int - not nullable
- language_id: int - not nullable
- module_id: int - not nullable
- oid: int - not nullable
- platform_id: int - not nullable

### smPrinterFormat
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- printerType_id: int - not nullable

### smPrinterType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smProcVar
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- initialvalue: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- path: varchar(255) - not nullable
- process_id: int - not nullable
- type_id: int - not nullable

### smProcess
- oid: int - not nullable (Primary Key)
- category: varchar(255) - not nullable
- classoid: int - not nullable
- code: varchar(255) - not nullable
- inputMode: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- outputMode: varchar(255) - not nullable
- parent_id: int - not nullable
- processType_id: int - not nullable
- purpose_id: int - not nullable
- state_id: int - not nullable
- type: varchar(255) - not nullable

### smProcessAttribute
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- process_id: int - not nullable
- value: varchar(255) - not nullable

### smProcessType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smProfiler
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- context_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- level: varchar(255) - not nullable
- maxTime: int - not nullable
- minimumLevel_id: int - not nullable
- minTime: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- printStack: varchar(255) - not nullable
- type_id: int - not nullable
- verbosity: varchar(255) - not nullable

### smProfilerFilter
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- context_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- profiler_id: int - not nullable
- type_id: int - not nullable

### smProfilerFilterType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smProfilerLevel
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- message_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- profiler_id: int - not nullable
- type_id: int - not nullable
- verbosity: varchar(255) - not nullable

### smProfilerType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smProfilerTypeLevel
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- message_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable
- type_id: int - not nullable

### smQuery
- oid: int - not nullable (Primary Key)
- baseQuery_id: int - not nullable
- classoid: int - not nullable
- defaultSort_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- parent_id: int - not nullable
- soloqlObject_id: int - not nullable

### smQueryElement
- oid: int - not nullable (Primary Key)
- query_id: int - not nullable (Foreign Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- displayMode: varchar(255) - not nullable
- function_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- relatedAttribute_id: int - not nullable
- relatedObject_id: int - not nullable
- relation: varchar(255) - not nullable
- required: varchar(10) - not nullable
- sequence: int - not nullable
- type_id: int - not nullable
- value: text - not nullable

### smQueryFilter
- oid: int - not nullable (Primary Key)
- query_id: int - not nullable (Foreign Key)
- attribute_id: int - not nullable
- attributeValue: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- operator: varchar(255) - not nullable
- required: varchar(10) - not nullable
- value: text - not nullable
- widget_id: int - not nullable

### smQuerySort
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- query_id: int - not nullable

### smQuerySortColumn
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- column_id: int - not nullable
- module_id: int - not nullable
- parent_id: int - not nullable
- sequence: int - not nullable
- sortMode: varchar(255) - not nullable

### smRecordableGroup
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smRecordableObject
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- group_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- sequence: int - not nullable

### smRelativeDate
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- endDate: varchar(255) - not nullable
- endValue: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- startDate: varchar(255) - not nullable
- startValue: int - not nullable
- timescale: varchar(255) - not nullable

### smReport
- oid: int - not nullable (Primary Key)
- parent_id: int - not nullable (Foreign Key)
- archivable: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- folder_id: int - not nullable
- format_id: int - not nullable
- group_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- owner_id: int - not nullable
- reportFormat_id: int - not nullable
- repository_id: int - not nullable
- type_id: int - not nullable

### smReportAttribute
- oid: int - not nullable (Primary Key)
- report_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- defaultvalue: varchar(255) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- required: varchar(10) - not nullable
- type_id: int - not nullable

### smReportFormat
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- filetype_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- printerType_id: int - not nullable
- type_id: int - not nullable

### smReportRelation
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- creationMode: varchar(255) - not nullable
- description_id: int - not nullable
- folder_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- report_id: int - not nullable
- reportInstance_id: int - not nullable
- repository_id: int - not nullable
- versioningMode: varchar(255) - not nullable

### smReportType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- format_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- printerType_id: int - not nullable

### smRepository
- oid: int - not nullable (Primary Key)
- category_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- location_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smRepositoryCategory
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smRepositoryLocation
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultLocation: varchar(10) - not nullable
- mode: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- repository_id: int - not nullable
- sequence: int - not nullable
- status: varchar(255) - not nullable
- type_id: int - not nullable

### smRepositoryType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- externalURL: varchar(10) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smRole
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- externalName: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- userType_id: int - not nullable

### smRoleObject
- oid: int - not nullable (Primary Key)
- access: varchar(255) - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- parent_id: int - not nullable
- role_id: int - not nullable
- securityRight_id: int - not nullable
- type_id: int - not nullable

### smScript
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- module_id: int - not nullable
- object_id: int - not nullable
- scriptText: text - not nullable
- sequence: int - not nullable
- triggerEvent: varchar(255) - not nullable
- type: varchar(255) - not nullable

### smScriptContext
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smScriptContextAction
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- classoid: int - not nullable
- initialContent: text - not nullable
- module_id: int - not nullable
- returnParam_id: int - not nullable
- script_id: int - not nullable

### smScriptLanguage
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- language_id: int - not nullable
- module_id: int - not nullable
- scriptContext_id: int - not nullable
- status: varchar(255) - not nullable

### smScriptingLang
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type: varchar(255) - not nullable

### smSecret
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- password: varchar(255) - not nullable
- type: varchar(255) - not nullable
- username: varchar(255) - not nullable

### smSecurableType
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- parent_id: int - not nullable
- securityRight_id: int - not nullable

### smSecurityPolicy
- oid: int - not nullable (Primary Key)
- attemptsBeforeLock: int - not nullable
- auditMode: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smSecurityRight
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- securableType_id: int - not nullable
- sequence: int - not nullable
- type: varchar(255) - not nullable

### smServerConnectorType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- defaultPort: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- protocol_id: int - not nullable

### smServerEndpoint
- oid: int - not nullable (Primary Key)
- authentication: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- serverProtocol_id: int - not nullable
- type_id: int - not nullable
- userEndpointType_id: int - not nullable

### smServerEndpointAction
- oid: int - not nullable (Primary Key)
- action_id: int - not nullable
- authentication: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- endpoint_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smServerEndpointType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- protocol_id: int - not nullable

### smService
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- category: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- index_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- returntype_id: int - not nullable

### smSessionType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- loggingMode: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- stateless: varchar(10) - not nullable
- timeout: int - not nullable

### smSoloQLFunction
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- example: varchar(255) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smState
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- stateIdentifier: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- defaultState: varchar(10) - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- notes_id: int - not nullable
- passthrough: varchar(10) - not nullable
- process_id: int - not nullable
- purpose_id: int - not nullable
- screenshot_id: int - not nullable
- subProcess_id: int - not nullable
- usage_id: int - not nullable
- voicelabel_id: int - not nullable

### smStorageDataType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- engine_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smStorageEngine
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smSysInterfaceObject
- oid: int - not nullable (Primary Key)
- asynchronous: varchar(10) - not nullable
- classoid: int - not nullable
- cron_id: int - not nullable
- defaultErrorAction: varchar(255) - not nullable
- defaultResponse: varchar(255) - not nullable
- description_id: int - not nullable
- document_id: int - not nullable
- documentMode: varchar(255) - not nullable
- errorCron_id: int - not nullable
- exporterTrigger: varchar(255) - not nullable
- hostErrCron_id: int - not nullable
- interface_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- msgLogging: varchar(255) - not nullable
- name: varchar(255) - not nullable
- notes_id: int - not nullable
- object_id: int - not nullable
- operation_id: int - not nullable
- requestCron_id: int - not nullable
- requestExporter_id: int - not nullable
- response_id: int - not nullable
- retryCount: int - not nullable
- sequence: int - not nullable
- status: varchar(255) - not nullable

### smSystemAccount
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- email: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- secret_id: int - not nullable
- system_id: int - not nullable

### smSystemInstance
- oid: int - not nullable (Primary Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- description: varchar(255) - not nullable
- instance_id: int - not nullable
- module_id: int - not nullable
- system_id: int - not nullable

### smSystemInterface
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- cron_id: int - not nullable
- defaultTrigger: varchar(255) - not nullable
- errorCron_id: int - not nullable
- format_id: int - not nullable
- mode: varchar(255) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- protocol_id: int - not nullable
- system_id: int - not nullable
- type_id: int - not nullable
- validation: varchar(255) - not nullable

### smTableDataGroup
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- dataGroup_id: int - not nullable
- module_id: int - not nullable
- table_id: int - not nullable

### smTableType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- keygen_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- partitioningColumn_id: int - not nullable

### smTactic
- oid: int - not nullable (Primary Key)
- tacticGroup_id: int - not nullable (Foreign Key)
- benefits_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- limitations_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- referenceId: char(36) - not nullable
- sequence: int - not nullable
- versionNo: int - not nullable

### smTacticConfiguration
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable (Foreign Key)
- tactic_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- value: text - not nullable

### smTacticGroup
- oid: int - not nullable (Primary Key)
- applicationModule_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- referenceId: char(36) - not nullable
- versionNo: int - not nullable

### smTransaction
- oid: bigint - not nullable (Primary Key)
- group_id: int - not nullable (Foreign Key)
- timestamp: datetime - not nullable (Foreign Key)
- upgrade_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- globalKey: char(36) - not nullable
- gmodule_id: int - not nullable
- module_id: int - not nullable
- user_id: int - not nullable

### smTransactionField
- oid: bigint - not nullable (Primary Key)
- attribute_id: int - not nullable (Foreign Key)
- object_id: int - not nullable (Foreign Key)
- objectKey: int - not nullable (Foreign Key)
- objectkey_id: int - not nullable (Foreign Key)
- transaction_id: int - not nullable (Foreign Key)
- version_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- fromDisplayValue: varchar(255) - not nullable
- fromValue: mediumtext - not nullable
- operation: varchar(255) - not nullable
- toDisplayValue: varchar(255) - not nullable
- toValue: mediumtext - not nullable

### smTransactionGroup
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- createdDate: datetime - not nullable
- description: text - not nullable
- globalKey: char(36) - not nullable
- gmodule_id: int - not nullable
- keepActive: varchar(10) - not nullable
- lastModified: char(36) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- reference: varchar(255) - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable
- updadeMode: varchar(255) - not nullable
- user_id: int - not nullable

### smTransition
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- state_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- destination_id: int - not nullable
- label_id: int - not nullable
- message_id: int - not nullable
- messageType: varchar(255) - not nullable
- module_id: int - not nullable
- priority: varchar(255) - not nullable
- type: varchar(255) - not nullable
- type_id: int - not nullable
- voicemessage_id: int - not nullable

### smTransitionType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- processType_id: int - not nullable

### smTransportProtocol
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smType
- oid: int - not nullable (Primary Key)
- code: varchar(255) - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- object_id: int - not nullable (Foreign Key)
- type_id: int - not nullable (Foreign Key)
- classname: varchar(255) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- publicType: varchar(10) - not nullable

### smUIAttribute
- oid: int - not nullable (Primary Key)
- type_id: int - not nullable (Foreign Key)
- widget_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- value: text - not nullable

### smUIAttributeType
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- widget_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- defaultValue: varchar(255) - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- required: varchar(10) - not nullable
- type_id: int - not nullable

### smUIIcon
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- style: varchar(255) - not nullable
- value: varchar(255) - not nullable

### smUIPageType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smUIRedirectionAlias
- oid: int - not nullable (Primary Key)
- redirection_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- destination_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable

### smUIStyle
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- color_id: int - not nullable
- description_id: int - not nullable
- fontSize: varchar(255) - not nullable
- fontStyle: varchar(255) - not nullable
- fontWeight: varchar(255) - not nullable
- icon_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- secondaryColor_id: int - not nullable
- textDecoration: varchar(255) - not nullable
- textVisibility: varchar(255) - not nullable

### smUITheme
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- pageType_id: int - not nullable
- primaryColor_id: int - not nullable

### smUIWidget
- oid: int - not nullable (Primary Key)
- module_id: int - not nullable (Foreign Key)
- object_id: int - not nullable (Foreign Key)
- page_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- widgetGroup_id: int - not nullable (Foreign Key)
- widgetType_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- header_id: int - not nullable
- helpTopic_id: int - not nullable
- label_id: int - not nullable
- layout_id: int - not nullable
- name: varchar(255) - not nullable
- operation_id: int - not nullable
- pageOrder: int - not nullable
- query_id: int - not nullable
- queryElement_id: int - not nullable
- querySort_id: int - not nullable
- redirection_id: int - not nullable
- style_id: int - not nullable
- toolbar_id: int - not nullable
- type_id: int - not nullable
- variable_id: int - not nullable
- widgetGroup: varchar(255) - not nullable
- widgetType: varchar(255) - not nullable

### smUIWidgetAttribute
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable (Foreign Key)
- widget_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- defaultValue: varchar(255) - not nullable
- module_id: int - not nullable

### smUIWidgetDataType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- module_id: int - not nullable
- subType_id: int - not nullable
- type: varchar(255) - not nullable
- widgetType_id: int - not nullable

### smUIWidgetGroup
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable
- widgetType_id: int - not nullable

### smUIWidgetRelation
- oid: int - not nullable (Primary Key)
- child_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- parent_id: int - not nullable
- parentRelation_id: int - not nullable
- widgetGroup_id: int - not nullable

### smUIWidgetType
- oid: int - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- abstractWidget: varchar(10) - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- pageType_id: int - not nullable
- parent_id: int - not nullable
- status: varchar(255) - not nullable
- widgetClass_id: int - not nullable

### smUseCase
- oid: int - not nullable (Primary Key)
- feature_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- parent_id: int - not nullable
- process_id: int - not nullable
- referenceId: char(36) - not nullable
- testType_id: int - not nullable
- type: varchar(255) - not nullable
- versionNo: int - not nullable

### smUseCaseStep
- oid: int - not nullable (Primary Key)
- useCase_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- parameters: text - not nullable
- reference_id: int - not nullable
- referenceId: char(36) - not nullable
- response: text - not nullable
- sequence: int - not nullable
- state_id: int - not nullable
- transition_id: int - not nullable
- versionNo: int - not nullable

### smUserAuthentication
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- initialCredentialStatus: varchar(10) - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- offlinePrivilege: varchar(10) - not nullable
- policy_id: int - not nullable
- securityPolicy_id: int - not nullable
- sessiontype_id: int - not nullable
- status: varchar(255) - not nullable
- system_id: int - not nullable
- usertype_id: int - not nullable

### smUserEndpoint
- oid: int - not nullable (Primary Key)
- applicationModel_id: int - not nullable
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable

### smUserEndpointAccess
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- module_id: int - not nullable
- userEndpoint_id: int - not nullable
- userType_id: int - not nullable

### smUserEndpointInstance
- oid: int - not nullable (Primary Key)
- authenticationSystem_id: int - not nullable
- classoid: int - not nullable
- endpoint_id: int - not nullable
- module_id: int - not nullable
- parent_id: int - not nullable

### smUserEndpointType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- pageType_id: int - not nullable

### smUserType
- oid: int - not nullable (Primary Key)
- baseType_id: int - not nullable
- classoid: int - not nullable
- defaultRole_id: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- userClass: varchar(255) - not nullable

### smUserTypePermType
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- description_id: int - not nullable
- label_id: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- permissionType_id: int - not nullable
- required: varchar(10) - not nullable
- userType_id: int - not nullable

### smUserTypeRight
- oid: int - not nullable (Primary Key)
- child_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- parent_id: int - not nullable

### smXMLNamespace
- oid: int - not nullable (Primary Key)
- alias: varchar(255) - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- schema_url: text - not nullable
- template_id: int - not nullable

### sysActionCache
- oid: bigint - not nullable (Primary Key)
- action_id: int - not nullable (Foreign Key)
- actionKey: varchar(255) - not nullable
- classoid: int - not nullable
- executionCount: bigint - not nullable

### sysAppServiceStatus
- oid: bigint - not nullable (Primary Key)
- applicationServer_id: int - not nullable
- classoid: int - not nullable
- instance_id: int - not nullable
- messages: text - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- service_id: int - not nullable
- startDate: datetime - not nullable
- status: varchar(255) - not nullable
- stopDate: datetime - not nullable

### sysApplicationEvent
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- data: text - not nullable
- event: varchar(255) - not nullable
- fromStatus: varchar(255) - not nullable
- server_id: int - not nullable
- serverName: varchar(255) - not nullable
- timestamp: datetime - not nullable
- toStatus: varchar(255) - not nullable
- version_id: int - not nullable

### sysApplicationVersion
- oid: bigint - not nullable (Primary Key)
- application_id: int - not nullable
- buildNo: int - not nullable
- classoid: int - not nullable
- currentStatus: varchar(255) - not nullable
- desiredStatus: varchar(255) - not nullable
- modelSchema: varchar(255) - not nullable
- version: varchar(255) - not nullable

### sysArchivedMessage
- oid: bigint - not nullable (Primary Key)
- account_id: int - not nullable (Foreign Key)
- content_id: int - not nullable (Foreign Key)
- endpoint_id: int - not nullable (Foreign Key)
- recipient_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- timestamp: datetime - not nullable (Foreign Key)
- classoid: int - not nullable
- instance_id: int - not nullable
- message: text - not nullable
- recipientName: varchar(255) - not nullable
- recipientType_id: int - not nullable

### sysArchivedPoolItem
- oid: bigint - not nullable (Primary Key)
- action_id: int - not nullable (Foreign Key)
- itemId: char(36) - not nullable (Foreign Key)
- pool_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- completedTime: datetime - not nullable
- exception: text - not nullable
- groupName: varchar(255) - not nullable
- messages: text - not nullable
- name: varchar(255) - not nullable
- parameters: text - not nullable
- priority: int - not nullable
- requestedTime: datetime - not nullable
- startedTime: datetime - not nullable
- user_id: int - not nullable

### sysAttributeConflict
- oid: bigint - not nullable (Primary Key)
- objectConflict_id: int - not nullable (Foreign Key)
- action: varchar(255) - not nullable
- attribute_id: int - not nullable
- classoid: int - not nullable
- currentDisplay: varchar(255) - not nullable
- currentValue: text - not nullable
- globalAttribute_id: int - not nullable
- modifiedValue: text - not nullable
- name: varchar(255) - not nullable
- newDisplay: varchar(255) - not nullable
- newValue: text - not nullable
- resolutionMode: varchar(255) - not nullable
- status: varchar(255) - not nullable

### sysCalendar
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- country_id: int - not nullable
- description: varchar(255) - not nullable
- endDate: datetime - not nullable
- interval_id: int - not nullable
- inverseDays: varchar(10) - not nullable
- name: varchar(255) - not nullable
- startDate: datetime - not nullable
- status: varchar(255) - not nullable

### sysCalendarDay
- oid: int - not nullable (Primary Key)
- calendar_id: int - not nullable
- classoid: int - not nullable
- day: datetime - not nullable
- description: varchar(255) - not nullable
- type: varchar(255) - not nullable

### sysCalendarOptions
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- firstDayWeek: int - not nullable
- firstHourDay: varchar(255) - not nullable
- firstMonthYear: int - not nullable
- name: varchar(255) - not nullable

### sysCodeCompilation
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- endTime: datetime - not nullable
- startTime: datetime - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable
- user_id: int - not nullable

### sysCompiledCode
- oid: bigint - not nullable (Primary Key)
- className: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- content: mediumtext - not nullable
- generatedCode_id: int - not nullable

### sysCountry
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- code: varchar(255) - not nullable
- name: varchar(255) - not nullable

### sysCredentials
- oid: int - not nullable (Primary Key)
- password: varchar(255) - not nullable (Foreign Key)
- user_id: int - not nullable (Foreign Key)
- username: varchar(255) - not nullable (Foreign Key)
- attempts: int - not nullable
- classoid: int - not nullable
- creationDate: datetime - not nullable
- expiration: datetime - not nullable
- policy_id: int - not nullable
- salt: char(36) - not nullable
- security_id: int - not nullable
- status: varchar(255) - not nullable
- system_id: int - not nullable
- tempPassword: varchar(255) - not nullable

### sysCredentialsHistory
- oid: bigint - not nullable (Primary Key)
- changedby_id: int - not nullable
- classoid: int - not nullable
- credentials_id: int - not nullable
- password: varchar(255) - not nullable
- policy_id: int - not nullable
- timestamp: datetime - not nullable
- username: varchar(255) - not nullable

### sysCurrency
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- code: varchar(255) - not nullable
- name: varchar(255) - not nullable

### sysCustomAttributeValue
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- custom_id: int - not nullable
- object_id: int - not nullable
- value: varchar(255) - not nullable

### sysDevice
- oid: bigint - not nullable (Primary Key)
- deviceId: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- description: text - not nullable
- deviceModel_id: int - not nullable
- macAddress: varchar(255) - not nullable
- userAgent_id: int - not nullable

### sysDeviceModel
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- manufacturer: varchar(255) - not nullable
- name: varchar(255) - not nullable

### sysDiagnosticIssue
- oid: bigint - not nullable (Primary Key)
- issueGroup_id: int - not nullable (Foreign Key)
- result_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description: text - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- objectType_id: int - not nullable
- resolution_id: int - not nullable
- status: varchar(255) - not nullable
- type_id: int - not nullable

### sysDiagnosticIssueGroup
- oid: bigint - not nullable (Primary Key)
- result_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- issueType_id: int - not nullable
- name: varchar(255) - not nullable

### sysDiagnosticIssueParam
- oid: bigint - not nullable (Primary Key)
- issue_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- name: varchar(255) - not nullable
- type_id: int - not nullable
- value: varchar(255) - not nullable

### sysDiagnosticResult
- oid: bigint - not nullable (Primary Key)
- diagnostic_id: int - not nullable (Foreign Key)
- instance_id: int - not nullable (Foreign Key)
- archive: varchar(10) - not nullable
- classoid: int - not nullable
- granularity_id: int - not nullable
- messageData: text - not nullable
- name: varchar(255) - not nullable
- parent_id: int - not nullable
- serializedData: text - not nullable
- startTime: datetime - not nullable
- status: varchar(255) - not nullable
- subtype_id: int - not nullable
- threshold_id: int - not nullable
- timestamp: datetime - not nullable
- unit_id: int - not nullable
- user_id: int - not nullable
- value: decimal(19,2) - not nullable

### sysDiagnosticSubtype
- oid: bigint - not nullable (Primary Key)
- diagnostic_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- description: varchar(255) - not nullable
- name: varchar(255) - not nullable
- reference_id: int - not nullable
- reference_type: int - not nullable

### sysDocument
- oid: int - not nullable (Primary Key)
- doctype_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- owner_type: int - not nullable (Foreign Key)
- classoid: int - not nullable
- coverPage_id: int - not nullable
- createdBy: int - not nullable
- creationDate: datetime - not nullable
- description_id: int - not nullable
- fileName: varchar(255) - not nullable
- filetype_id: int - not nullable
- folder_id: int - not nullable
- label_id: int - not nullable
- language_id: int - not nullable
- owner_id: int - not nullable
- parent_id: int - not nullable
- referenceId: char(36) - not nullable
- reportRelation_id: int - not nullable
- repository_id: int - not nullable
- status: varchar(255) - not nullable
- tableOfContents_id: int - not nullable
- template_id: int - not nullable
- type_id: int - not nullable
- version: int - not nullable

### sysEvent
- oid: bigint - not nullable (Primary Key)
- action_id: int - not nullable (Foreign Key)
- reference_id: int - not nullable (Foreign Key)
- actionEvent_id: int - not nullable
- classoid: int - not nullable
- eventCode: varchar(255) - not nullable
- eventData: text - not nullable
- partitionNo: int - not nullable
- referenceKey: varchar(255) - not nullable
- referenceType: int - not nullable
- timestamp: datetime - not nullable
- user_id: int - not nullable

### sysGeneratedCode
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- codeTemplate_id: int - not nullable
- message: text - not nullable
- name: varchar(255) - not nullable
- objectContext_id: int - not nullable
- sourceCode: mediumtext - not nullable
- status: varchar(255) - not nullable
- timestamp: datetime - not nullable

### sysGlobalAttribute
- oid: bigint - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- module_id: int - not nullable
- originalValue: text - not nullable

### sysGlobalKey
- oid: bigint - not nullable (Primary Key)
- currentVersion_id: int - not nullable (Foreign Key)
- globalKey: char(36) - not nullable (Foreign Key)
- localKey: int - not nullable (Foreign Key)
- object_id: int - not nullable (Foreign Key)
- originalVersion_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- transactionGroup_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- deleted: varchar(10) - not nullable
- keyVersion_id: int - not nullable
- name: varchar(255) - not nullable
- originalVersionNo: int - not nullable
- versionNo: int - not nullable

### sysGlobalKeyModule
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- globalKey_id: int - not nullable
- module_id: int - not nullable
- version_id: int - not nullable
- versionNo: int - not nullable

### sysGlobalKeyVersion
- oid: bigint - not nullable (Primary Key)
- globalKey_id: int - not nullable (Foreign Key)
- transaction_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- module_id: int - not nullable
- name: varchar(255) - not nullable
- operation: varchar(255) - not nullable
- previous_id: int - not nullable
- version_id: int - not nullable
- versionNo: int - not nullable

### sysGlobalModule
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- defaultGroup_id: int - not nullable
- globalKey: char(36) - not nullable
- lastModified: char(36) - not nullable
- module_id: int - not nullable
- nextId: int - not nullable

### sysGlobalObjVersion
- oid: bigint - not nullable (Primary Key)
- object_id: int - not nullable (Foreign Key)
- version_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- globalKey: char(36) - not nullable
- lastModified: char(36) - not nullable

### sysGlobalObject
- oid: bigint - not nullable (Primary Key)
- object_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- globalKey: char(36) - not nullable
- lastModified: char(36) - not nullable
- module_id: int - not nullable

### sysGlobalVersion
- oid: bigint - not nullable (Primary Key)
- module_id: int - not nullable (Foreign Key)
- version_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- globalKey: char(36) - not nullable
- lastModified: char(36) - not nullable

### sysImportedItem
- oid: bigint - not nullable (Primary Key)
- externaltoken: varchar(255) - not nullable (Foreign Key)
- importedStamp: datetime - not nullable (Foreign Key)
- timestamp: datetime - not nullable (Foreign Key)
- classoid: int - not nullable
- config_id: int - not nullable
- content: mediumtext - not nullable
- errors: mediumtext - not nullable
- importer_id: int - not nullable
- interfaceInstance_id: int - not nullable
- modifiedContent: mediumtext - not nullable
- partitionNo: int - not nullable
- response: mediumtext - not nullable
- source_id: int - not nullable
- startTime: datetime - not nullable
- status: varchar(255) - not nullable

### sysImportingItem
- oid: bigint - not nullable (Primary Key)
- startTime: datetime - not nullable (Foreign Key)
- timestamp: datetime - not nullable (Foreign Key)
- classoid: int - not nullable
- config_id: int - not nullable
- content: mediumtext - not nullable
- endTime: datetime - not nullable
- errors: mediumtext - not nullable
- externaltoken: varchar(255) - not nullable
- importer_id: int - not nullable
- interfaceInstance_id: int - not nullable
- modifiedContent: mediumtext - not nullable
- response: mediumtext - not nullable
- source_id: int - not nullable
- status: varchar(255) - not nullable

### sysInstalledModule
- oid: bigint - not nullable (Primary Key)
- applicationVersion_id: int - not nullable
- buildDate: datetime - not nullable
- buildNo: int - not nullable
- classoid: int - not nullable
- globalKey: char(36) - not nullable
- lastModified: char(36) - not nullable
- name: varchar(255) - not nullable
- version: varchar(255) - not nullable

### sysInterfaceArchive
- oid: bigint - not nullable (Primary Key)
- timestamp: datetime - not nullable (Foreign Key)
- archivedDate: datetime - not nullable
- classoid: int - not nullable
- config_id: int - not nullable
- content: mediumtext - not nullable
- createdDate: datetime - not nullable
- destination_id: int - not nullable
- event_id: int - not nullable
- exporterTrigger_id: int - not nullable
- externalToken: varchar(255) - not nullable
- interfaceInstance_id: int - not nullable
- message: text - not nullable
- partitionNo: int - not nullable
- response: text - not nullable
- status: varchar(255) - not nullable
- trigger_id: int - not nullable

### sysInterfaceError
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- cron_id: int - not nullable
- endTime: datetime - not nullable
- exception: text - not nullable
- interface_id: int - not nullable
- lastRetry: datetime - not nullable
- message: text - not nullable
- startTime: datetime - not nullable
- status: varchar(255) - not nullable

### sysLanguage
- oid: int - not nullable (Primary Key)
- code: varchar(255) - not nullable (Foreign Key)
- active: varchar(10) - not nullable
- classoid: int - not nullable
- language: varchar(255) - not nullable
- locale: varchar(255) - not nullable
- name: varchar(255) - not nullable

### sysLocaleConfiguration
- oid: bigint - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- language_id: int - not nullable
- user_id: int - not nullable
- value: varchar(255) - not nullable

### sysLocalizableItem
- oid: int - not nullable (Primary Key)
- attribute_id: int - not nullable
- classoid: int - not nullable
- owner_id: int - not nullable
- owner_type: int - not nullable

### sysLocalizableValue
- oid: int - not nullable (Primary Key)
- localizable_id: int - not nullable (Foreign Key)
- autotranslated: varchar(10) - not nullable
- classoid: int - not nullable
- language: varchar(255) - not nullable
- message: mediumtext - not nullable

### sysLockEntry
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- lockKey: varchar(255) - not nullable
- name: varchar(255) - not nullable
- server_id: int - not nullable
- status: varchar(255) - not nullable
- timestamp: datetime - not nullable
- type: varchar(255) - not nullable
- user_id: int - not nullable

### sysMessageContent
- oid: bigint - not nullable (Primary Key)
- endpoint_id: int - not nullable (Foreign Key)
- message_id: int - not nullable (Foreign Key)
- reference_id: int - not nullable (Foreign Key)
- status: varchar(255) - not nullable (Foreign Key)
- attachments: text - not nullable
- classoid: int - not nullable
- content: text - not nullable
- creationDate: datetime - not nullable
- format_id: int - not nullable
- referenceType: int - not nullable
- sentDate: datetime - not nullable
- title: varchar(255) - not nullable
- type_id: int - not nullable
- user_id: int - not nullable

### sysMessageRecipientAccount
- oid: int - not nullable (Primary Key)
- recipient_id: int - not nullable (Foreign Key)
- accountName: varchar(255) - not nullable
- classoid: int - not nullable
- language_id: int - not nullable
- type_id: int - not nullable

### sysMessageSubscriptionRecipient
- oid: bigint - not nullable (Primary Key)
- account_id: int - not nullable
- classoid: int - not nullable
- recipient_id: int - not nullable
- status: varchar(255) - not nullable
- subscriptionGroup_id: int - not nullable

### sysMigrationScriptEvent
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- messages: text - not nullable
- migrationScript_id: int - not nullable
- moduleUpgrade_id: int - not nullable
- status: varchar(255) - not nullable
- timestamp: datetime - not nullable
- user_id: int - not nullable

### sysModuleUpgrade
- oid: bigint - not nullable (Primary Key)
- module_id: int - not nullable (Foreign Key)
- user_id: int - not nullable (Foreign Key)
- automatic: varchar(10) - not nullable
- classoid: int - not nullable
- conflictCount: int - not nullable
- fromBuildNo: int - not nullable
- fromVersion_id: int - not nullable
- incremental: varchar(10) - not nullable
- status: varchar(255) - not nullable
- timestamp: datetime - not nullable
- toBuildNo: int - not nullable
- toVersion_id: int - not nullable
- unresolvedConflictCount: int - not nullable
- upgradeMode: varchar(255) - not nullable

### sysObjectConflict
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- globalKey_id: int - not nullable
- name: varchar(255) - not nullable
- newVersion_id: int - not nullable
- newVersionNo: int - not nullable
- status: varchar(255) - not nullable
- type: varchar(255) - not nullable
- upgrade_id: int - not nullable

### sysObjectHistory
- oid: bigint - not nullable (Primary Key)
- logger_id: int - not nullable (Foreign Key)
- object_id: int - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- timestamp: datetime - not nullable (Foreign Key)
- user_id: int - not nullable (Foreign Key)
- action: varchar(255) - not nullable
- classoid: int - not nullable
- content: text - not nullable
- objectKey: int - not nullable
- objectName: varchar(255) - not nullable
- parentKey: int - not nullable
- transaction_id: int - not nullable

### sysObjectPermission
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- externalName: varchar(255) - not nullable
- name: varchar(255) - not nullable
- object_id: int - not nullable
- type_id: int - not nullable

### sysProcessProfiling
- oid: bigint - not nullable (Primary Key)
- process_id: int - not nullable (Foreign Key)
- requestId: varchar(255) - not nullable (Foreign Key)
- serverStartTime: datetime - not nullable (Foreign Key)
- session_id: int - not nullable (Foreign Key)
- accessPoint_id: int - not nullable
- activeDBConnection: int - not nullable
- classoid: int - not nullable
- clientExecutionTime: int - not nullable
- clientNetworkTime: int - not nullable
- clientStartTime: datetime - not nullable
- firstTransitions: varchar(255) - not nullable
- fromState_id: int - not nullable
- ipAddress: varchar(255) - not nullable
- location: varchar(255) - not nullable
- location_id: int - not nullable
- parameters: text - not nullable
- queryDuplicateCount: int - not nullable
- queryReadCount: int - not nullable
- queryWriteCount: int - not nullable
- response: text - not nullable
- responseSize: int - not nullable
- retryCount: int - not nullable
- rssi: int - not nullable
- serverExecutionTime: int - not nullable
- serverProcessTime: int - not nullable
- serverUITime: int - not nullable
- signalStrength: int - not nullable
- speed: int - not nullable
- toState_id: int - not nullable
- transition_id: int - not nullable
- transitionCount: int - not nullable
- widget_id: int - not nullable

### sysQuartzJobDetail
- oid: bigint - not nullable (Primary Key)
- scheduler_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- jobGroup: varchar(255) - not nullable
- jobName: varchar(255) - not nullable
- nonConcurrent: varchar(10) - not nullable
- paused: varchar(10) - not nullable
- requestsRecovery: varchar(10) - not nullable

### sysQuartzSchedulerInstance
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- name: varchar(255) - not nullable
- scheduler_id: int - not nullable
- server_id: int - not nullable

### sysQuartzTrigger
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- cronExpresion: varchar(255) - not nullable
- endTime: datetime - not nullable
- jobDetail_id: int - not nullable
- misfireInstruction: int - not nullable
- name: varchar(255) - not nullable
- nextFireTime: datetime - not nullable
- previousFireTime: datetime - not nullable
- priority: int - not nullable
- startTime: datetime - not nullable
- state: varchar(255) - not nullable

### sysQuartzTriggerInstance
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- instance_id: int - not nullable
- trigger_id: int - not nullable

### sysQuickLinks
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- keyvalue: varchar(255) - not nullable
- name: varchar(255) - not nullable
- sequence: int - not nullable
- user_id: int - not nullable
- widget_id: int - not nullable

### sysStateProvince
- oid: bigint - not nullable (Primary Key)
- code: varchar(255) - not nullable (Foreign Key)
- country_id: int - not nullable (Foreign Key)
- name: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable

### sysTransactionGroupUpgrade
- oid: bigint - not nullable (Primary Key)
- moduleUpgrade_id: int - not nullable (Foreign Key)
- transactionGroup_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- conflictCount: int - not nullable
- status: varchar(255) - not nullable
- unresolvedConflictCount: int - not nullable

### sysUIProfiling
- oid: bigint - not nullable (Primary Key)
- fromPage_id: int - not nullable (Foreign Key)
- serverStartTime: datetime - not nullable (Foreign Key)
- session_id: int - not nullable (Foreign Key)
- toPage_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- fromWidget_id: int - not nullable
- operation_id: int - not nullable
- parameters: text - not nullable
- queryDuplicateCount: int - not nullable
- queryReadCount: int - not nullable
- queryWriteCount: int - not nullable
- serverExecutionTime: int - not nullable
- toWidget_id: int - not nullable

### sysUserAgent
- oid: bigint - not nullable (Primary Key)
- classoid: int - not nullable
- name: varchar(255) - not nullable

### sysUserPermission
- oid: int - not nullable (Primary Key)
- classoid: int - not nullable
- object_id: int - not nullable
- permission_id: int - not nullable
- user_id: int - not nullable

### sysUserRole
- oid: int - not nullable (Primary Key)
- user_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- role_id: int - not nullable

### sysUserSession
- oid: bigint - not nullable (Primary Key)
- credentials_id: int - not nullable (Foreign Key)
- sessionKey: varchar(255) - not nullable (Foreign Key)
- sessionStart: datetime - not nullable (Foreign Key)
- assumedIdentity_id: int - not nullable
- classoid: int - not nullable
- device_id: int - not nullable
- endpoint_id: int - not nullable
- language: varchar(255) - not nullable
- lastActivity: datetime - not nullable
- lastServer: varchar(255) - not nullable
- network_id: int - not nullable
- parameters: text - not nullable
- sessionEnd: datetime - not nullable
- source: varchar(255) - not nullable
- status: varchar(255) - not nullable
- system_id: int - not nullable
- type_id: int - not nullable
- userAgent_id: int - not nullable
- userEndpoint_id: int - not nullable
- username: varchar(255) - not nullable

### sysUserTransaction
- oid: bigint - not nullable (Primary Key)
- session_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- timestamp: datetime - not nullable
- transactionId: char(36) - not nullable
- user_id: int - not nullable

### sysUserTransactionGroup
- oid: bigint - not nullable (Primary Key)
- transactionGroup_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- closedDate: datetime - not nullable
- openedDate: datetime - not nullable
- status: varchar(255) - not nullable
- user_id: int - not nullable
- userSession_id: int - not nullable

### sysWorkflowSession
- oid: bigint - not nullable (Primary Key)
- sessionKey: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- data: mediumtext - not nullable
- lastActivity: datetime - not nullable
- lastProfiling_id: int - not nullable
- lastRequestId: varchar(255) - not nullable
- process_id: int - not nullable
- state_id: int - not nullable
- status: varchar(255) - not nullable
- userSession_id: int - not nullable

### testObject
- oid: bigint - not nullable (Primary Key)
- name: varchar(255) - not nullable (Foreign Key)
- parent_id: int - not nullable (Foreign Key)
- classoid: int - not nullable
- sequence: int - not nullable
- testBigDecimal: decimal(19,2) - not nullable
- testBoolean: varchar(10) - not nullable
- testDate: datetime - not nullable
- testInteger: int - not nullable
- testLocalizedString_id: int - not nullable
- testString: varchar(255) - not nullable
- testStringEnum: varchar(255) - not nullable
- testText: text - not nullable
- testTotalValue: decimal(19,2) - not nullable
- testUUID: char(36) - not nullable
- testValue: decimal(19,2) - not nullable

### users
- oid: int - not nullable (Primary Key)
- userName: varchar(255) - not nullable (Foreign Key)
- classoid: int - not nullable
- firstName: varchar(255) - not nullable
- language_id: int - not nullable
- lastName: varchar(255) - not nullable
- locale: varchar(255) - not nullable
- status: varchar(255) - not nullable
- timeZone: varchar(255) - not nullable
- type_id: int - not nullable
- userGroup_id: int - not nullable

---


## 7. Summary of Top Tables Structure

Shows a summary of column types and keys for each large table

Structure summary for major tables:

### scMaterial
- Total columns: 64
- Primary keys: 1.0
- Foreign keys: 18.0
- Nullable columns: 0.0
- Data types used: bigint,datetime,decimal,int,varchar

### scMovement
- Total columns: 48
- Primary keys: 1.0
- Foreign keys: 20.0
- Nullable columns: 0.0
- Data types used: bigint,datetime,decimal,int,varchar

### sysProcessProfiling
- Total columns: 33
- Primary keys: 1.0
- Foreign keys: 4.0
- Nullable columns: 0.0
- Data types used: bigint,datetime,int,text,varchar

### scMIAdjustment
- Total columns: 26
- Primary keys: 1.0
- Foreign keys: 6.0
- Nullable columns: 0.0
- Data types used: bigint,datetime,decimal,int,varchar

### scLineAdjustment
- Total columns: 22
- Primary keys: 1.0
- Foreign keys: 3.0
- Nullable columns: 0.0
- Data types used: bigint,int,varchar

### scOrderAdjustment
- Total columns: 19
- Primary keys: 1.0
- Foreign keys: 2.0
- Nullable columns: 0.0
- Data types used: bigint,datetime,int,varchar

### scGeneratedMREQ
- Total columns: 18
- Primary keys: 1.0
- Foreign keys: 3.0
- Nullable columns: 0.0
- Data types used: bigint,decimal,int,mediumtext,varchar

### sysEvent
- Total columns: 12
- Primary keys: 1.0
- Foreign keys: 2.0
- Nullable columns: 0.0
- Data types used: bigint,datetime,int,text,varchar

### scMIAdjustmentDimension
- Total columns: 9
- Primary keys: 1.0
- Foreign keys: 2.0
- Nullable columns: 0.0
- Data types used: bigint,decimal,int

### oidToTable
- Total columns: 3
- Primary keys: 1.0
- Foreign keys: 2.0
- Nullable columns: 0.0
- Data types used: int


---


## 8. Daily Operation Volumes

Analyzes daily operation patterns in the warehouse

Daily operation patterns:

- 2024-10-30: Pick - 950 operations by 24 users
- 2024-10-30: DropPick - 544 operations by 19 users
- 2024-10-30: Ship - 404 operations by 1 users
- 2024-10-30: MoveOut - 356 operations by 8 users
- 2024-10-30: Load - 346 operations by 2 users
- 2024-10-30: Receive - 286 operations by 2 users
- 2024-10-30: MoveIn - 226 operations by 5 users
- 2024-10-30: PickingHandlingMaterialAdj - 136 operations by 1 users
- 2024-10-30: Putaway - 118 operations by 5 users
- 2024-10-30: DropReceive - 94 operations by 2 users
- 2024-10-30: ReplenishIn - 24 operations by 2 users
- 2024-10-30: Move - 7 operations by 1 users
- 2024-10-30: CountCreation - 4 operations by 2 users
- 2024-10-30: Inbound - 3 operations by 1 users
- 2024-10-30: Cancel - 2 operations by 1 users
- 2024-10-30: Creation - 2 operations by 1 users
- 2024-10-30: ReconcileIn - 2 operations by 1 users
- 2024-10-30: StandBy - 2 operations by 2 users
- 2024-10-29: Pick - 15540 operations by 71 users
- 2024-10-29: Ship - 10605 operations by 8 users
- 2024-10-29: DropPick - 9854 operations by 71 users
- 2024-10-29: Receive - 6908 operations by 17 users
- 2024-10-29: Load - 6729 operations by 17 users
- 2024-10-29: MoveOut - 6141 operations by 56 users
- 2024-10-29: PickingHandlingMaterialAdj - 3664 operations by 8 users
- 2024-10-29: MoveIn - 3438 operations by 44 users
- 2024-10-29: Putaway - 2496 operations by 35 users
- 2024-10-29: DropReceive - 2110 operations by 13 users
- 2024-10-29: ReplenishIn - 578 operations by 13 users
- 2024-10-29: Move - 317 operations by 8 users
- 2024-10-29: MoveTE - 254 operations by 2 users
- 2024-10-29: Cancel - 200 operations by 22 users
- 2024-10-29: Creation - 186 operations by 1 users
- 2024-10-29: Quantity - 158 operations by 2 users
- 2024-10-29: CountOutTol - 149 operations by 2 users
- 2024-10-29: CountNotFound - 132 operations by 4 users
- 2024-10-29: CountCreation - 119 operations by 11 users
- 2024-10-29: CountInTol - 108 operations by 1 users
- 2024-10-29: StandBy - 71 operations by 18 users
- 2024-10-29: Unload - 71 operations by 2 users
- 2024-10-29: Inbound - 63 operations by 4 users
- 2024-10-29: LoadHandlingMaterialAdj - 62 operations by 3 users
- 2024-10-29: ReconcileIn - 60 operations by 7 users
- 2024-10-29: AutomaticCondition - 36 operations by 1 users
- 2024-10-29: Scrap - 17 operations by 4 users
- 2024-10-29: Condition - 16 operations by 2 users
- 2024-10-29: ConsolidateLicensePlate - 10 operations by 3 users
- 2024-10-29: ChangeLabel - 4 operations by 2 users
- 2024-10-29: Reclassify - 3 operations by 1 users
- 2024-10-29: Consolidate - 2 operations by 2 users
- 2024-10-29: Dimension - 1 operations by 1 users
- 2024-10-28: Pick - 17551 operations by 82 users
- 2024-10-28: DropPick - 9996 operations by 82 users
- 2024-10-28: Ship - 9029 operations by 7 users
- 2024-10-28: Load - 5967 operations by 12 users
- 2024-10-28: MoveOut - 4960 operations by 46 users
- 2024-10-28: PickingHandlingMaterialAdj - 3708 operations by 7 users
- 2024-10-28: Receive - 3564 operations by 10 users
- 2024-10-28: MoveIn - 3478 operations by 46 users
- 2024-10-28: Putaway - 1646 operations by 29 users
- 2024-10-28: DropReceive - 1224 operations by 8 users
- 2024-10-28: Creation - 636 operations by 1 users
- 2024-10-28: ReplenishIn - 592 operations by 8 users
- 2024-10-28: Move - 247 operations by 10 users
- 2024-10-28: CountOutTol - 230 operations by 3 users
- 2024-10-28: CountNotFound - 213 operations by 3 users
- 2024-10-28: CountInTol - 116 operations by 1 users
- 2024-10-28: Cancel - 95 operations by 21 users
- 2024-10-28: CountCreation - 87 operations by 10 users
- 2024-10-28: LoadHandlingMaterialAdj - 70 operations by 3 users
- 2024-10-28: StandBy - 44 operations by 14 users
- 2024-10-28: Condition - 32 operations by 3 users
- 2024-10-28: AutomaticCondition - 30 operations by 1 users
- 2024-10-28: Inbound - 30 operations by 6 users
- 2024-10-28: Scrap - 15 operations by 4 users
- 2024-10-28: ChangeLabel - 10 operations by 2 users
- 2024-10-28: MoveTE - 8 operations by 2 users
- 2024-10-28: ReconcileIn - 6 operations by 3 users
- 2024-10-28: Consolidate - 3 operations by 1 users
- 2024-10-28: ConsolidateLicensePlate - 2 operations by 1 users
- 2024-10-28: Dimension - 2 operations by 1 users
- 2024-10-28: Quantity - 2 operations by 1 users
- 2024-10-28: Unpick - 2 operations by 1 users
- 2024-10-27: Pick - 10560 operations by 58 users
- 2024-10-27: Ship - 7274 operations by 3 users
- 2024-10-27: Load - 6872 operations by 11 users
- 2024-10-27: DropPick - 6119 operations by 58 users
- 2024-10-27: Receive - 5812 operations by 10 users
- 2024-10-27: MoveOut - 3404 operations by 47 users
- 2024-10-27: PickingHandlingMaterialAdj - 2608 operations by 3 users
- 2024-10-27: Putaway - 1990 operations by 32 users
- 2024-10-27: DropReceive - 1974 operations by 8 users
- 2024-10-27: MoveIn - 853 operations by 33 users
- 2024-10-27: Cancel - 408 operations by 23 users
- 2024-10-27: ReplenishIn - 334 operations by 13 users
- 2024-10-27: Move - 231 operations by 3 users
- 2024-10-27: Unload - 188 operations by 1 users
- 2024-10-27: Condition - 90 operations by 1 users
- 2024-10-27: StandBy - 48 operations by 10 users
- 2024-10-27: Reclassify - 45 operations by 2 users
- 2024-10-27: Quantity - 24 operations by 1 users
- 2024-10-27: AutomaticCondition - 18 operations by 1 users
- 2024-10-27: LoadHandlingMaterialAdj - 18 operations by 2 users
- 2024-10-27: Inbound - 16 operations by 2 users
- 2024-10-27: CountCreation - 11 operations by 3 users
- 2024-10-27: CountOutTol - 5 operations by 1 users
- 2024-10-27: MoveTE - 5 operations by 2 users
- 2024-10-27: Consolidate - 4 operations by 1 users
- 2024-10-27: CountNotFound - 4 operations by 1 users
- 2024-10-27: Dimension - 4 operations by 2 users
- 2024-10-27: ReconcileIn - 4 operations by 2 users
- 2024-10-27: Creation - 3 operations by 1 users
- 2024-10-27: ChangeLabel - 2 operations by 1 users
- 2024-10-27: ConsolidateLicensePlate - 2 operations by 1 users
- 2024-10-27: Unpick - 2 operations by 1 users
- 2024-10-27: Scrap - 1 operations by 1 users
- 2024-10-26: Pick - 16072 operations by 60 users
- 2024-10-26: Ship - 9638 operations by 3 users
- 2024-10-26: DropPick - 9429 operations by 60 users
- 2024-10-26: Load - 7169 operations by 13 users
- 2024-10-26: Receive - 6084 operations by 11 users
- 2024-10-26: MoveOut - 5349 operations by 42 users
- 2024-10-26: PickingHandlingMaterialAdj - 3458 operations by 3 users
- 2024-10-26: MoveIn - 3013 operations by 34 users
- 2024-10-26: DropReceive - 2074 operations by 10 users
- 2024-10-26: Putaway - 2048 operations by 28 users
- 2024-10-26: ReplenishIn - 412 operations by 11 users
- 2024-10-26: Move - 303 operations by 2 users
- 2024-10-26: Cancel - 277 operations by 19 users
- 2024-10-26: Condition - 200 operations by 3 users
- 2024-10-26: Reclassify - 171 operations by 2 users
- 2024-10-26: Unload - 149 operations by 1 users
- 2024-10-26: Creation - 78 operations by 1 users
- 2024-10-26: Inbound - 51 operations by 2 users
- 2024-10-26: StandBy - 46 operations by 10 users
- 2024-10-26: LoadHandlingMaterialAdj - 36 operations by 2 users
- 2024-10-26: CountOutTol - 34 operations by 2 users
- 2024-10-26: ProductionOutput - 28 operations by 1 users
- 2024-10-26: CountCreation - 26 operations by 9 users
- 2024-10-26: AutomaticCondition - 22 operations by 1 users
- 2024-10-26: ProductionConsume - 15 operations by 1 users
- 2024-10-26: ConsolidateLicensePlate - 10 operations by 2 users
- 2024-10-26: Quantity - 6 operations by 2 users
- 2024-10-26: CountNotFound - 5 operations by 2 users
- 2024-10-26: ChangeLabel - 4 operations by 2 users
- 2024-10-26: MoveTE - 3 operations by 1 users
- 2024-10-26: Scrap - 3 operations by 1 users
- 2024-10-26: ProductionStart - 1 operations by 1 users
- 2024-10-25: Pick - 16131 operations by 74 users
- 2024-10-25: Ship - 10399 operations by 6 users
- 2024-10-25: DropPick - 9744 operations by 74 users
- 2024-10-25: Load - 6884 operations by 13 users
- 2024-10-25: Receive - 6700 operations by 15 users
- 2024-10-25: MoveOut - 6400 operations by 49 users
- 2024-10-25: MoveIn - 3831 operations by 42 users
- 2024-10-25: PickingHandlingMaterialAdj - 3714 operations by 6 users
- 2024-10-25: Putaway - 2436 operations by 32 users
- 2024-10-25: DropReceive - 2186 operations by 12 users
- 2024-10-25: ReplenishIn - 534 operations by 9 users
- 2024-10-25: Move - 304 operations by 8 users
- 2024-10-25: Cancel - 244 operations by 20 users
- 2024-10-25: CountNotFound - 191 operations by 5 users
- 2024-10-25: CountOutTol - 179 operations by 2 users
- 2024-10-25: CountInTol - 118 operations by 1 users
- 2024-10-25: Creation - 107 operations by 1 users
- 2024-10-25: Scrap - 103 operations by 4 users
- 2024-10-25: CountCreation - 78 operations by 12 users
- 2024-10-25: StandBy - 69 operations by 16 users
- 2024-10-25: Inbound - 58 operations by 6 users
- 2024-10-25: LoadHandlingMaterialAdj - 48 operations by 1 users
- 2024-10-25: AutomaticCondition - 24 operations by 1 users
- 2024-10-25: Condition - 24 operations by 6 users
- 2024-10-25: Quantity - 20 operations by 3 users
- 2024-10-25: ReconcileIn - 14 operations by 7 users
- 2024-10-25: MoveTE - 8 operations by 2 users
- 2024-10-25: Consolidate - 7 operations by 1 users
- 2024-10-25: ChangeLabel - 4 operations by 1 users
- 2024-10-25: ConsolidateLicensePlate - 2 operations by 1 users
- 2024-10-25: ReconcileOut - 2 operations by 1 users
- 2024-10-24: Pick - 18021 operations by 80 users
- 2024-10-24: Ship - 10696 operations by 6 users
- 2024-10-24: DropPick - 10669 operations by 78 users
- 2024-10-24: Load - 7700 operations by 14 users
- 2024-10-24: Receive - 7180 operations by 14 users
- 2024-10-24: MoveOut - 6230 operations by 56 users
- 2024-10-24: MoveIn - 3347 operations by 49 users
- 2024-10-24: PickingHandlingMaterialAdj - 3238 operations by 5 users
- 2024-10-24: Putaway - 2680 operations by 34 users
- 2024-10-24: DropReceive - 2314 operations by 11 users
- 2024-10-24: ReplenishIn - 598 operations by 9 users
- 2024-10-24: Move - 312 operations by 7 users
- 2024-10-24: Creation - 196 operations by 1 users
- 2024-10-24: Quantity - 172 operations by 3 users
- 2024-10-24: MoveTE - 158 operations by 3 users
- 2024-10-24: Cancel - 131 operations by 28 users
- 2024-10-24: CountOutTol - 125 operations by 3 users
- 2024-10-24: CountNotFound - 99 operations by 5 users
- 2024-10-24: CountInTol - 80 operations by 1 users
- 2024-10-24: Unload - 76 operations by 1 users
- 2024-10-24: Condition - 66 operations by 2 users
- 2024-10-24: StandBy - 63 operations by 16 users
- 2024-10-24: Inbound - 54 operations by 5 users
- 2024-10-24: ReconcileIn - 34 operations by 5 users
- 2024-10-24: Dimension - 33 operations by 3 users
- 2024-10-24: CountCreation - 32 operations by 8 users
- 2024-10-24: AutomaticCondition - 16 operations by 1 users
- 2024-10-24: LoadHandlingMaterialAdj - 16 operations by 2 users
- 2024-10-24: Scrap - 9 operations by 2 users
- 2024-10-24: Consolidate - 7 operations by 3 users
- 2024-10-24: ReconcileOut - 2 operations by 1 users
- 2024-10-23: Pick - 16783 operations by 76 users
- 2024-10-23: Ship - 10745 operations by 5 users
- 2024-10-23: DropPick - 9966 operations by 74 users
- 2024-10-23: Load - 7425 operations by 13 users
- 2024-10-23: Receive - 6732 operations by 13 users
- 2024-10-23: MoveOut - 6049 operations by 51 users
- 2024-10-23: PickingHandlingMaterialAdj - 3780 operations by 5 users
- 2024-10-23: MoveIn - 3277 operations by 43 users
- 2024-10-23: Putaway - 2436 operations by 32 users
- 2024-10-23: DropReceive - 2238 operations by 9 users
- 2024-10-23: ReplenishIn - 602 operations by 11 users
- 2024-10-23: Move - 328 operations by 6 users
- 2024-10-23: Creation - 292 operations by 1 users
- 2024-10-23: Cancel - 260 operations by 20 users
- 2024-10-23: CountOutTol - 244 operations by 2 users
- 2024-10-23: CountInTol - 134 operations by 1 users
- 2024-10-23: Condition - 86 operations by 3 users
- 2024-10-23: CountNotFound - 72 operations by 5 users
- 2024-10-23: StandBy - 63 operations by 13 users
- 2024-10-23: Inbound - 58 operations by 5 users
- 2024-10-23: CountCreation - 44 operations by 12 users
- 2024-10-23: Quantity - 38 operations by 4 users
- 2024-10-23: ReconcileIn - 28 operations by 8 users
- 2024-10-23: AutomaticCondition - 26 operations by 1 users
- 2024-10-23: LoadHandlingMaterialAdj - 22 operations by 2 users
- 2024-10-23: ChangeLabel - 16 operations by 3 users
- 2024-10-23: Consolidate - 12 operations by 2 users
- 2024-10-23: MoveTE - 8 operations by 2 users
- 2024-10-23: ConsolidateLicensePlate - 4 operations by 2 users
- 2024-10-23: ReconcileOut - 4 operations by 1 users
- 2024-10-23: Scrap - 3 operations by 1 users
- 2024-10-23: Dimension - 2 operations by 1 users
- 2024-10-22: Pick - 16322 operations by 67 users
- 2024-10-22: DropPick - 9952 operations by 67 users
- 2024-10-22: Ship - 9785 operations by 5 users
- 2024-10-22: Receive - 6540 operations by 14 users
- 2024-10-22: Load - 6266 operations by 12 users
- 2024-10-22: MoveOut - 6036 operations by 48 users
- 2024-10-22: PickingHandlingMaterialAdj - 4574 operations by 5 users
- 2024-10-22: MoveIn - 3321 operations by 46 users
- 2024-10-22: Putaway - 2356 operations by 36 users
- 2024-10-22: DropReceive - 2074 operations by 9 users
- 2024-10-22: ReplenishIn - 566 operations by 8 users
- 2024-10-22: Move - 336 operations by 9 users
- 2024-10-22: Cancel - 219 operations by 23 users
- 2024-10-22: CountOutTol - 165 operations by 3 users
- 2024-10-22: Creation - 149 operations by 1 users
- 2024-10-22: Quantity - 128 operations by 4 users
- 2024-10-22: CountNotFound - 109 operations by 3 users
- 2024-10-22: CountInTol - 102 operations by 1 users
- 2024-10-22: StandBy - 73 operations by 16 users
- 2024-10-22: Condition - 72 operations by 4 users
- 2024-10-22: Unpick - 70 operations by 1 users
- 2024-10-22: Inbound - 58 operations by 7 users
- 2024-10-22: AutomaticCondition - 56 operations by 1 users
- 2024-10-22: Scrap - 51 operations by 6 users
- 2024-10-22: CountCreation - 38 operations by 8 users
- 2024-10-22: ReconcileIn - 10 operations by 3 users
- 2024-10-22: Reclassify - 9 operations by 1 users
- 2024-10-22: ChangeLabel - 6 operations by 2 users
- 2024-10-22: LoadHandlingMaterialAdj - 6 operations by 1 users
- 2024-10-22: Consolidate - 4 operations by 2 users
- 2024-10-22: Dimension - 4 operations by 3 users
- 2024-10-22: CountFound - 2 operations by 1 users
- 2024-10-22: MoveTE - 2 operations by 2 users
- 2024-10-22: ProductionConsume - 2 operations by 1 users
- 2024-10-22: ProductionOutput - 2 operations by 1 users
- 2024-10-22: ReconcileOut - 2 operations by 1 users
- 2024-10-22: ProductionStart - 1 operations by 1 users
- 2024-10-21: Pick - 15525 operations by 79 users
- 2024-10-21: Ship - 9689 operations by 7 users
- 2024-10-21: DropPick - 9126 operations by 78 users
- 2024-10-21: Load - 6754 operations by 14 users
- 2024-10-21: MoveOut - 5659 operations by 49 users
- 2024-10-21: Receive - 5020 operations by 14 users
- 2024-10-21: MoveIn - 3292 operations by 47 users
- 2024-10-21: PickingHandlingMaterialAdj - 3142 operations by 7 users
- 2024-10-21: Putaway - 1990 operations by 33 users
- 2024-10-21: DropReceive - 1692 operations by 9 users
- 2024-10-21: Creation - 589 operations by 1 users
- 2024-10-21: ReplenishIn - 504 operations by 14 users
- 2024-10-21: Cancel - 297 operations by 23 users
- 2024-10-21: Move - 290 operations by 10 users
- 2024-10-21: Reclassify - 288 operations by 3 users
- 2024-10-21: Quantity - 276 operations by 4 users
- 2024-10-21: CountOutTol - 165 operations by 1 users
- 2024-10-21: LoadHandlingMaterialAdj - 92 operations by 3 users
- 2024-10-21: CountCreation - 71 operations by 7 users
- 2024-10-21: CountNotFound - 64 operations by 1 users
- 2024-10-21: StandBy - 56 operations by 15 users
- 2024-10-21: CountInTol - 54 operations by 2 users
- 2024-10-21: Inbound - 49 operations by 7 users
- 2024-10-21: ReconcileIn - 46 operations by 8 users
- 2024-10-21: AutomaticCondition - 44 operations by 1 users
- 2024-10-21: Consolidate - 39 operations by 3 users
- 2024-10-21: Condition - 34 operations by 2 users
- 2024-10-21: Scrap - 19 operations by 2 users
- 2024-10-21: Dimension - 13 operations by 4 users
- 2024-10-21: ChangeLabel - 10 operations by 3 users
- 2024-10-21: ConsolidateLicensePlate - 6 operations by 3 users
- 2024-10-21: CountFound - 2 operations by 1 users
- 2024-10-21: MoveTE - 2 operations by 1 users
- 2024-10-21: ReconcileOut - 2 operations by 1 users
- 2024-10-21: Unload - 2 operations by 1 users
- 2024-10-20: Pick - 13154 operations by 61 users
- 2024-10-20: DropPick - 7725 operations by 61 users
- 2024-10-20: Ship - 7511 operations by 2 users
- 2024-10-20: Load - 6690 operations by 10 users
- 2024-10-20: Receive - 4686 operations by 9 users
- 2024-10-20: PickingHandlingMaterialAdj - 2908 operations by 2 users
- 2024-10-20: MoveOut - 2843 operations by 35 users
- 2024-10-20: Putaway - 1560 operations by 24 users
- 2024-10-20: DropReceive - 1542 operations by 7 users
- 2024-10-20: MoveIn - 1158 operations by 35 users
- 2024-10-20: ReplenishIn - 376 operations by 10 users
- 2024-10-20: Cancel - 266 operations by 18 users
- 2024-10-20: Move - 237 operations by 3 users
- 2024-10-20: Reclassify - 138 operations by 2 users
- 2024-10-20: Condition - 102 operations by 3 users
- 2024-10-20: Quantity - 102 operations by 4 users
- 2024-10-20: AutomaticCondition - 48 operations by 1 users
- 2024-10-20: StandBy - 41 operations by 10 users
- 2024-10-20: LoadHandlingMaterialAdj - 28 operations by 1 users
- 2024-10-20: Inbound - 24 operations by 2 users
- 2024-10-20: CountCreation - 16 operations by 4 users
- 2024-10-20: MoveTE - 11 operations by 2 users
- 2024-10-20: ReconcileIn - 8 operations by 4 users
- 2024-10-20: CountOutTol - 7 operations by 2 users
- 2024-10-20: Consolidate - 6 operations by 1 users
- 2024-10-20: CountNotFound - 4 operations by 2 users
- 2024-10-20: Unload - 4 operations by 2 users
- 2024-10-20: ChangeLabel - 2 operations by 1 users
- 2024-10-20: CountInTol - 2 operations by 1 users
- 2024-10-20: Dimension - 2 operations by 1 users
- 2024-10-19: Pick - 14915 operations by 57 users
- 2024-10-19: Ship - 9284 operations by 2 users
- 2024-10-19: DropPick - 8501 operations by 55 users
- 2024-10-19: Receive - 6218 operations by 10 users
- 2024-10-19: Load - 6087 operations by 11 users
- 2024-10-19: MoveOut - 5316 operations by 39 users
- 2024-10-19: MoveIn - 3297 operations by 37 users
- 2024-10-19: PickingHandlingMaterialAdj - 3294 operations by 2 users
- 2024-10-19: DropReceive - 2052 operations by 8 users
- 2024-10-19: Putaway - 1998 operations by 26 users
- 2024-10-19: ReplenishIn - 390 operations by 9 users
- 2024-10-19: Move - 265 operations by 3 users
- 2024-10-19: Cancel - 139 operations by 15 users
- 2024-10-19: StandBy - 62 operations by 9 users
- 2024-10-19: Inbound - 51 operations by 3 users
- 2024-10-19: CountCreation - 49 operations by 7 users
- 2024-10-19: LoadHandlingMaterialAdj - 38 operations by 2 users
- 2024-10-19: AutomaticCondition - 32 operations by 1 users
- 2024-10-19: ProductionOutput - 32 operations by 1 users
- 2024-10-19: Quantity - 32 operations by 2 users
- 2024-10-19: Condition - 20 operations by 3 users
- 2024-10-19: ProductionConsume - 17 operations by 1 users
- 2024-10-19: MoveTE - 14 operations by 2 users
- 2024-10-19: ReconcileIn - 12 operations by 4 users
- 2024-10-19: ChangeLabel - 6 operations by 2 users
- 2024-10-19: ConsolidateLicensePlate - 6 operations by 2 users
- 2024-10-19: CountOutTol - 6 operations by 3 users
- 2024-10-19: Creation - 6 operations by 1 users
- 2024-10-19: CountInTol - 2 operations by 1 users
- 2024-10-19: CountNotFound - 2 operations by 1 users
- 2024-10-19: Scrap - 2 operations by 2 users
- 2024-10-19: ProductionStart - 1 operations by 1 users
- 2024-10-18: Pick - 17430 operations by 77 users
- 2024-10-18: Ship - 10198 operations by 7 users
- 2024-10-18: DropPick - 10093 operations by 75 users
- 2024-10-18: Load - 7074 operations by 11 users
- 2024-10-18: Receive - 6952 operations by 13 users
- 2024-10-18: MoveOut - 6273 operations by 47 users
- 2024-10-18: MoveIn - 3424 operations by 46 users
- 2024-10-18: PickingHandlingMaterialAdj - 2574 operations by 7 users
- 2024-10-18: Putaway - 2536 operations by 31 users
- 2024-10-18: DropReceive - 2306 operations by 10 users
- 2024-10-18: ReplenishIn - 624 operations by 11 users
- 2024-10-18: Move - 346 operations by 10 users
- 2024-10-18: Creation - 304 operations by 1 users
- 2024-10-18: Cancel - 207 operations by 25 users
- 2024-10-18: CountOutTol - 177 operations by 2 users
- 2024-10-18: CountNotFound - 163 operations by 2 users
- 2024-10-18: CountInTol - 108 operations by 1 users
- 2024-10-18: StandBy - 60 operations by 14 users
- 2024-10-18: Inbound - 58 operations by 4 users
- 2024-10-18: Condition - 50 operations by 3 users
- 2024-10-18: Unpick - 46 operations by 1 users
- 2024-10-18: AutomaticCondition - 30 operations by 1 users
- 2024-10-18: CountCreation - 28 operations by 10 users
- 2024-10-18: LoadHandlingMaterialAdj - 16 operations by 2 users
- 2024-10-18: ReconcileIn - 16 operations by 5 users
- 2024-10-18: Scrap - 16 operations by 2 users
- 2024-10-18: MoveTE - 14 operations by 3 users
- 2024-10-18: ChangeLabel - 4 operations by 2 users
- 2024-10-18: Quantity - 4 operations by 2 users
- 2024-10-18: ConsolidateLicensePlate - 2 operations by 1 users
- 2024-10-17: Pick - 16764 operations by 77 users
- 2024-10-17: Ship - 11308 operations by 4 users
- 2024-10-17: DropPick - 10259 operations by 76 users
- 2024-10-17: Load - 8022 operations by 11 users
- 2024-10-17: Receive - 7516 operations by 12 users
- 2024-10-17: MoveOut - 6435 operations by 52 users
- 2024-10-17: PickingHandlingMaterialAdj - 3688 operations by 4 users
- 2024-10-17: MoveIn - 3537 operations by 49 users
- 2024-10-17: Putaway - 2674 operations by 35 users
- 2024-10-17: DropReceive - 2504 operations by 10 users
- 2024-10-17: ReplenishIn - 542 operations by 9 users
- 2024-10-17: Move - 350 operations by 6 users
- 2024-10-17: Cancel - 206 operations by 22 users
- 2024-10-17: CountOutTol - 197 operations by 3 users
- 2024-10-17: CountNotFound - 131 operations by 3 users
- 2024-10-17: Creation - 113 operations by 1 users
- 2024-10-17: CountInTol - 86 operations by 2 users
- 2024-10-17: StandBy - 74 operations by 15 users
- 2024-10-17: Inbound - 60 operations by 4 users
- 2024-10-17: CountCreation - 57 operations by 9 users
- 2024-10-17: LoadHandlingMaterialAdj - 48 operations by 2 users
- 2024-10-17: AutomaticCondition - 46 operations by 1 users
- 2024-10-17: ConsolidateLicensePlate - 22 operations by 5 users
- 2024-10-17: Quantity - 16 operations by 5 users
- 2024-10-17: MoveTE - 12 operations by 3 users
- 2024-10-17: ReconcileIn - 12 operations by 3 users
- 2024-10-17: ChangeLabel - 10 operations by 3 users
- 2024-10-17: Scrap - 9 operations by 2 users
- 2024-10-17: Consolidate - 6 operations by 3 users
- 2024-10-17: Dimension - 2 operations by 2 users
- 2024-10-17: ReconcileOut - 2 operations by 1 users
- 2024-10-16: Pick - 17200 operations by 83 users
- 2024-10-16: Ship - 10262 operations by 4 users
- 2024-10-16: DropPick - 9900 operations by 82 users
- 2024-10-16: Load - 7258 operations by 14 users
- 2024-10-16: MoveOut - 6133 operations by 51 users
- 2024-10-16: Receive - 5586 operations by 11 users
- 2024-10-16: MoveIn - 3561 operations by 48 users
- 2024-10-16: PickingHandlingMaterialAdj - 2644 operations by 4 users
- 2024-10-16: Putaway - 2112 operations by 28 users
- 2024-10-16: DropReceive - 1818 operations by 9 users
- 2024-10-16: Creation - 648 operations by 1 users
- 2024-10-16: ReplenishIn - 608 operations by 12 users
- 2024-10-16: Move - 344 operations by 6 users
- 2024-10-16: Cancel - 328 operations by 21 users
- 2024-10-16: CountOutTol - 225 operations by 2 users
- 2024-10-16: Quantity - 166 operations by 5 users
- 2024-10-16: CountInTol - 145 operations by 2 users
- 2024-10-16: Condition - 90 operations by 3 users
- 2024-10-16: CountNotFound - 64 operations by 3 users
- 2024-10-16: StandBy - 63 operations by 13 users
- 2024-10-16: CountCreation - 54 operations by 9 users
- 2024-10-16: Inbound - 51 operations by 3 users
- 2024-10-16: LoadHandlingMaterialAdj - 46 operations by 2 users
- 2024-10-16: Dimension - 33 operations by 2 users
- 2024-10-16: AutomaticCondition - 32 operations by 1 users
- 2024-10-16: MoveTE - 17 operations by 3 users
- 2024-10-16: ReconcileIn - 8 operations by 3 users
- 2024-10-16: Scrap - 8 operations by 2 users
- 2024-10-16: ChangeLabel - 6 operations by 2 users
- 2024-10-16: ProductionConsume - 4 operations by 1 users
- 2024-10-16: ProductionOutput - 4 operations by 1 users
- 2024-10-16: ConsolidateLicensePlate - 2 operations by 1 users
- 2024-10-16: ProductionStart - 2 operations by 1 users
- 2024-10-16: ReconcileOut - 2 operations by 1 users
- 2024-10-16: Consolidate - 1 operations by 1 users
- 2024-10-15: Pick - 14427 operations by 68 users
- 2024-10-15: DropPick - 8933 operations by 68 users
- 2024-10-15: Ship - 8213 operations by 5 users
- 2024-10-15: MoveOut - 5639 operations by 44 users
- 2024-10-15: Receive - 5344 operations by 10 users
- 2024-10-15: Load - 4482 operations by 10 users
- 2024-10-15: MoveIn - 3255 operations by 39 users
- 2024-10-15: PickingHandlingMaterialAdj - 2470 operations by 4 users
- 2024-10-15: Putaway - 2114 operations by 29 users
- 2024-10-15: DropReceive - 1766 operations by 8 users
- 2024-10-15: ReplenishIn - 494 operations by 8 users
- 2024-10-15: Move - 360 operations by 8 users
- 2024-10-15: Cancel - 251 operations by 16 users
- 2024-10-15: CountOutTol - 189 operations by 1 users
- 2024-10-15: CountNotFound - 171 operations by 3 users
- 2024-10-15: Creation - 95 operations by 1 users
- 2024-10-15: CountCreation - 92 operations by 7 users
- 2024-10-15: CountInTol - 88 operations by 1 users
- 2024-10-15: StandBy - 63 operations by 10 users
- 2024-10-15: AutomaticCondition - 62 operations by 1 users
- 2024-10-15: Inbound - 60 operations by 5 users
- 2024-10-15: Condition - 58 operations by 3 users
- 2024-10-15: Scrap - 58 operations by 4 users
- 2024-10-15: LoadHandlingMaterialAdj - 42 operations by 2 users
- 2024-10-15: Quantity - 36 operations by 4 users
- 2024-10-15: MoveTE - 16 operations by 3 users
- 2024-10-15: ConsolidateLicensePlate - 10 operations by 4 users
- 2024-10-15: ReconcileIn - 10 operations by 3 users
- 2024-10-15: ChangeLabel - 6 operations by 3 users
- 2024-10-15: ReconcileOut - 6 operations by 2 users
- 2024-10-15: Unpick - 4 operations by 2 users
- 2024-10-15: Dimension - 3 operations by 3 users
- 2024-10-15: CountFound - 2 operations by 1 users
- 2024-10-15: Unload - 2 operations by 1 users
- 2024-10-14: Pick - 13514 operations by 66 users
- 2024-10-14: Ship - 8381 operations by 3 users
- 2024-10-14: DropPick - 8221 operations by 64 users
- 2024-10-14: Load - 7047 operations by 12 users
- 2024-10-14: Receive - 4110 operations by 10 users
- 2024-10-14: PickingHandlingMaterialAdj - 3372 operations by 3 users
- 2024-10-14: MoveOut - 2934 operations by 47 users
- 2024-10-14: Putaway - 1416 operations by 25 users
- 2024-10-14: DropReceive - 1386 operations by 10 users
- 2024-10-14: MoveIn - 989 operations by 38 users
- 2024-10-14: Creation - 903 operations by 1 users
- 2024-10-14: ReplenishIn - 464 operations by 10 users
- 2024-10-14: Cancel - 280 operations by 22 users
- 2024-10-14: CountOutTol - 241 operations by 2 users
- 2024-10-14: Move - 232 operations by 4 users
- 2024-10-14: CountInTol - 106 operations by 1 users
- 2024-10-14: CountNotFound - 97 operations by 2 users
- 2024-10-14: CountCreation - 87 operations by 5 users
- 2024-10-14: StandBy - 44 operations by 13 users
- 2024-10-14: Unload - 37 operations by 1 users
- 2024-10-14: Reclassify - 30 operations by 2 users
- 2024-10-14: Inbound - 24 operations by 3 users
- 2024-10-14: AutomaticCondition - 20 operations by 1 users
- 2024-10-14: LoadHandlingMaterialAdj - 18 operations by 1 users
- 2024-10-14: MoveTE - 11 operations by 2 users
- 2024-10-14: Condition - 10 operations by 1 users
- 2024-10-14: ReconcileIn - 10 operations by 3 users
- 2024-10-14: Quantity - 6 operations by 3 users
- 2024-10-14: ChangeLabel - 4 operations by 1 users
- 2024-10-14: ConsolidateLicensePlate - 4 operations by 2 users
- 2024-10-14: ReconcileOut - 2 operations by 1 users
- 2024-10-14: Scrap - 1 operations by 1 users
- 2024-10-13: Pick - 8941 operations by 48 users
- 2024-10-13: DropPick - 5367 operations by 48 users
- 2024-10-13: Ship - 5316 operations by 2 users
- 2024-10-13: Receive - 5114 operations by 11 users
- 2024-10-13: Load - 4539 operations by 10 users
- 2024-10-13: MoveOut - 2844 operations by 39 users
- 2024-10-13: PickingHandlingMaterialAdj - 2302 operations by 2 users
- 2024-10-13: Putaway - 1852 operations by 30 users
- 2024-10-13: DropReceive - 1684 operations by 10 users
- 2024-10-13: MoveIn - 639 operations by 33 users
- 2024-10-13: ReplenishIn - 358 operations by 12 users
- 2024-10-13: Move - 249 operations by 5 users
- 2024-10-13: Cancel - 240 operations by 22 users
- 2024-10-13: StandBy - 48 operations by 10 users
- 2024-10-13: Inbound - 22 operations by 2 users
- 2024-10-13: AutomaticCondition - 18 operations by 1 users
- 2024-10-13: CountCreation - 16 operations by 7 users
- 2024-10-13: Condition - 14 operations by 1 users
- 2024-10-13: MoveTE - 13 operations by 3 users
- 2024-10-13: LoadHandlingMaterialAdj - 12 operations by 2 users
- 2024-10-13: CountOutTol - 10 operations by 1 users
- 2024-10-13: ReconcileIn - 8 operations by 4 users
- 2024-10-13: Quantity - 2 operations by 1 users
- 2024-10-13: Creation - 1 operations by 1 users
- 2024-10-13: Scrap - 1 operations by 1 users
- 2024-10-12: Pick - 14124 operations by 64 users
- 2024-10-12: Ship - 9935 operations by 4 users
- 2024-10-12: Receive - 9002 operations by 9 users
- 2024-10-12: DropPick - 8558 operations by 64 users
- 2024-10-12: Load - 6662 operations by 9 users
- 2024-10-12: MoveOut - 6447 operations by 49 users
- 2024-10-12: PickingHandlingMaterialAdj - 3714 operations by 4 users
- 2024-10-12: MoveIn - 3067 operations by 38 users
- 2024-10-12: Putaway - 3048 operations by 37 users
- 2024-10-12: DropReceive - 2976 operations by 8 users
- 2024-10-12: ReplenishIn - 558 operations by 12 users
- 2024-10-12: Move - 322 operations by 2 users
- 2024-10-12: Cancel - 232 operations by 24 users
- 2024-10-12: StandBy - 92 operations by 10 users
- 2024-10-12: LoadHandlingMaterialAdj - 60 operations by 2 users
- 2024-10-12: Inbound - 41 operations by 2 users
- 2024-10-12: CountCreation - 25 operations by 9 users
- 2024-10-12: AutomaticCondition - 24 operations by 1 users
- 2024-10-12: ProductionOutput - 24 operations by 1 users
- 2024-10-12: Condition - 20 operations by 2 users
- 2024-10-12: ReconcileIn - 20 operations by 5 users
- 2024-10-12: CountNotFound - 15 operations by 6 users
- 2024-10-12: MoveTE - 14 operations by 2 users
- 2024-10-12: ProductionConsume - 13 operations by 1 users
- 2024-10-12: CountOutTol - 8 operations by 3 users
- 2024-10-12: ChangeLabel - 6 operations by 2 users
- 2024-10-12: ConsolidateLicensePlate - 6 operations by 2 users
- 2024-10-12: Quantity - 6 operations by 2 users
- 2024-10-12: Dimension - 4 operations by 4 users
- 2024-10-12: CountInTol - 2 operations by 1 users
- 2024-10-12: Creation - 2 operations by 1 users
- 2024-10-12: Consolidate - 1 operations by 1 users
- 2024-10-12: ProductionStart - 1 operations by 1 users
- 2024-10-12: Scrap - 1 operations by 1 users
- 2024-10-11: Pick - 20660 operations by 87 users
- 2024-10-11: Ship - 12764 operations by 5 users
- 2024-10-11: DropPick - 12244 operations by 87 users
- 2024-10-11: Load - 9030 operations by 14 users
- 2024-10-11: MoveOut - 6914 operations by 50 users
- 2024-10-11: Receive - 6610 operations by 13 users
- 2024-10-11: PickingHandlingMaterialAdj - 5786 operations by 5 users
- 2024-10-11: MoveIn - 4180 operations by 52 users
- 2024-10-11: Putaway - 2382 operations by 31 users
- 2024-10-11: DropReceive - 2194 operations by 11 users
- 2024-10-11: ReplenishIn - 738 operations by 17 users
- 2024-10-11: Move - 335 operations by 9 users
- 2024-10-11: Cancel - 185 operations by 17 users
- 2024-10-11: CountNotFound - 87 operations by 7 users
- 2024-10-11: StandBy - 73 operations by 16 users
- 2024-10-11: Inbound - 64 operations by 5 users
- 2024-10-11: CountCreation - 42 operations by 10 users
- 2024-10-11: LoadHandlingMaterialAdj - 32 operations by 2 users
- 2024-10-11: AutomaticCondition - 30 operations by 1 users
- 2024-10-11: Creation - 15 operations by 1 users
- 2024-10-11: MoveTE - 14 operations by 3 users
- 2024-10-11: Scrap - 14 operations by 1 users
- 2024-10-11: ReconcileIn - 8 operations by 4 users
- 2024-10-11: Quantity - 6 operations by 3 users
- 2024-10-11: ChangeLabel - 4 operations by 1 users
- 2024-10-11: Dimension - 3 operations by 2 users
- 2024-10-11: Condition - 2 operations by 1 users
- 2024-10-11: CountInTol - 2 operations by 1 users
- 2024-10-11: CountOutTol - 2 operations by 1 users
- 2024-10-10: Pick - 18768 operations by 86 users
- 2024-10-10: DropPick - 11431 operations by 86 users
- 2024-10-10: Ship - 11172 operations by 7 users
- 2024-10-10: Load - 7824 operations by 14 users
- 2024-10-10: Receive - 7116 operations by 10 users
- 2024-10-10: MoveOut - 6886 operations by 53 users
- 2024-10-10: PickingHandlingMaterialAdj - 4954 operations by 5 users
- 2024-10-10: MoveIn - 3661 operations by 41 users
- 2024-10-10: Putaway - 2674 operations by 36 users
- 2024-10-10: DropReceive - 2392 operations by 8 users
- 2024-10-10: ReplenishIn - 666 operations by 17 users
- 2024-10-10: Move - 370 operations by 6 users
- 2024-10-10: Cancel - 312 operations by 19 users
- 2024-10-10: CountOutTol - 130 operations by 2 users
- 2024-10-10: StandBy - 70 operations by 16 users
- 2024-10-10: Inbound - 66 operations by 5 users
- 2024-10-10: CountInTol - 57 operations by 2 users
- 2024-10-10: CountNotFound - 54 operations by 1 users
- 2024-10-10: CountCreation - 34 operations by 6 users
- 2024-10-10: Quantity - 32 operations by 6 users
- 2024-10-10: Unload - 17 operations by 1 users
- 2024-10-10: AutomaticCondition - 16 operations by 1 users
- 2024-10-10: LoadHandlingMaterialAdj - 14 operations by 1 users
- 2024-10-10: MoveTE - 12 operations by 3 users
- 2024-10-10: Creation - 10 operations by 1 users
- 2024-10-10: Condition - 8 operations by 2 users
- 2024-10-10: ConsolidateLicensePlate - 8 operations by 2 users
- 2024-10-10: Scrap - 8 operations by 1 users
- 2024-10-10: Consolidate - 7 operations by 1 users
- 2024-10-10: ChangeLabel - 6 operations by 1 users
- 2024-10-10: ReconcileIn - 6 operations by 3 users
- 2024-10-09: Pick - 17040 operations by 81 users
- 2024-10-09: Ship - 10805 operations by 5 users
- 2024-10-09: DropPick - 10180 operations by 81 users
- 2024-10-09: Load - 7243 operations by 12 users
- 2024-10-09: Receive - 6298 operations by 9 users
- 2024-10-09: MoveOut - 5963 operations by 52 users
- 2024-10-09: PickingHandlingMaterialAdj - 4116 operations by 5 users
- 2024-10-09: MoveIn - 3209 operations by 46 users
- 2024-10-09: Putaway - 2330 operations by 29 users
- 2024-10-09: DropReceive - 2118 operations by 8 users
- 2024-10-09: ReplenishIn - 630 operations by 11 users
- 2024-10-09: Move - 309 operations by 6 users
- 2024-10-09: Cancel - 202 operations by 24 users
- 2024-10-09: CountOutTol - 173 operations by 2 users
- 2024-10-09: Creation - 165 operations by 1 users
- 2024-10-09: CountInTol - 148 operations by 1 users
- 2024-10-09: Quantity - 79 operations by 4 users
- 2024-10-09: StandBy - 65 operations by 12 users
- 2024-10-09: Condition - 64 operations by 3 users
- 2024-10-09: CountCreation - 57 operations by 7 users
- 2024-10-09: Inbound - 50 operations by 4 users
- 2024-10-09: CountNotFound - 41 operations by 3 users
- 2024-10-09: LoadHandlingMaterialAdj - 38 operations by 2 users
- 2024-10-09: MoveTE - 23 operations by 2 users
- 2024-10-09: ReconcileIn - 20 operations by 6 users
- 2024-10-09: Dimension - 16 operations by 2 users
- 2024-10-09: AutomaticCondition - 14 operations by 1 users
- 2024-10-09: ChangeLabel - 6 operations by 3 users
- 2024-10-09: Scrap - 4 operations by 2 users
- 2024-10-09: ReconcileOut - 2 operations by 1 users
- 2024-10-09: Consolidate - 1 operations by 1 users
- 2024-10-08: Pick - 15582 operations by 70 users
- 2024-10-08: DropPick - 9536 operations by 69 users
- 2024-10-08: Ship - 9050 operations by 6 users
- 2024-10-08: MoveOut - 6518 operations by 49 users
- 2024-10-08: Receive - 6156 operations by 10 users
- 2024-10-08: Load - 5984 operations by 8 users
- 2024-10-08: MoveIn - 3923 operations by 41 users
- 2024-10-08: PickingHandlingMaterialAdj - 3602 operations by 6 users
- 2024-10-08: Putaway - 2094 operations by 30 users
- 2024-10-08: DropReceive - 2000 operations by 7 users
- 2024-10-08: ReplenishIn - 678 operations by 11 users
- 2024-10-08: Move - 286 operations by 6 users
- 2024-10-08: Cancel - 250 operations by 20 users
- 2024-10-08: CountNotFound - 169 operations by 4 users
- 2024-10-08: CountOutTol - 145 operations by 3 users
- 2024-10-08: LoadHandlingMaterialAdj - 82 operations by 4 users
- 2024-10-08: CountInTol - 81 operations by 2 users
- 2024-10-08: CountCreation - 69 operations by 5 users
- 2024-10-08: StandBy - 66 operations by 13 users
- 2024-10-08: Condition - 64 operations by 4 users
- 2024-10-08: Quantity - 58 operations by 3 users
- 2024-10-08: Inbound - 54 operations by 5 users
- 2024-10-08: Unpick - 40 operations by 2 users
- 2024-10-08: Scrap - 18 operations by 5 users
- 2024-10-08: Consolidate - 17 operations by 2 users
- 2024-10-08: AutomaticCondition - 16 operations by 1 users
- 2024-10-08: Creation - 14 operations by 1 users
- 2024-10-08: MoveTE - 13 operations by 3 users
- 2024-10-08: ReconcileIn - 12 operations by 4 users
- 2024-10-08: ChangeLabel - 10 operations by 2 users
- 2024-10-08: ConsolidateLicensePlate - 8 operations by 3 users
- 2024-10-08: Unload - 4 operations by 1 users
- 2024-10-08: Dimension - 3 operations by 1 users
- 2024-10-08: ReconcileOut - 2 operations by 1 users
- 2024-10-07: Pick - 1587 operations by 36 users
- 2024-10-07: DropPick - 1101 operations by 35 users
- 2024-10-07: Ship - 995 operations by 2 users
- 2024-10-07: Load - 645 operations by 6 users
- 2024-10-07: PickingHandlingMaterialAdj - 522 operations by 2 users
- 2024-10-07: Receive - 492 operations by 1 users
- 2024-10-07: MoveOut - 380 operations by 11 users
- 2024-10-07: Putaway - 234 operations by 7 users
- 2024-10-07: DropReceive - 150 operations by 1 users
- 2024-10-07: MoveIn - 117 operations by 8 users
- 2024-10-07: ReplenishIn - 46 operations by 3 users
- 2024-10-07: Cancel - 30 operations by 3 users
- 2024-10-07: Move - 26 operations by 3 users
- 2024-10-07: CountNotFound - 8 operations by 1 users
- 2024-10-07: LoadHandlingMaterialAdj - 6 operations by 1 users
- 2024-10-07: Creation - 4 operations by 1 users
- 2024-10-07: Consolidate - 3 operations by 1 users
- 2024-10-07: MoveTE - 3 operations by 1 users
- 2024-10-07: StandBy - 3 operations by 1 users

---


## 9. Order Processing Performance

Analyzes order processing times and completion rates

Order processing performance:

- 2024-10-30: 30 orders, avg processing time -28837460.3 minutes, 0 completed, 0 cancelled
- 2024-10-29: 8497 orders, avg processing time -8565537.5 minutes, 2188 completed, 56 cancelled
- 2024-10-28: 6508 orders, avg processing time -48126.8 minutes, 6079 completed, 124 cancelled
- 2024-10-27: 3376 orders, avg processing time -732943.1 minutes, 3216 completed, 69 cancelled
- 2024-10-26: 9179 orders, avg processing time -17604.6 minutes, 9083 completed, 85 cancelled
- 2024-10-25: 7813 orders, avg processing time -6642.6 minutes, 7688 completed, 120 cancelled
- 2024-10-24: 9481 orders, avg processing time -17436.9 minutes, 9276 completed, 167 cancelled
- 2024-10-23: 7596 orders, avg processing time -33548.4 minutes, 7438 completed, 144 cancelled
- 2024-10-22: 7292 orders, avg processing time -38847.8 minutes, 7137 completed, 142 cancelled
- 2024-10-21: 8311 orders, avg processing time -13182.7 minutes, 8020 completed, 287 cancelled
- 2024-10-20: 2523 orders, avg processing time -78776.9 minutes, 2439 completed, 76 cancelled
- 2024-10-19: 9612 orders, avg processing time -4664.0 minutes, 9429 completed, 181 cancelled
- 2024-10-18: 8352 orders, avg processing time -6160.1 minutes, 8270 completed, 80 cancelled
- 2024-10-17: 8789 orders, avg processing time 664.0 minutes, 8612 completed, 177 cancelled
- 2024-10-16: 9833 orders, avg processing time -11073.5 minutes, 9384 completed, 445 cancelled
- 2024-10-15: 6722 orders, avg processing time 620.3 minutes, 6430 completed, 292 cancelled
- 2024-10-14: 6233 orders, avg processing time 578.9 minutes, 5954 completed, 279 cancelled
- 2024-10-13: 4919 orders, avg processing time 1144.2 minutes, 4803 completed, 116 cancelled
- 2024-10-12: 6094 orders, avg processing time 799.1 minutes, 5889 completed, 205 cancelled
- 2024-10-11: 7124 orders, avg processing time 559.7 minutes, 6831 completed, 293 cancelled
- 2024-10-10: 9100 orders, avg processing time 741.1 minutes, 8565 completed, 535 cancelled
- 2024-10-09: 9235 orders, avg processing time -2391.3 minutes, 8519 completed, 715 cancelled
- 2024-10-08: 7206 orders, avg processing time -3227.0 minutes, 6711 completed, 493 cancelled
- 2024-10-07: 1683 orders, avg processing time 1332.0 minutes, 1585 completed, 98 cancelled

---


## 10. Inventory Movement Patterns

Analyzes patterns in inventory movements

Inventory movement patterns:

- Pick: 347557 movements, 185635 unique items, avg quantity 56.2
- Ship: 213458 movements, 212694 unique items, avg quantity 45.3
- DropPick: 207448 movements, 207445 unique items, avg quantity 46.0
- Load: 150680 movements, 150102 unique items, avg quantity 49.0
- Receive: 136026 movements, 68014 unique items, avg quantity 149.1
- MoveOut: 122109 movements, 68407 unique items, avg quantity 288.0
- PickingHandlingMaterialAdj: 77968 movements, 38985 unique items, avg quantity -25.3
- MoveIn: 66093 movements, 53178 unique items, avg quantity 84.3
- Putaway: 49220 movements, 24535 unique items, avg quantity 371.7
- DropReceive: 44868 movements, 22435 unique items, avg quantity 387.9
- ReplenishIn: 11916 movements, 5959 unique items, avg quantity 478.4
- Move: 6706 movements, 560 unique items, avg quantity 0.0
- Cancel: 5261 movements, 1839 unique items, avg quantity 1323.7
- Creation: 4518 movements, 4518 unique items, avg quantity 199.4
- CountOutTol: 2806 movements, 1435 unique items, avg quantity 71.5
- CountNotFound: 1895 movements, 1157 unique items, avg quantity -200.8
- CountInTol: 1539 movements, 713 unique items, avg quantity -0.3
- Quantity: 1369 movements, 676 unique items, avg quantity -186.4
- StandBy: 1359 movements, 427 unique items, avg quantity 0.0
- CountCreation: 1136 movements, 1135 unique items, avg quantity 303.2
- Condition: 1122 movements, 416 unique items, avg quantity 257.0
- Inbound: 1065 movements, 415 unique items, avg quantity 0.0
- LoadHandlingMaterialAdj: 850 movements, 426 unique items, avg quantity -32.6
- Reclassify: 684 movements, 438 unique items, avg quantity 207.9
- AutomaticCondition: 660 movements, 311 unique items, avg quantity 154.5
- MoveTE: 635 movements, 344 unique items, avg quantity 43.2
- Unload: 550 movements, 550 unique items, avg quantity 33.6
- Scrap: 361 movements, 214 unique items, avg quantity 264.6
- ReconcileIn: 354 movements, 177 unique items, avg quantity -318.9
- Unpick: 164 movements, 83 unique items, avg quantity 118.4
- ChangeLabel: 126 movements, 64 unique items, avg quantity 475.3
- Dimension: 125 movements, 123 unique items, avg quantity 438.9
- Consolidate: 120 movements, 120 unique items, avg quantity 49.1
- ConsolidateLicensePlate: 104 movements, 48 unique items, avg quantity 2816.6

---


## 11. Material Adjustments Analysis

Analyzes patterns in inventory adjustments

Material adjustments analysis:

- 2024-10-30: MoveIn - 2413 adjustments, 2413.0 positive, 0.0 negative, avg adjustment size 72.7
- 2024-10-30: MoveOut - 2270 adjustments, 0.0 positive, 2270.0 negative, avg adjustment size 69.8
- 2024-10-30: PositiveAdj - 75 adjustments, 75.0 positive, 0.0 negative, avg adjustment size 19.8
- 2024-10-30: NegativeAdj - 69 adjustments, 0.0 positive, 69.0 negative, avg adjustment size 15.8
- 2024-10-29: MoveIn - 45901 adjustments, 45901.0 positive, 0.0 negative, avg adjustment size 91.4
- 2024-10-29: MoveOut - 42446 adjustments, 0.0 positive, 42446.0 negative, avg adjustment size 87.0
- 2024-10-29: PositiveAdj - 2519 adjustments, 2506.0 positive, 0.0 negative, avg adjustment size 87.3
- 2024-10-29: NegativeAdj - 2151 adjustments, 0.0 positive, 2142.0 negative, avg adjustment size 66.2
- 2024-10-28: MoveIn - 40833 adjustments, 40818.0 positive, 0.0 negative, avg adjustment size 84.7
- 2024-10-28: MoveOut - 39051 adjustments, 0.0 positive, 39036.0 negative, avg adjustment size 82.2
- 2024-10-28: PositiveAdj - 2992 adjustments, 2979.0 positive, 0.0 negative, avg adjustment size 88.6
- 2024-10-28: NegativeAdj - 2194 adjustments, 0.0 positive, 2187.0 negative, avg adjustment size 41.1
- 2024-10-27: MoveIn - 30883 adjustments, 30874.0 positive, 0.0 negative, avg adjustment size 98.7
- 2024-10-27: MoveOut - 27962 adjustments, 0.0 positive, 27953.0 negative, avg adjustment size 94.0
- 2024-10-27: PositiveAdj - 1420 adjustments, 1420.0 positive, 0.0 negative, avg adjustment size 30.1
- 2024-10-27: NegativeAdj - 1406 adjustments, 0.0 positive, 1406.0 negative, avg adjustment size 28.7
- 2024-10-26: MoveIn - 42562 adjustments, 42560.0 positive, 0.0 negative, avg adjustment size 122.7
- 2024-10-26: MoveOut - 39463 adjustments, 0.0 positive, 39461.0 negative, avg adjustment size 118.5
- 2024-10-26: PositiveAdj - 2060 adjustments, 2060.0 positive, 0.0 negative, avg adjustment size 46.4
- 2024-10-26: NegativeAdj - 1953 adjustments, 0.0 positive, 1953.0 negative, avg adjustment size 39.5
- 2024-10-25: MoveIn - 45979 adjustments, 45973.0 positive, 0.0 negative, avg adjustment size 95.9
- 2024-10-25: MoveOut - 42629 adjustments, 0.0 positive, 42623.0 negative, avg adjustment size 90.0
- 2024-10-25: PositiveAdj - 2437 adjustments, 2433.0 positive, 0.0 negative, avg adjustment size 61.3
- 2024-10-25: NegativeAdj - 2183 adjustments, 0.0 positive, 2173.0 negative, avg adjustment size 43.9
- 2024-10-24: MoveIn - 48146 adjustments, 48143.0 positive, 0.0 negative, avg adjustment size 90.9
- 2024-10-24: MoveOut - 44556 adjustments, 0.0 positive, 44553.0 negative, avg adjustment size 87.8
- 2024-10-24: PositiveAdj - 2203 adjustments, 2203.0 positive, 0.0 negative, avg adjustment size 79.9
- 2024-10-24: NegativeAdj - 1912 adjustments, 0.0 positive, 1911.0 negative, avg adjustment size 63.8
- 2024-10-23: MoveIn - 46050 adjustments, 46043.0 positive, 0.0 negative, avg adjustment size 100.3
- 2024-10-23: MoveOut - 42684 adjustments, 0.0 positive, 42677.0 negative, avg adjustment size 95.3
- 2024-10-23: PositiveAdj - 2555 adjustments, 2548.0 positive, 0.0 negative, avg adjustment size 69.7
- 2024-10-23: NegativeAdj - 2135 adjustments, 0.0 positive, 2119.0 negative, avg adjustment size 43.0
- 2024-10-22: MoveIn - 44195 adjustments, 44193.0 positive, 0.0 negative, avg adjustment size 89.9
- 2024-10-22: MoveOut - 40922 adjustments, 0.0 positive, 40920.0 negative, avg adjustment size 86.4
- 2024-10-22: PositiveAdj - 2855 adjustments, 2853.0 positive, 0.0 negative, avg adjustment size 49.6
- 2024-10-22: NegativeAdj - 2607 adjustments, 0.0 positive, 2599.0 negative, avg adjustment size 36.4
- 2024-10-21: MoveIn - 41570 adjustments, 41567.0 positive, 0.0 negative, avg adjustment size 106.0
- 2024-10-21: MoveOut - 38964 adjustments, 0.0 positive, 38961.0 negative, avg adjustment size 100.1
- 2024-10-21: PositiveAdj - 2751 adjustments, 2751.0 positive, 0.0 negative, avg adjustment size 107.6
- 2024-10-21: NegativeAdj - 2023 adjustments, 0.0 positive, 2023.0 negative, avg adjustment size 70.3
- 2024-10-20: MoveIn - 32849 adjustments, 32848.0 positive, 0.0 negative, avg adjustment size 77.1
- 2024-10-20: MoveOut - 30460 adjustments, 0.0 positive, 30459.0 negative, avg adjustment size 73.5
- 2024-10-20: PositiveAdj - 1669 adjustments, 1669.0 positive, 0.0 negative, avg adjustment size 46.9
- 2024-10-20: NegativeAdj - 1650 adjustments, 0.0 positive, 1650.0 negative, avg adjustment size 42.3
- 2024-10-19: MoveIn - 40562 adjustments, 40562.0 positive, 0.0 negative, avg adjustment size 81.1
- 2024-10-19: MoveOut - 37453 adjustments, 0.0 positive, 37453.0 negative, avg adjustment size 77.3
- 2024-10-19: PositiveAdj - 1792 adjustments, 1792.0 positive, 0.0 negative, avg adjustment size 38.1
- 2024-10-19: NegativeAdj - 1733 adjustments, 0.0 positive, 1732.0 negative, avg adjustment size 33.3
- 2024-10-18: MoveIn - 46237 adjustments, 46234.0 positive, 0.0 negative, avg adjustment size 92.7
- 2024-10-18: MoveOut - 42761 adjustments, 0.0 positive, 42758.0 negative, avg adjustment size 88.1
- 2024-10-18: PositiveAdj - 1910 adjustments, 1908.0 positive, 0.0 negative, avg adjustment size 77.0
- 2024-10-18: NegativeAdj - 1514 adjustments, 0.0 positive, 1504.0 negative, avg adjustment size 48.7
- 2024-10-17: MoveIn - 48626 adjustments, 48613.0 positive, 0.0 negative, avg adjustment size 131.4
- 2024-10-17: MoveOut - 44868 adjustments, 0.0 positive, 44855.0 negative, avg adjustment size 128.6
- 2024-10-17: PositiveAdj - 2307 adjustments, 2305.0 positive, 0.0 negative, avg adjustment size 54.2
- 2024-10-17: NegativeAdj - 2070 adjustments, 0.0 positive, 2067.0 negative, avg adjustment size 41.3
- 2024-10-16: MoveIn - 44901 adjustments, 44885.0 positive, 0.0 negative, avg adjustment size 95.6
- 2024-10-16: MoveOut - 42108 adjustments, 0.0 positive, 42092.0 negative, avg adjustment size 91.6
- 2024-10-16: PositiveAdj - 2457 adjustments, 2452.0 positive, 0.0 negative, avg adjustment size 116.7
- 2024-10-16: NegativeAdj - 1664 adjustments, 0.0 positive, 1648.0 negative, avg adjustment size 70.0
- 2024-10-15: MoveIn - 38369 adjustments, 38364.0 positive, 0.0 negative, avg adjustment size 98.1
- 2024-10-15: MoveOut - 35697 adjustments, 0.0 positive, 35692.0 negative, avg adjustment size 94.0
- 2024-10-15: PositiveAdj - 1809 adjustments, 1809.0 positive, 0.0 negative, avg adjustment size 81.8
- 2024-10-15: NegativeAdj - 1562 adjustments, 0.0 positive, 1558.0 negative, avg adjustment size 62.6
- 2024-10-14: MoveIn - 34249 adjustments, 34247.0 positive, 0.0 negative, avg adjustment size 91.4
- 2024-10-14: MoveOut - 32184 adjustments, 0.0 positive, 32182.0 negative, avg adjustment size 88.0
- 2024-10-14: PositiveAdj - 2953 adjustments, 2947.0 positive, 0.0 negative, avg adjustment size 125.4
- 2024-10-14: NegativeAdj - 1899 adjustments, 0.0 positive, 1883.0 negative, avg adjustment size 40.4
- 2024-10-13: MoveIn - 24547 adjustments, 24547.0 positive, 0.0 negative, avg adjustment size 101.6
- 2024-10-13: MoveOut - 21990 adjustments, 0.0 positive, 21990.0 negative, avg adjustment size 98.4
- 2024-10-13: PositiveAdj - 1203 adjustments, 1203.0 positive, 0.0 negative, avg adjustment size 32.5
- 2024-10-13: NegativeAdj - 1184 adjustments, 0.0 positive, 1184.0 negative, avg adjustment size 29.4
- 2024-10-12: MoveIn - 44154 adjustments, 44139.0 positive, 0.0 negative, avg adjustment size 103.1
- 2024-10-12: MoveOut - 39653 adjustments, 0.0 positive, 39638.0 negative, avg adjustment size 98.3
- 2024-10-12: PositiveAdj - 1980 adjustments, 1979.0 positive, 0.0 negative, avg adjustment size 40.7
- 2024-10-12: NegativeAdj - 1948 adjustments, 0.0 positive, 1948.0 negative, avg adjustment size 32.4
- 2024-10-11: MoveIn - 54263 adjustments, 54257.0 positive, 0.0 negative, avg adjustment size 90.5
- 2024-10-11: MoveOut - 50958 adjustments, 0.0 positive, 50952.0 negative, avg adjustment size 86.2
- 2024-10-11: PositiveAdj - 3048 adjustments, 3048.0 positive, 0.0 negative, avg adjustment size 30.7
- 2024-10-11: NegativeAdj - 2988 adjustments, 0.0 positive, 2988.0 negative, avg adjustment size 26.3
- 2024-10-10: MoveIn - 50155 adjustments, 50152.0 positive, 0.0 negative, avg adjustment size 94.9
- 2024-10-10: MoveOut - 46597 adjustments, 0.0 positive, 46594.0 negative, avg adjustment size 91.7
- 2024-10-10: PositiveAdj - 2688 adjustments, 2688.0 positive, 0.0 negative, avg adjustment size 32.6
- 2024-10-10: NegativeAdj - 2601 adjustments, 0.0 positive, 2601.0 negative, avg adjustment size 28.3
- 2024-10-09: MoveIn - 45753 adjustments, 45744.0 positive, 0.0 negative, avg adjustment size 92.6
- 2024-10-09: MoveOut - 42604 adjustments, 0.0 positive, 42595.0 negative, avg adjustment size 88.4
- 2024-10-09: PositiveAdj - 2586 adjustments, 2577.0 positive, 0.0 negative, avg adjustment size 64.1
- 2024-10-09: NegativeAdj - 2286 adjustments, 0.0 positive, 2273.0 negative, avg adjustment size 41.5
- 2024-10-08: MoveIn - 42895 adjustments, 42863.0 positive, 0.0 negative, avg adjustment size 145.8
- 2024-10-08: MoveOut - 39817 adjustments, 0.0 positive, 39785.0 negative, avg adjustment size 145.2
- 2024-10-08: PositiveAdj - 2232 adjustments, 2225.0 positive, 0.0 negative, avg adjustment size 95.9
- 2024-10-08: NegativeAdj - 2095 adjustments, 0.0 positive, 2091.0 negative, avg adjustment size 48.3
- 2024-10-07: MoveIn - 3851 adjustments, 3847.0 positive, 0.0 negative, avg adjustment size 110.1
- 2024-10-07: MoveOut - 3605 adjustments, 0.0 positive, 3601.0 negative, avg adjustment size 112.6
- 2024-10-07: PositiveAdj - 274 adjustments, 274.0 positive, 0.0 negative, avg adjustment size 24.9
- 2024-10-07: NegativeAdj - 270 adjustments, 0.0 positive, 270.0 negative, avg adjustment size 19.9

---


## 12. Picking Performance Analysis

Analyzes picking operation efficiency

Picking performance analysis:

- 2024-10-30: 415 picks, 24 unique pickers, avg pick time 152.9 minutes, 99.0% accuracy
- 2024-10-29: 6810 picks, 72 unique pickers, avg pick time 109.1 minutes, 98.8% accuracy
- 2024-10-28: 8277 picks, 83 unique pickers, avg pick time 117.6 minutes, 99.3% accuracy
- 2024-10-27: 5116 picks, 58 unique pickers, avg pick time 189.1 minutes, 99.6% accuracy
- 2024-10-26: 7658 picks, 61 unique pickers, avg pick time 170.7 minutes, 99.4% accuracy
- 2024-10-25: 7435 picks, 74 unique pickers, avg pick time 171.3 minutes, 99.3% accuracy
- 2024-10-24: 8533 picks, 81 unique pickers, avg pick time 125.2 minutes, 99.3% accuracy
- 2024-10-23: 7863 picks, 77 unique pickers, avg pick time 139.3 minutes, 99.4% accuracy
- 2024-10-22: 7429 picks, 68 unique pickers, avg pick time 138.3 minutes, 99.2% accuracy
- 2024-10-21: 7424 picks, 80 unique pickers, avg pick time 115.7 minutes, 99.4% accuracy
- 2024-10-20: 6088 picks, 62 unique pickers, avg pick time 161.3 minutes, 99.3% accuracy
- 2024-10-19: 7043 picks, 57 unique pickers, avg pick time 175.2 minutes, 99.3% accuracy
- 2024-10-18: 8339 picks, 78 unique pickers, avg pick time 154.6 minutes, 99.1% accuracy
- 2024-10-17: 7801 picks, 77 unique pickers, avg pick time 119.0 minutes, 99.3% accuracy
- 2024-10-16: 8173 picks, 84 unique pickers, avg pick time 112.3 minutes, 99.4% accuracy
- 2024-10-15: 6495 picks, 69 unique pickers, avg pick time 122.2 minutes, 99.0% accuracy
- 2024-10-14: 6113 picks, 67 unique pickers, avg pick time 182.0 minutes, 99.4% accuracy
- 2024-10-13: 4074 picks, 48 unique pickers, avg pick time 239.6 minutes, 99.4% accuracy
- 2024-10-12: 6480 picks, 64 unique pickers, avg pick time 146.3 minutes, 99.4% accuracy
- 2024-10-11: 9703 picks, 88 unique pickers, avg pick time 114.1 minutes, 99.5% accuracy
- 2024-10-10: 8752 picks, 87 unique pickers, avg pick time 111.8 minutes, 99.4% accuracy
- 2024-10-09: 7925 picks, 81 unique pickers, avg pick time 141.4 minutes, 99.4% accuracy
- 2024-10-08: 7256 picks, 71 unique pickers, avg pick time 137.1 minutes, 99.1% accuracy
- 2024-10-07: 687 picks, 36 unique pickers, avg pick time 141.4 minutes, 98.4% accuracy

---

