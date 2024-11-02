import { Injectable } from '@angular/core';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import { from, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class S3Service {
  private s3Client: S3Client;
  private bucketName = 'your-bucket-name'; // replace with your actual bucket name

  constructor() {
    this.s3Client = new S3Client({
      region: 'your-region', // replace with your region
      credentials: {
        accessKeyId: 'your-access-key-id', // replace with your access key
        secretAccessKey: 'your-secret-access-key' // replace with your secret access key
      }
    });
  }

  uploadFile(file: File): Observable<any> {
    const params = {
      Bucket: this.bucketName,
      Key: file.name,
      Body: file,
      ContentType: file.type
    };
    const command = new PutObjectCommand(params);
    return from(this.s3Client.send(command));
  }
}
