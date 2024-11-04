import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { S3Service } from '@app/services/s3/s3.service';
import { FileService } from '@app/services/file/file.service';
import { HttpClient } from '@angular/common/http';
import { Feature } from '@app/enums/Feature';
import { Router } from '@angular/router';
import { ResponseService } from '@app/services/response/response.service';

@Component({
  selector: 'app-feature',
  templateUrl: './feature.component.html',
  styleUrls: ['./feature.component.scss'],
  standalone: true,
  imports: [CommonModule]
})
export class FeatureComponent implements OnInit {
  loading: boolean = false;
  private companies: { [key: string]: { name: string, logo: string, description: string } } = {
    CN: { name: "Canadian National Railway", logo: "../../assets/CN.png", description: "The Canadian National Railway Company is a Canadian Class I freight railway headquartered in Montreal, Quebec, which serves Canada and the Midwestern and Southern United States." },
    CPKC: { name: "Canadian Pacific Kansas City", logo: "../../assets/CPKC.png", description: "Canadian Pacific Kansas City Limited, doing business as CPKC, is a Canadian railway holding company." },
    Cogeco: { name: "Cogeco", logo: "../../assets/Cogeco.png", description: "Cogeco Inc. is a Canadian telecommunications and media company. Its corporate offices are located at 1 Place Ville-Marie in Montreal, Quebec. The company is structured into three strategic business units; Cogeco Connexion, Breezeline, and Cogeco Media." },
    Bell: { name: "Bell Canada", logo: "../../assets/Bell.png", description: "Bell Canada is a Canadian telecommunications company headquartered at 1 Carrefour Alexander-Graham-Bell in the borough of Verdun, Quebec, in Canada. It is an ILEC in the provinces of Ontario and Quebec; as such, it was a founding member of the Stentor Alliance." },
    Telus: { name: "Telus", logo: "../../assets/Telus.png", description: "Telus Corporation (also shortened and referred to as Telus Corp.) is a Canadian publicly traded holding company and conglomerate, headquartered in Vancouver, British Columbia, which is the parent company of several subsidiaries: Telus Communications Inc. offers telephony, television, data and Internet services." },
    Rogers: { name: "Rogers Communications", logo: "../../assets/Rogers.png", description: "Rogers Communications Inc. is a Canadian communications and media company operating primarily in the fields of wireless communications, cable television, telephony and Internet, with significant additional telecommunications and mass media assets. Rogers has its headquarters in Toronto, Ontario." },
    Quebecor: { name: "Quebecor", logo: "../../assets/Quebecor.png", description: "Quebecor Inc. is a Canadian diversified media and telecommunications company serving Québec based in Montreal. It was spelled Quebecor in both English and French until May 2012, when shareholders voted to add the acute accent, Québecor, in French only" },
    HydroOne: { name: "Hydro One", logo: "../../assets/HydroOne.png", description: "Hydro One Limited is an electricity transmission and distribution utility serving the Canadian province of Ontario. Hydro One traces its history to the early 20th century and the establishment of the Hydro-Electric Power Commission of Ontario (renamed Ontario Hydro in 1974). In October 1998, the provincial legislature passed the Energy Competition Act which restructured Ontario Hydro into separate entities responsible for electrical generation, transmission/delivery, and price management with a final goal of total privatization." },
    Fortis: { name: "Fortis", logo: "../../assets/Fortis.png", description: "Fortis Inc. is a St. John's, Newfoundland and Labrador-based international diversified electric utility holding company. It operates in Canada, the United States, Central America, and the Caribbean. In 2015, it earned CA$6.7 billion." },
    AltaGas: { name: "AltaGas", logo: "../../assets/AltaGas.png", description: "AltaGas is a North American energy infrastructure company based in Calgary, Alberta. It links natural gas liquids and natural gas to both Canadian and global markets. The company operates in four business segments: utilities, midstream, power and corporate." }
  };

  file: File | null = null;
  @ViewChild('fileInput') fileInput!: ElementRef;

  public company: string = '';
  public year: string = '';
  public companyInfo: { name: string, logo: string, description: string } | null = null;

  constructor(
    private fileService: FileService,
    private s3Service: S3Service,
    private http: HttpClient,
    private router: Router,
    private responseService: ResponseService
  ) {}

  private parseFileName(fileName: string): { company: string, year: string} {
    const parts = fileName.split('_');
    if (parts.length !== 2) {
      throw new Error('Invalid file name format. Expected format: company_year.pdf');
    }
    const [company, yearWithExtension] = parts;
    const year = yearWithExtension.replace('.pdf', '');
    return { company, year };
  }

  private uploadAndPrompt(feature: Feature, company: string, year: string) {
    if (this.file) {
      this.loading = true;
      this.s3Service.uploadFile(this.file).subscribe(
        () => {
          console.log('File uploaded successfully:', this.file?.name);
          let file: string = '';
          if (this.file?.name) {
            file = this.file?.name;
          }
          this.http.post<{ result: string }>('/api/run-model', { feature, company, year, file }).subscribe(
            response => {
              console.log('Model response:', response.result);
              this.responseService.setResponseData(response.result);
              const fileName = this.file?.name || '';
              if (feature === Feature.Summarization) {
                this.router.navigate(['/summary', fileName]);
              } else if (feature === Feature.SentimentAnalysis) {
                this.router.navigate(['/sentiment', fileName]);
              }
            },
            err => console.error('Error from model:', err)
          );
        },
        err => console.error('Error uploading file:', err)
      );
    } else {
      console.warn('No file selected');
    }
  }

  ngOnInit() {
    this.file = this.fileService.getFile();
    if (this.file) {
      try {
        const { company, year } = this.parseFileName(this.file.name);
        this.company = company;
        this.year = year;
        this.companyInfo = this.companies[company] || null;
        console.log(company, year);
      } catch (error) {
        if (error instanceof Error) {
          console.error(error.message);
        } else {
          console.error('An unknown error occurred');
        }
      }
    }
  }

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      const file = input.files[0];
      console.log('File selected:', file.name);
      this.fileService.setFile(file);
      this.file = file;
  
      const { company, year } = this.parseFileName(file.name);
      this.company = company;
      this.year = year;
      this.companyInfo = this.companies[company] || null;
    }
  }

  changeFile() {
    this.fileInput.nativeElement.click();
  }

  generateSummary() {
    this.uploadAndPrompt(Feature.Summarization, this.company, this.year);
  }

  analyzeSentiment() {
    this.uploadAndPrompt(Feature.SentimentAnalysis, this.company, this.year);
  }

  analyzeData() {
    this.uploadAndPrompt(Feature.DataGeneration, this.company, this.year);
  }
}