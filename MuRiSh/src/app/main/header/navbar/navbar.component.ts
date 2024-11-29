import { Component } from '@angular/core';
import { SearchComponent } from "../search/search.component";
import { ProfileComponent } from "../profile/profile.component";
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [SearchComponent, ProfileComponent, CommonModule, FormsModule, RouterLink,RouterLinkActive],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {

}
