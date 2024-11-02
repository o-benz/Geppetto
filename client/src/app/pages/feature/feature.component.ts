import { Component, OnInit } from '@angular/core';
// import { FileService } from '@app/services/file/file.service';
// import { AwsBedrockService } from '@app/services/aws-bedrock/aws-bedrock.service';

@Component({
  selector: 'app-feature',
  standalone: true,
  imports: [],
  templateUrl: './feature.component.html',
  styleUrls: ['./feature.component.scss']
})
export class FeatureComponent implements OnInit {
  file: File | null = null;

  // constructor(private fileService: FileService, private awsBedrockService: AwsBedrockService) {}

  ngOnInit() {
    // this.file = this.fileService.getFile();
    // if (this.file) {
    //   console.log('File retrieved from service:', this.file.name);
    // } else {
    //   console.log('No file found in service');
    // }
  }

  generateSummary() {
    // if (this.file) {
    //   this.awsBedrockService.generateSummary(this.file).subscribe(
    //     response => {
    //       console.log('Summary:', response);
    //     },
    //     err => {
    //       console.error('Error generating summary:', err);
    //     }
    //   );
    // }
  }

  extractKPI() {
    // if (this.file) {
    //   this.awsBedrockService.extractKPI(this.file).subscribe(
    //     response => {
    //       console.log('KPI:', response);
    //     },
    //     err => {
    //       console.error('Error extracting KPI:', err);
    //     }
    //   );
    // }
  }

  analyzeData() {
    // if (this.file) {
    //   this.awsBedrockService.analyzeData(this.file).subscribe(
    //     response => {
    //       console.log('Analysis:', response);
    //     },
    //     err => {
    //       console.error('Error analyzing data:', err);
    //     }
    //   );
    // }
  }
}