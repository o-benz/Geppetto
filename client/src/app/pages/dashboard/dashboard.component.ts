import { Component, OnInit, AfterViewInit } from '@angular/core';
import { Chart, registerables } from 'chart.js';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit, AfterViewInit {
  fileContent: any;
  explanations: any;

  constructor() {
    Chart.register(...registerables);
  }

  ngOnInit() {
    this.fileContent = {
      dates: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      stockPrices: [65, 59, 80, 81, 56, 55, 40],
      revenue: [28, 48, 40, 19, 86, 27, 90],
      expenseCategories: ['Rent', 'Utilities', 'Salaries', 'Marketing', 'Miscellaneous'],
      expenses: [3000, 1500, 2000, 1000, 500],
      investmentCategories: ['Stocks', 'Bonds', 'Real Estate', 'Commodities', 'Cryptocurrency'],
      investments: [5000, 3000, 4000, 2000, 1000],
      performanceMetrics: ['Return on Investment', 'Net Profit Margin', 'Gross Profit Margin', 'Operating Expense Ratio', 'Current Ratio'],
      performance: [20, 30, 40, 50, 60]
    };

    this.explanations = {
      chart1: 'This line chart shows stock price movements over the first half of the fiscal year. The data highlights a generally upward trend with significant volatility, peaking in March at $245 per share due to a successful product launch. However, there was a dip in April, likely due to market correction and external economic factors. The end-of-June price at $225 indicates investor confidence despite slight fluctuations.',
      chart2: 'This bar chart represents monthly revenue, showing robust growth from January through June. Notably, May saw a 40% jump in revenue, reaching $10 million, attributed to a seasonal uptick in sales and a new subscription model. While June’s revenue stabilized, the consistent growth reflects expanding market reach and effective monetization strategies.',
      chart3: 'This pie chart details the expenditure breakdown for the first half of the year. Rent and Utilities form the largest portion, representing 35% of overall expenses, while R&D and Marketing closely follow. Increased R&D spending indicates a strong focus on product innovation, underscoring a commitment to long-term growth through investment in technology advancements.',
      chart4: 'This doughnut chart illustrates the investment portfolio distribution. Over 50% of the investments are allocated to stocks and real estate, reflecting a balanced approach between growth and stability. Emerging technologies make up a smaller but strategic 15%, aligning with a goal to stay at the forefront of industry trends while mitigating risk through diversified asset classes.',
      chart5: 'This radar chart evaluates key performance metrics: Customer Satisfaction, Market Penetration, Innovation, Cost Efficiency, and Employee Engagement. Each metric is scored on a 1 to 100 scale. Notably, Customer Satisfaction scores an impressive 90, reflecting high product appeal. Cost Efficiency lags slightly at 65, suggesting potential areas for improvement in operational costs to enhance profitability.'
    };
  }

  ngAfterViewInit() {
    this.renderCharts();
  }

  renderCharts() {
    const ctx1 = (document.getElementById('chart1') as HTMLCanvasElement)?.getContext('2d');
    if (ctx1) {
      new Chart(ctx1, {
        type: 'line',
        data: {
          labels: this.fileContent.dates,
          datasets: [{
            label: 'Stock Prices',
            data: this.fileContent.stockPrices,
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }]
        }
      });
    } else {
      console.error('Failed to get context for chart1');
    }

    const ctx2 = (document.getElementById('chart2') as HTMLCanvasElement)?.getContext('2d');
    if (ctx2) {
      new Chart(ctx2, {
        type: 'bar',
        data: {
          labels: this.fileContent.dates,
          datasets: [{
            label: 'Revenue',
            data: this.fileContent.revenue,
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1
          }]
        }
      });
    } else {
      console.error('Failed to get context for chart2');
    }

    const ctx3 = (document.getElementById('chart3') as HTMLCanvasElement)?.getContext('2d');
    if (ctx3) {
      new Chart(ctx3, {
        type: 'pie',
        data: {
          labels: this.fileContent.expenseCategories,
          datasets: [{
            label: 'Expenses',
            data: this.fileContent.expenses,
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)'
            ],
            borderWidth: 1
          }]
        }
      });
    } else {
      console.error('Failed to get context for chart3');
    }

    const ctx4 = (document.getElementById('chart4') as HTMLCanvasElement)?.getContext('2d');
    if (ctx4) {
      new Chart(ctx4, {
        type: 'doughnut',
        data: {
          labels: this.fileContent.investmentCategories,
          datasets: [{
            label: 'Investments',
            data: this.fileContent.investments,
            backgroundColor: [
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
              'rgba(255, 159, 64, 1)',
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
          }]
        }
      });
    } else {
      console.error('Failed to get context for chart4');
    }

    const ctx5 = (document.getElementById('chart5') as HTMLCanvasElement)?.getContext('2d');
    if (ctx5) {
      new Chart(ctx5, {
        type: 'radar',
        data: {
          labels: this.fileContent.performanceMetrics,
          datasets: [{
            label: 'Performance',
            data: this.fileContent.performance,
            backgroundColor: 'rgba(255, 206, 86, 0.2)',
            borderColor: 'rgba(255, 206, 86, 1)',
            borderWidth: 1
          }]
        }
      });
    } else {
      console.error('Failed to get context for chart5');
    }
  }

  exportToPDF() {
    const section = document.querySelector('.section') as HTMLElement;
    if (section) {
      html2canvas(section).then(canvas => {
        const imgData = canvas.toDataURL('image/png');
        const doc = new jsPDF('p', 'mm', 'a4');
        const imgProps = doc.getImageProperties(imgData);
        const pdfWidth = doc.internal.pageSize.getWidth();
        const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
  
        doc.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
        doc.save('dashboard.pdf');
      }).catch(error => {
        console.error('Failed to capture section as image', error);
      });
    } else {
      console.error('Failed to find section with class "section"');
    }
  }

  exportToPNG(visual: string) {
    const canvas = document.getElementById(visual) as HTMLCanvasElement;
    if (canvas) {
      const link = document.createElement('a');
      link.href = canvas.toDataURL('image/png');
      link.download = `${visual}.png`;
      link.click();
    } else {
      console.error(`Failed to find canvas with id ${visual}`);
    }
  }

  exportToCSV() {
    const data = [
      ['Date', 'Stock Prices', 'Revenue', 'Expenses', 'Investments', 'Performance'],
      ...this.fileContent.dates.map((date: any, index: string | number) => [
        date,
        this.fileContent.stockPrices[index],
        this.fileContent.revenue[index],
        this.fileContent.expenses[index],
        this.fileContent.investments[index],
        this.fileContent.performance[index]
      ])
    ];
  
    const csvContent = data.map(e => e.join(",")).join("\n");
  
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", "dashboard_data.csv");
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
}