import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderModule } from './header/header/header.module';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { SharedComponent } from './main/shared/shared.component';

@NgModule({
  declarations: [AppComponent, SharedComponent],
  imports: [BrowserModule, AppRoutingModule, HeaderModule],

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, AppRoutingModule, HeaderModule, FontAwesomeModule],


  declarations: [AppComponent],
  imports: [BrowserModule, AppRoutingModule, HeaderModule, FontAwesomeModule],

  providers: [provideClientHydration()],
  bootstrap: [AppComponent],
})
export class AppModule {}
