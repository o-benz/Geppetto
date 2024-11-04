import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ResponseService } from '@app/services/response/response.service';
import { HttpClient } from '@angular/common/http';
import { Feature } from '@app/enums/Feature';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.scss'],
  standalone: true,
  imports: [CommonModule]
})
export class SummaryComponent implements OnInit {
  @ViewChild('logTerminal') logTerminal!: ElementRef;
  summary: string | null = null;
  sentiment: string | null = null;
  messages: string[] = [];
  chatEnabled: boolean = true;

  constructor(
    private responseService: ResponseService,
    private http: HttpClient
  ) {}

  ngOnInit() {
    this.sentiment = this.responseService.getSentiment();
    this.summary = this.responseService.getSummary();
  }

  sendMessage(prompt: string) {
    if (prompt.trim()) {
      this.messages.push(prompt);
      this.logTerminal.nativeElement.scrollTop = this.logTerminal.nativeElement.scrollHeight;
      this.chatEnabled = false;
  
      this.http.post<{ result: string }>('/api/run-model', { feature: Feature.Chat, prompt })
        .subscribe(
          (response) => {
            console.log('Chat response:', response.result);
            this.messages.push(response.result);
            this.chatEnabled = true;
            this.logTerminal.nativeElement.scrollTop = this.logTerminal.nativeElement.scrollHeight;
          },
          (err) => {
            console.error('Error from model:', err);
            this.messages.push('Error from model');
            this.chatEnabled = true;
            this.logTerminal.nativeElement.scrollTop = this.logTerminal.nativeElement.scrollHeight;
          }
        );
    }
  }
}