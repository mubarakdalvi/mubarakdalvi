import { Routes } from '@angular/router';
import { SignupComponent } from './header/signup/signup.component';
import { LoginComponent } from './header/login/login.component';
import { NotfoundComponent } from './header/notfound/notfound.component';
import { AboutComponent } from './header/about/about.component';

export const routes: Routes = [
  {
    path: 'login',
    component: LoginComponent,
  },
  {
    path: 'signup',
    component: SignupComponent,
  },
  {
    path: 'about',
    loadComponent: () => import('./header/about/about.component').then(mod => mod.AboutComponent) // here we are using lazy loading and with that our app speed up fater
  },
  {
    path: '',
    redirectTo: '/login',
    pathMatch: 'full', // this will alway redirect to login page
  },
  {
    path: '**',
    component: NotfoundComponent, //always add this at end, ** maens it will  try every path from top to bottom, that why in the end it is neccessary this is called wild card
  },
];
