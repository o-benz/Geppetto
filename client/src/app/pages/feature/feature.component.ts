import { Component, OnInit } from '@angular/core';
import { FileService } from '@app/services/file/file.service';

@Component({
  selector: 'app-feature',
  standalone: true,
  imports: [],
  templateUrl: './feature.component.html',
  styleUrls: ['./feature.component.scss']
})
export class FeatureComponent implements OnInit {
  file: File | null = null;

  constructor(private fileService: FileService) {}

  ngOnInit() {
    this.file = this.fileService.getFile();
    if (this.file) {
      console.log('File retrieved from service:', this.file.name);
    } else {
      console.log('No file found in service');
    }
  }
  
}