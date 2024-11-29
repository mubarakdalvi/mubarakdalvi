import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AuthorizeRoutingModule } from './authorize-routing.module';
import { LoginComponent } from './login/login.component';
import { RouterOutlet } from '@angular/router';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { SetPasswordComponent } from './set-password/set-password.component';

@NgModule({
  declarations: [
    LoginComponent,
    ForgotPasswordComponent,
    SetPasswordComponent,
  ],
  imports: [CommonModule, AuthorizeRoutingModule, RouterOutlet],
  exports: [],
})
export class AuthorizeModule {}
