import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-main-page',
  standalone: true,
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss'],
  imports: [CommonModule]
})
export class MainPageComponent {
  fileUploaded: boolean = false;
  features = [
    {
      title: 'Automated Financial Summarization',
      description: 'Generate concise summaries from complex financial reports quickly and efficiently.',
      buttonText: 'Generate Summary',
      action: () => this.generateSummary()
    },
    {
      title: 'KPI Extraction',
      description: 'Extract and visualize essential KPIs to monitor performance effectively.',
      buttonText: 'Extract KPI',
      action: () => this.extractKPI()
    },
    {
      title: 'Data Analysis',
      description: 'Utilize advanced analytics tools to uncover trends and insights from your financial data.',
      buttonText: 'Analyze Data',
      action: () => this.analyzeData()
    },
  ];

  startAnalysis() {
    this.fileUploaded = true;
  }

  onFileSelected(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      // Handle the uploaded file, e.g., parsing it or uploading it to a server
      console.log('File selected:', file.name);
      // Perform actions based on the uploaded file
    }
  }

  generateSummary() {
    // Logic for generating summary
    console.log('Generating summary...');
  }

  extractKPI() {
    // Logic for extracting KPI
    console.log('Extracting KPI...');
  }

  analyzeData() {
    // Logic for analyzing data
    console.log('Analyzing data...');
  }
}
