import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ResponseService {
  private responseData: string | null = null;

  setResponseData(data: string) {
    this.responseData = data;
  }

  getResponseData(): string | null {
    return this.responseData;
  }
}