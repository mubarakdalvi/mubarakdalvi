import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
})
export class HeaderComponent {
  users = [
    {
      name: 'asdfghjk',
      email: 'asdft@dfghj.com',
      position: 'default',
      accessGroup: 'USER',
    },
    {
      name: 'asdfghjksadasd',
      email: 'asdfdasdasdt@dfghj.com',
      position: 'default',
      accessGroup: 'USER',
    },
  ];

  isUserVisible = false;

  openUser(): void {
    this.isUserVisible = true;
  }

  closeUser(): void {
    this.isUserVisible = false;
  }
}
