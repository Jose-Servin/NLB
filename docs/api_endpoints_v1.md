# API Endpoints - Version 1

## **Authentication:**

- **POST `/api/register/`**
  - **Role**: Public (Unauthenticated users)
  - **Description**: Allows new users to register.
  
- **POST `/api/login/`**
  - **Role**: Public (Unauthenticated users)
  - **Description**: Allows users to log in.
  
- **POST `/api/logout/`**
  - **Role**: Authenticated Users
  - **Description**: Allows logged-in users to log out.
  
- **GET `/api/user/`**
  - **Role**: Authenticated Users
  - **Description**: Retrieves details of the currently logged-in user.

## **Loads:**

- **GET `/api/loads/`**
  - **Role**: Authenticated Users
  - **Description**: Retrieves a list of available loads.
  
- **POST `/api/loads/`**
  - **Role**: Shippers, Brokers
  - **Description**: Allows Shippers and Brokers to create a new load.
  
- **GET `/api/loads/{id}/`**
  - **Role**: Authenticated Users
  - **Description**: Retrieves details of a specific load.
  
- **PUT `/api/loads/{id}/`**
  - **Role**: Shippers, Brokers (Owner of the load)
  - **Description**: Allows the owner (Shipper/Broker) to update a specific load.
  
- **DELETE `/api/loads/{id}/`**
  - **Role**: Shippers, Brokers (Owner of the load)
  - **Description**: Allows the owner (Shipper/Broker) to delete a specific load.

## **Bidding:**

- **POST `/api/loads/{id}/bids/`**
  - **Role**: Carriers
  - **Description**: Allows Carriers to submit a bid on a load.
  
- **GET `/api/loads/{id}/bids/`**
  - **Role**: Shippers, Brokers (Owner of the load)
  - **Description**: Allows the owner (Shipper/Broker) to retrieve all bids on a specific load.
  
- **PUT `/api/loads/{id}/bids/{bid_id}/`**
  - **Role**: Shippers, Brokers (Owner of the load)
  - **Description**: Allows the owner (Shipper/Broker) to accept or reject a bid.

## **Assignment:**

- **POST `/api/loads/{id}/assign/`**
  - **Role**: Shippers, Brokers (Owner of the load)
  - **Description**: Allows the owner (Shipper/Broker) to assign a load to a Carrier.
  
- **GET `/api/loads/{id}/status/`**
  - **Role**: Shippers, Brokers, Carriers (Involved with the load)
  - **Description**: Allows the assigned Shipper, Broker, or Carrier to retrieve the current status of a load.

## **Search:**

- **GET `/api/search/loads/`**
  - **Role**: Authenticated Users
  - **Description**: Allows users to search for loads based on various criteria.

## **Dashboard:**

- **GET `/api/dashboard/`**
  - **Role**: Authenticated Users
  - **Description**: Retrieves summary information like active loads, shipments, and financials for the logged-in user.

## **My Loads:**

- **GET `/api/my-loads/`**
  - **Role**: Shippers, Brokers, Carriers
  - **Description**: Allows users to retrieve a list of loads posted or accepted by them.

## **My Shipments:**

- **GET `/api/my-shipments/`**
  - **Role**: Shippers, Brokers, Carriers
  - **Description**: Allows users to retrieve details of current and past shipments.

## **My Trucks:**

- **GET `/api/my-trucks/`**
  - **Role**: Carriers
  - **Description**: Allows Carriers to retrieve information about their trucks and their availability.

## **Documents Hub:**

- **GET `/api/documents/`**
  - **Role**: Authenticated Users
  - **Description**: Allows users to retrieve a list of all documents related to loads, shipments, and trucks.
  
- **POST `/api/documents/`**
  - **Role**: Shippers, Brokers, Carriers (Involved with the load)
  - **Description**: Allows users to upload a new document related to a load, shipment, or truck.

## **Tools:**

- **POST `/api/tools/ocr-scan/`**
  - **Role**: Shippers, Brokers, Carriers
  - **Description**: Allows users to upload and scan a document using OCR (Optical Character Recognition).
  
- **GET `/api/tools/live-tracking/`**
  - **Role**: Shippers, Brokers, Carriers (Involved with the load)
  - **Description**: Allows users to retrieve real-time tracking information for active loads.
  
- **GET `/api/tools/financial-reports/`**
  - **Role**: Shippers, Brokers, Carriers
  - **Description**: Allows users to retrieve financial reports, such as earnings and expenses.

## **Notifications:**

- **GET `/api/notifications/`**
  - **Role**: Authenticated Users
  - **Description**: Allows users to retrieve a list of their notifications.
  
- **POST `/api/notifications/`**
  - **Role**: System/Internal Use
  - **Description**: Allows the system to send notifications (not typically used by end-users).

## **Payments (Optional):**

- **POST `/api/payments/`**
  - **Role**: Shippers, Brokers
  - **Description**: Allows payment processing for completed loads.
  
- **GET `/api/payments/`**
  - **Role**: Shippers, Brokers, Carriers
  - **Description**: Allows users to retrieve their payment history.
