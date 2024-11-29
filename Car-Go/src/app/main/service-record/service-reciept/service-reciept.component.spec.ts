import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServiceRecieptComponent } from './service-reciept.component';

describe('ServiceRecieptComponent', () => {
  let component: ServiceRecieptComponent;
  let fixture: ComponentFixture<ServiceRecieptComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ServiceRecieptComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ServiceRecieptComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
