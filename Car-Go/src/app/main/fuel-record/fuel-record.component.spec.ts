import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FuelRecordComponent } from './fuel-record.component';

describe('FuelRecordComponent', () => {
  let component: FuelRecordComponent;
  let fixture: ComponentFixture<FuelRecordComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [FuelRecordComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FuelRecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
