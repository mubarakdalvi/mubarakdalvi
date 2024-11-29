import { Component } from '@angular/core';
import { Router } from '@angular/router';



@Component({
    selector: 'app-accounts',
    templateUrl: './accounts.component.html',
    styleUrl: './accounts.component.css',
    standalone: false
})
export class AccountsComponent {
  constructor(private router: Router) {}

  ngOnInit() {}

}
