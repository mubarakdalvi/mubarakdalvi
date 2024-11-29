import { Component, Input, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css',
})
export class UserPermissionEditModalComponent {
  @Input() isVisible: boolean = false;
  @Output() close = new EventEmitter<void>();

  userName: string = 'Admin';
  userNameInitial: string = '';

  colors: string[] = [];

  ngOnInit(): void {
    this.userNameInitial = this.userName.charAt(0).toUpperCase();
  }

  Users = [
    { id: 1, user: 'Administrator' },
    { id: 2, user: 'Manager' },
    { id: 3, user: 'User' },
  ];

  selectedUsers: { id: number; user: string }[] = [];

  userForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.userForm = this.fb.group({
      selectedUser: [null, Validators.required],
    });
  }

  closeUser(): void {
    this.isVisible = false;
    this.close.emit();
  }

  modifyUser(): void {
    if (this.userForm.valid && this.Users[0]) {
      const selectedUserId = this.selectedUsers.map((user) => user.id);
      const selectedUser = this.Users.find((user) =>
        selectedUserId.includes(user.id)
      );
      if (selectedUser && !this.selectedUsers.includes(selectedUser)) {
        this.selectedUsers.push(selectedUser);
      }

      console.log('User Modification Done', {
        selectedUser,
      });
      this.closeUser();
    } else {
      console.log('You dont have permission to perform this action');
    }
  }

  onSelectChnage(event: Event): void {
    const selectedElement = event.target as HTMLSelectElement;
    const selectOptions = Array.from(
      selectedElement.selectedOptions
    ) as HTMLOptionElement[];
    this.selectedUsers = selectOptions
      .map((option) => {
        const userId = parseInt(option.value, 10);
        return this.Users.find((user) => user.id === userId);
      })
      .filter((user) => user !== undefined) as {
      id: number;
      user: string;
    }[];
  }

  removeUser(user: any): void {
    this.selectedUsers = this.selectedUsers.filter((u) => u.id !== user.id);
  }
}
