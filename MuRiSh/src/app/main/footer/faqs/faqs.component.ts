import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CountrycodePipe } from '../../../pipes/countrycode.pipe';
import { MydirectivesDirective } from '../../../directives/mydirectives.directive';

@Component({
  selector: 'app-faqs',
  standalone: true,
  imports: [FormsModule, CommonModule, CountrycodePipe, MydirectivesDirective],
  templateUrl: './faqs.component.html',
  styleUrl: './faqs.component.css',
})
export class FaqsComponent {
  id = 1;
  name = 'myname';
  fullName = 'myname surname';
  age = 28;
  salary = 1;
  searchQuery = '';
  selectedCountry = '';

  countryKeys: string[];

  constructor() {
    const countrycodePipe = new CountrycodePipe();
    this.countryKeys = countrycodePipe.getCountryKeys();
  }

  get filteredCountryKeys(): string[] {
    const query = this.selectedCountry.toLowerCase();
    return this.countryKeys.filter((country) =>
      country.toLowerCase().includes(query)
    );
  }

}
