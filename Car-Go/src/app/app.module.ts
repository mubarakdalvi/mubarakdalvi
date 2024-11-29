import { NgModule } from '@angular/core';
import {
  BrowserModule,
  provideClientHydration,
} from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainModule } from './main/main.module';
import { AuthorizeModule } from './authorize/authorize.module';
import { RegisterModule } from './register/register.module';
import { MainComponent } from './main/main.component';
import { AuthorizeComponent } from './authorize/authorize.component';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatIconModule } from '@angular/material/icon';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

@NgModule({
  declarations: [AppComponent, MainComponent, AuthorizeComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MainModule,
    AuthorizeModule,
    RegisterModule,
    BrowserAnimationsModule,
    MatIconModule,
  ],
  providers: [provideClientHydration(), provideHttpClient(withFetch()), provideAnimationsAsync()],
  bootstrap: [AppComponent],
})
export class AppModule {}
