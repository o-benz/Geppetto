# Financial Analysis Tool using Generative AI: Geppetto

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Setup Instructions](#setup-instructions)
5. [Architecture](#architecture)
6. [Functionality](#functionality)
7. [Usage](#usage)
8. [Contributors](#contributors)
9. [License](#license)

## Project Overview
Geppetto is an innovative application designed to assist financial analysts in automating the analysis of financial reports. Leveraging generative AI and AWS services, the tool provides features for summarizing financial statements and extracting key performance indicators (KPIs).

## Features
- **Automatic Report Summarization**: Generate concise summaries of financial reports.
- **KPI Extraction**: Identify and visualize critical financial metrics.
- **User-Friendly Interface**: Intuitive design for easy navigation.
- **Data Visualization**: Present financial data through graphs and charts.
- **Integration with AWS Services**: Utilize AWS Bedrock and S3 for data processing and storage.

## Tech Stack
- **Frontend**: Angular, TypeScript, SCSS
- **Backend**: Node.js, Express.js (or AWS Lambda)
- **Database**: Amazon S3 (for data storage)
- **AI Services**: Amazon Bedrock (with Claude 3.5 for generative AI capabilities)
- **Deployment**: AWS Lambda (if applicable) or a suitable cloud service

## Getting Started

### Prerequisites
To run this project, you will need:
- Node.js and npm installed on your machine.
- Access to an AWS account with permissions to use AWS Bedrock and S3.
- Angular CLI installed globally:
  ```bash
  npm install -g @angular/cli
  ```

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/financial-analysis-tool.git
   cd financial-analysis-tool
   ```

2. **Set Up the Angular Client**:
   ```bash
   cd client
   npm install
   ng serve
   ```

3. **Set Up the Backend**:
   - If using Express.js:
     ```bash
     cd backend
     npm install
     node index.js
     ```

   - If using AWS Lambda, deploy your function through the AWS console and set up API Gateway.

4. **Configure AWS Credentials**:
   - Ensure that your AWS credentials are correctly configured in your environment to allow the application to access AWS services.

## Architecture
The application follows a modular architecture with distinct separation between the client and backend services. The Angular frontend communicates with the backend API, which in turn interacts with AWS services for data processing and storage.

![Architecture Diagram](./docs/architecture.png) <!-- Replace with actual diagram -->

## Functionality
- **Frontend**: The user interface is developed in Angular and provides forms for uploading financial reports, viewing summaries, and visualizing KPIs.
- **Backend**: The server processes requests from the Angular client, utilizes AWS Bedrock for generating report summaries, and retrieves data from S3 for analysis.

## Usage
1. Navigate to the Angular application in your browser (`http://localhost:4200`).
2. Use the provided forms to upload financial reports.
3. View the generated summaries and KPI visualizations on the dashboard.

## Contributors
- **Omar Benzekri** - [GitHub Profile](https://github.com/o-benz)
- **[Other Contributors]** - [Other Contributor GitHub Profiles]

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.