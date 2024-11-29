import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AlertAndNotificatonsComponent } from './alert-and-notificatons.component';

describe('AlertAndNotificatonsComponent', () => {
  let component: AlertAndNotificatonsComponent;
  let fixture: ComponentFixture<AlertAndNotificatonsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AlertAndNotificatonsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AlertAndNotificatonsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
