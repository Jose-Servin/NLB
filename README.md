# NLB

National Load Board provides a centralized online platform for shippers, brokers, and carriers in the freight sector. The platform’s primary role is to link available loads with carriers capable of transporting them. It also offers additional benefits including OCR for scanning and managing documents, live tracking of loads for real-time visibility, and financial reporting to support efficient freight management.

## Main Functionalities of a Load Board

- **Load Posting**: Shippers and brokers can post details of available loads, including pickup and delivery locations, cargo type, weight, and special requirements.
- **Load Searching**: Carriers can search for loads based on criteria like location, type of cargo, and desired route, helping them find jobs that fit their schedule and equipment.
- **Bidding and Negotiation**: Carriers can place bids on loads, and shippers or brokers can accept or negotiate these bids to reach an agreement on transportation rates.
- **Load Assignment**: Once a bid is accepted, the load is assigned to a carrier, who is then responsible for transporting the freight.
- **Tracking and Updates**: Provides real-time tracking and status updates of loads, allowing all parties to monitor the progress of shipments.
- **Payment Processing**: Facilitates secure and timely payment processing for completed shipments, often with integrated invoicing and financial reporting features.

## NLB Core Features

- **Search Loads**: Enables users to search for available loads based on various criteria such as location, weight, type of cargo, and more.

- **Dashboard**: Provides users with an overview of their activities, including active loads, upcoming shipments, and recent notifications.

- **My Loads**: Allows users to manage and track the loads they have posted or are currently handling.

- **My Shipments**: Displays all shipments associated with the user, including their current status and history.

- **My Trucks**: A management feature where users can keep track of their fleet, including truck details, availability, and maintenance schedules.

- **Documents Hub**: A centralized location for storing and accessing important documents, such as contracts, invoices, and shipment papers.

- **Tools**:
  - **OCR Doc Scanning**: Provides Optical Character Recognition (OCR) capabilities to scan and digitize documents directly within the platform.
  - **Live Load Tracking**: Enables real-time tracking of loads, providing visibility into the current location and status of shipments.
  - **Financial Reports**: Generates detailed financial reports related to loads, payments, and other transactions for better financial management.

## API Documentation

- [API Endpoints Version 1](./docs/api_endpoints_v1.md)

## Disclaimer

This project is a fictional load board created solely for the purpose of practicing and demonstrating my Full-Stack web development skills. It is not intended for real-world use in the logistics or transportation industry. The features and functionalities implemented in this project are for educational purposes only.

## Branching Strategy

For effective development and integration, we use a structured branching strategy. Here’s a quick guide:

- **`main`**: The production-ready branch that contains stable code. All final releases are merged into this branch.
  
- **`staging`**: The branch used for pre-production testing. Features that are integrated and tested in `dev` are merged into `staging` for final validation before being released to production.

- **`dev`**: The branch where active development occurs. Feature branches are merged into `dev` for integration and initial testing. Once features are stable, they are merged into `staging`.

- **`feature/[feature-name]`**: Individual branches for developing new features or fixes. These branches are created off of `dev` and are merged back into `dev` once the feature is complete and tested.

### Workflow

1. **Create Feature Branches**: Start by creating a feature branch off of `dev` for each new feature or fix. Use the naming convention `feature/[feature-name]`.

2. **Develop and Test**: Work on the feature in its own branch. Once complete, merge it back into `dev` for integration and further testing.

3. **Prepare for Production**: Once `dev` is stable, merge it into `staging` for final pre-production testing.

4. **Deploy to Production**: After successful testing in `staging`, merge `staging` into `main` for production release.
