import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StoreDocumentRoutingModule } from './store-document-routing.module';
import { StoreDocumentsComponent } from '../store-documents/store-documents.component';
import { UploadDocumentsComponent } from '../store-documents/upload-documents/upload-documents.component';


@NgModule({
  declarations: [StoreDocumentsComponent, UploadDocumentsComponent],
  imports: [CommonModule, StoreDocumentRoutingModule],
  exports: [StoreDocumentsComponent],
})
export class StoreDocumentModule {}
