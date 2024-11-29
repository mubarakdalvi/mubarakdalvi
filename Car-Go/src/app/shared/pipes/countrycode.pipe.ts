import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
    name: 'countrycode',
    standalone: false
})
export class CountrycodePipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
