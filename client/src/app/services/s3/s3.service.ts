import { Injectable } from '@angular/core';
import { S3Client, PutObjectCommand, GetObjectCommand } from '@aws-sdk/client-s3';
import { from, Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class S3Service {
  private s3Client: S3Client;
  private bucketName = 'datalakefinancier';

  constructor() {
    this.s3Client = new S3Client({
      region: environment.aws.region,
      credentials: {
        accessKeyId: environment.aws.accessKeyId,
        secretAccessKey: environment.aws.secretAccessKey
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

  getFile(key: string): Observable<any> {
    const params = {
      Bucket: this.bucketName,
      Key: key
    };
    const command = new GetObjectCommand(params);
    return from(this.s3Client.send(command).then(data => data.Body));
  }
}
