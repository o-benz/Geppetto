import { Injectable } from '@angular/core';
import Anthropic from '@anthropic-ai/sdk';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AnthropicService {
  private anthropic: Anthropic;

  constructor() {
    this.anthropic = new Anthropic({
      apiKey: environment.aws.accessKeyId,
      dangerouslyAllowBrowser: true
    });
  }

  async sendPrompt(content: string): Promise<void> {
    try {
      const msg = await this.anthropic.messages.create({
        model: "claude-3-5-sonnet-20241022",
        max_tokens: 1024,
        messages: [{ role: "user", content }],
      });
      console.log(msg);
    } catch (error) {
      console.error('Error sending prompt:', error);
    }
  }
}