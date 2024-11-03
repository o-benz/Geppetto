import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { S3Service } from '@app/services/s3/s3.service';
import { BedrockService } from '@app/services/bedrock/bedrock.service';
import { FileService } from '@app/services/file/file.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-feature',
  templateUrl: './feature.component.html',
  styleUrls: ['./feature.component.scss'],
  standalone: true,
  imports: [CommonModule]
})
export class FeatureComponent implements OnInit {
  file: File | null = null;
  @ViewChild('fileInput') fileInput!: ElementRef;

  constructor(
    private fileService: FileService,
    private s3Service: S3Service,
    private bedrockService: BedrockService,
    private http: HttpClient
  ) {}

  ngOnInit() {
    this.file = this.fileService.getFile();
  }

  changeFile() {
    this.fileInput.nativeElement.click();
  }

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      const file = input.files[0];
      console.log('File selected:', file.name);
      this.fileService.setFile(file);
      this.file = file;
    }
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

  sendPrompt(prompt: string) {
    this.http.post<{ result: string }>('/api/run-model', { prompt }).subscribe(
      response => {
        console.log('Model response:', response.result);
      },
      err => console.error('Error from model:', err)
    );
  }

  generateSummary() {
    this.uploadAndPrompt('Generate a summary based on the file contents.');
  }

  analyzeData() {
    this.uploadAndPrompt('Analyze the data and provide insights.');
  }
}
