import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReadyToGoVehiclesComponent } from './ready-to-go-vehicles.component';

describe('ReadyToGoVehiclesComponent', () => {
  let component: ReadyToGoVehiclesComponent;
  let fixture: ComponentFixture<ReadyToGoVehiclesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ReadyToGoVehiclesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ReadyToGoVehiclesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
