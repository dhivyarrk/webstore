import { Routes } from '@angular/router';
import { LandingpageComponent } from './landingpage/landingpage.component';
import { SignupComponent } from './signup/signup.component';

export const routes: Routes = [
    { path: '', component: LandingpageComponent }, // Default route
    { path: 'signup', component: SignupComponent }, 
];
