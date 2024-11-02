import { Component, OnInit } from '@angular/core';
import { S3Service } from '@app/services/s3/s3.service';
import { BedrockService } from '@app/services/bedrock/bedrock.service';
import { FileService } from '@app/services/file/file.service';

@Component({
  selector: 'app-feature',
  templateUrl: './feature.component.html',
  styleUrls: ['./feature.component.scss']
})
export class FeatureComponent implements OnInit {
  file: File | null = null;

  constructor(private fileService: FileService, private s3Service: S3Service, private bedrockService: BedrockService) {}

  ngOnInit() {
    this.file = this.fileService.getFile();
  }

  private uploadAndPrompt(prompt: string) {
    if (this.file) {
      this.s3Service.uploadFile(this.file).subscribe(
        () => {
          console.log('File uploaded successfully:', this.file?.name);
          this.bedrockService.sendPrompt(prompt).subscribe(
            response => console.log('Bedrock response:', response),
            err => console.error('Error from Bedrock:', err)
          );
        },
        err => console.error('Error uploading file:', err)
      );
    } else {
      console.warn('No file selected');
    }
  }

  generateSummary() {
    this.uploadAndPrompt('Generate a summary based on the file contents.');
  }

  extractKPI() {
    this.uploadAndPrompt('Extract key performance indicators from the file contents.');
  }

  analyzeData() {
    this.uploadAndPrompt('Analyze the data and provide insights.');
  }
}
