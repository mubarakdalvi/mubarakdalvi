import { Component } from '@angular/core';

@Component({
    selector: 'app-app-settings',
    templateUrl: './app-settings.component.html',
    styleUrl: './app-settings.component.css',
    standalone: false
})
export class AppSettingsComponent {
  hasUnsavedChanges: any;

}
