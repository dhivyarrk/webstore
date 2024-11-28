import { Routes } from '@angular/router';
import { LandingpageComponent } from './landingpage/landingpage.component';
import { SignupComponent } from './signup/signup.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { WomensclothesComponent } from './womensclothes/womensclothes.component';

export const routes: Routes = [
    { path: '', component: LandingpageComponent }, // Default route
    { path: 'signup', component: SignupComponent },
    { path: 'dashboard',
        component: DashboardComponent,
        children: [
          { path: 'womenclothes', component: WomensclothesComponent }, // Child route
        ], },
];
