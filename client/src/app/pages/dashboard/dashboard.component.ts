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
      chart1: 'This chart shows the stock prices over the first half of the year. The data indicates a fluctuating trend with a peak in March.',
      chart2: 'This bar chart represents the revenue generated each month. Notice the significant increase in revenue during May.',
      chart3: 'This pie chart breaks down the expenses into various categories. Rent and Utilities constitute the major portions of the expenses.',
      chart4: 'This doughnut chart illustrates the distribution of investments across different categories. Stocks and Real Estate are the primary investment areas.',
      chart5: 'This radar chart displays the performance metrics. Each metric is evaluated on a scale of 1 to 100, with Metric5 showing the highest performance.'
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