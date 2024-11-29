import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class MyservicesService {
  constructor(public http: HttpClient) {} // we will inject depency here

  getservice() {
    return this.http.get(
      'https://api.chucknorris.io/jokes/random?category=dev'
    );
  }
}
