import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InsuarenceRegisterationRenewalReminderComponent } from './insuarence-registeration-renewal-reminder.component';

describe('InsuarenceRegisterationRenewalReminderComponent', () => {
  let component: InsuarenceRegisterationRenewalReminderComponent;
  let fixture: ComponentFixture<InsuarenceRegisterationRenewalReminderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [InsuarenceRegisterationRenewalReminderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InsuarenceRegisterationRenewalReminderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
