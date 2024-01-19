<?php

namespace App\Http\Controllers;

use App\Models\websites;
use App\Http\Controllers\Controller;
use App\Http\Requests\StorewebsitesRequest;
use App\Http\Requests\UpdatewebsitesRequest;

class WebsitesController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StorewebsitesRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(websites $websites)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(websites $websites)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdatewebsitesRequest $request, websites $websites)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(websites $websites)
    {
        //
    }

    public function view_website()
    {
        $view_website  = Website::get()->all();
        return response()->json($view_website);
    }

    // public function setWebsiteName(Request $request)
    // {
    //     $request->validate([
    //         'name' => 'required|string',
    //     ]);

    //     Setting::updateOrCreate(['key' => 'website_name'], ['value' => $request->input('name')]);

    //     return response()->json(['message' => 'Website name set successfully']);
    // }

    // public function getWebsiteName()
    // {
    //     $websiteName = Setting::where('key', 'website_name')->value('value');
    //     return response()->json(['name' => $websiteName]);
    // }

}
