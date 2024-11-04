import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ResponseService } from '@app/services/response/response.service';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.scss'],
  standalone: true,
  imports: [CommonModule]
})
export class SummaryComponent implements OnInit {
  summary: string | null = null;
  sentiment: string | null = null;

  constructor(private responseService: ResponseService) {}

  ngOnInit() {
    this.sentiment = this.responseService.getSentiment();
    this.summary = this.responseService.getSummary();
  }
}