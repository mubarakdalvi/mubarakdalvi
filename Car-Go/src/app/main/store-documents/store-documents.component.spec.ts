import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StoreDocumentsComponent } from './store-documents.component';

describe('StoreDocumentsComponent', () => {
  let component: StoreDocumentsComponent;
  let fixture: ComponentFixture<StoreDocumentsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [StoreDocumentsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StoreDocumentsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
