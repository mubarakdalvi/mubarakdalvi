import { Routes } from '@angular/router';
import { LoginComponent } from './header/login/login.component';

import { SignupComponent } from './header/signup/signup.component';

export const routes: Routes = [
  {
  path: 'login', component: LoginComponent
  },{
    path: 'signup' , component: SignupComponent
  }
];
