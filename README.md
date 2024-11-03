# Geppetto: AI Financial Analysis Dashboard

![Polyfinance's Datathon](/doc/assets/header.png)

## Table of Contents
1. [Project Overview](#project-overview)
2. [Polyfinance's 2024 Datathon](#polyfinances-2024-datathon)
3. [Features](#features)
   - [Automatic Report Summarization](#automatic-report-summarization)
   - [Sentiment Analysis](#sentiment-analysis)
   - [Financial Indicator Monitoring](#financial-indicator-monitoring)
   - [Financial Trend Predictions](#financial-trend-predictions)
   - [KPI Extraction and Visualization](#kpi-extraction-and-visualization)
   - [Multi-Report Comparisons](#multi-report-comparisons)
4. [User Interface](#user-interface)
5. [Tech Stack](#tech-stack)
6. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Setup Instructions](#setup-instructions)
7. [Architecture](#architecture)
8. [Functionality](#functionality)
9. [Usage](#usage)
10. [Contributors](#contributors)
11. [License](#license)

## Project Overview
Geppetto is an advanced AI-driven application designed to empower financial analysts by automating key tasks, making the analysis of financial reports faster and more insightful. Developed as part of the 2024 Polyfinance Datathon, Geppetto leverages generative AI and the AWS ecosystem to provide cutting-edge tools like automatic summarization, sentiment analysis, and real-time financial monitoring. This tool offers seamless integration with AWS services, enabling analysts to extract KPIs, visualize data, and perform comprehensive trend predictions with just a few clicks.

## Polyfinance's 2024 Datathon
The Polyfinance 2024 Datathon is a high-impact 48-hour challenge, sponsored by National Bank of Canada, focusing on innovation in financial analytics. Participants were tasked with developing a generative AI-powered tool to assist financial analysts in synthesizing and interpreting data more efficiently. Armed with AWS resources like Bedrock, Cloud9, and a wealth of financial data, the Geppetto team created a robust solution to provide real-time insights, facilitate informed decision-making, and increase the accessibility of complex financial analyses.

## Features
### Automatic Report Summarization
Our solution uses generative AI to generate concise, accurate summaries of extensive financial reports. By analyzing annual reports and key company documents, Geppetto provides analysts with a time-saving overview of essential information, enabling them to focus on strategic insights without combing through extensive data.

### Sentiment Analysis
Geppetto includes sentiment analysis for textual sections like letters to shareholders and executive comments. This feature detects the tone of these segments—optimistic, pessimistic, or neutral—offering analysts a quick overview of company sentiment across periods or documents.

### Financial Indicator Monitoring
With built-in financial indicator tracking, Geppetto detects significant variations in revenue, expenses, and other key metrics over time. Our solution enables analysts to monitor trends and uncover unexpected deviations, facilitating a proactive approach to financial oversight.

### Financial Trend Predictions
Geppetto employs historical data to forecast future trends, providing analysts with predictions for revenue, costs, and profitability. This predictive analysis helps stakeholders anticipate potential market shifts and strategize accordingly.

### KPI Extraction and Visualization
By extracting KPIs, Geppetto delivers meaningful data visualizations to help analysts interpret core metrics efficiently. Using clear graphs and dashboards, Geppetto enhances the interpretability of critical financial indicators.

### Multi-Report Comparisons
Geppetto’s comparison tool allows analysts to view differences across multiple financial reports or time periods. This feature streamlines comparative analysis, highlighting shifts in performance metrics that may indicate growth opportunities or risks.

## User Interface
Geppetto’s interface was built with the end user in mind, ensuring that even complex analytical tools are accessible and intuitive. With a streamlined layout, users can navigate seamlessly through different functionalities such as report upload, KPI dashboard, and sentiment analysis. Each component was designed to minimize clicks and maximize information accessibility, making Geppetto an ideal tool for both seasoned analysts and newcomers.

## Tech Stack
- **Frontend**: Angular, TypeScript, SCSS
- **Database**: Amazon S3 (for data storage)
- **AI Services**: Amazon Bedrock (utilizing Claude 3.5 for generative AI)
- **Deployment**: AWS Lambda and/or similar AWS services for cloud scalability and efficiency

## Getting Started

### Prerequisites
To run this project, you will need:
- Node.js and npm installed on your machine.
- Access to an AWS account with permissions for AWS Bedrock, S3, and other relevant services.
- Angular CLI installed globally:
  ```bash
  npm install -g @angular/cli
  ```

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/o-benz/geppetto.git
   cd geppetto
   ```

2. **Set Up the Angular Client**:
   ```bash
   cd client
   npm install
   ng serve
   ```

3. **Configure AWS Credentials**:
   Ensure your AWS credentials are correctly configured in the `environment.prod.ts` file, allowing the application to interact with AWS services securely.

## Architecture
Geppetto follows a modular, scalable architecture that optimally separates concerns. The Angular frontend interacts with backend AWS services via a structured API layer. Data is stored in Amazon S3, while generative AI processing is handled by Amazon Bedrock, which provides high-performance natural language processing to interpret, summarize, and predict data. The architecture leverages AWS Lambda for serverless deployment, ensuring minimal latency and optimal scalability.

![Architecture Diagram](./docs/architecture.png) <!-- Replace with actual diagram -->

## Functionality
Geppetto’s interface provides:
- **Upload Capabilities** for users to input financial reports.
- **Automated Summarization** and **Sentiment Analysis** for fast, AI-driven insights.
- **Dashboard Displays** for KPI visualizations, with clear graphical representations.
- **Trend and Forecasting Tools** to analyze past performance and predict future results.

## Usage
1. Access the Angular application in your browser at `http://localhost:4200`.
2. Upload financial documents through the report upload form.
3. Use the KPI dashboard to view generated summaries, sentiment insights, and visualized data.

## Contributors
- **Omar Benzekri** - [o-benz](https://github.com/o-benz)
- **Tinihane Boudiab** - [tinhinaneboudiab](https://github.com/tinhinaneboudiab)
- **Younes Allouchi** - [youyoulebgdemeknes](https://github.com/youyoulebgdemeknes)
- **Souhil Zaida** - [The-Lite](https://github.com/The-Lite)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.