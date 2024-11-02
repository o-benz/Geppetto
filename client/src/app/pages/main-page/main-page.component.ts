import { Component, ElementRef, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { FileService } from '@app/services/file/file.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss']
})
export class MainPageComponent {
  @ViewChild('fileInput') fileInput!: ElementRef;

  constructor(private router: Router, private fileService: FileService) {}

  triggerFileInput() {
    this.fileInput.nativeElement.click();
  }

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      const file = input.files[0];
      console.log('File selected:', file.name);
      this.fileService.setFile(file);
      this.router.navigate(['/feature', file.name]);
    }
  }
}