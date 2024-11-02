import { Component, ViewChild, ElementRef } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-main-page',
  standalone: true,
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss'],
  imports: [CommonModule]
})
export class MainPageComponent {
  @ViewChild('fileInput') fileInput!: ElementRef;

  constructor(private router: Router) {}

  triggerFileInput() {
    this.fileInput.nativeElement.click();
  }

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      const file = input.files[0];
      if (file.type === 'application/pdf') {
        this.router.navigate(['/feature', { fileName: file.name }]);
      } else {
        alert('Please upload a valid PDF file.');
      }
    }
  }
}
