import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CommonModalComponent } from './common-modal/common-modal.component';
import { CountrycodePipe } from './pipes/countrycode.pipe';
import { DropdownDirective } from './directives/dropdown.directive';
import { ProfilModalComponent } from './profil-modal/profil-modal.component';

const components = [CommonModalComponent];

const directives = [DropdownDirective];

const pipes = [CountrycodePipe];

@NgModule({
  declarations: [
    ...components,
    ...directives,
    ...pipes,
    ProfilModalComponent,
  ],
  imports: [CommonModule],
  exports: [...components, ...directives, ...pipes],
})
export class SharedModule {}
