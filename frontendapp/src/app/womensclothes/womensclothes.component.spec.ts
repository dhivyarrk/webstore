import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WomensclothesComponent } from './womensclothes.component';

describe('WomensclothesComponent', () => {
  let component: WomensclothesComponent;
  let fixture: ComponentFixture<WomensclothesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [WomensclothesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WomensclothesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
