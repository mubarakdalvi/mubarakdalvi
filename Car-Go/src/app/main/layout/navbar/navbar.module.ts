import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchComponent } from './search/search.component';
import { SharedModule } from '../../../shared/shared.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AccountsModule } from '../../accounts/accounts.module';
import { ProfileDropdownComponent } from './profile-dropdown/profile-dropdown.component';
import { RouterModule } from '@angular/router';
import { MatIconModule } from '@angular/material/icon';

@NgModule({
  declarations: [SearchComponent, ProfileDropdownComponent],
  imports: [
    CommonModule,
    SharedModule,
    AccountsModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    MatIconModule,
  ],
  exports: [SearchComponent, ProfileDropdownComponent],
})
export class NavbarModule {}
