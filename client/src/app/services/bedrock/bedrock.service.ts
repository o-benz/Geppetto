// aws-bedrock.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BedrockService {
  private apiUrl = 'https://bedrock-api-url'; // replace with your Bedrock API endpoint

  constructor(private http: HttpClient) {}

  sendPrompt(prompt: string): Observable<any> {
    return this.http.post(this.apiUrl, { prompt });
  }
}
