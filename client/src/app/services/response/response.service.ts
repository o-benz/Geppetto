import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ResponseService {
  private summary: string | null = null;
  private sentiment: string | null = null;

  setSummary(data: string) {
    this.summary = data;
  }

  getSummary(): string | null {
    return this.summary;
  }

  setSentiment(data: string) {
    this.sentiment = data;
  }

  getSentiment(): string | null {
    return this.sentiment;
  }
}