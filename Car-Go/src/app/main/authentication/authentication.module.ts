import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthenticationRoutingModule } from './authentication-routing.module';
import { AuthenticationComponent } from '../authentication/authentication.component';
import { CreatePinComponent } from './create-pin/create-pin.component';
import { ResetPinComponent } from './reset-pin/reset-pin.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AuthenticationComponent,
    CreatePinComponent,
    ResetPinComponent,
  ],
  imports: [
    CommonModule,
    AuthenticationRoutingModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  exports: [AuthenticationComponent],
})
export class AuthenticationModule {}
