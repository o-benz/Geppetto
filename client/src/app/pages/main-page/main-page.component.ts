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

  startAnalysis() {
    this.fileUploaded = true;
  }
}
