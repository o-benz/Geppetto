import { provideHttpClient } from '@angular/common/http';
import { bootstrapApplication } from '@angular/platform-browser';
import { provideAnimations } from '@angular/platform-browser/animations';
import { Routes, provideRouter } from '@angular/router';
import { AppComponent } from '@app/components/app/app.component';
import { MainPageComponent } from '@app/pages/main-page/main-page.component';
import { FeatureComponent } from '@app/pages/feature/feature.component';
import { SummaryComponent } from '@app/pages/summary/summary.component';

const routes: Routes = [
    { path: '', redirectTo: '/home', pathMatch: 'full' },
    { path: 'home', component: MainPageComponent },
    { path: 'feature/:fileName', component: FeatureComponent },
    { path: 'summary/:fileName', component: SummaryComponent },
    { path: 'dashboard/:fileName', component: FeatureComponent },
    { path: '**', redirectTo: '/home' },
];

bootstrapApplication(AppComponent, {
    providers: [provideHttpClient(), provideRouter(routes), provideAnimations()],
})
